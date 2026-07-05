# services/ai_engine.py

import faiss
import pandas as pd
import numpy as np

from collections import defaultdict

from sentence_transformers import SentenceTransformer

from transformers import (
    pipeline,
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

from utils.priority_rules import get_priority_from_rules


class AIEngine:

    def __init__(self):

        print("Loading AI models...")

        # -----------------------------
        # Embedding Model
        # -----------------------------
        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        # -----------------------------
        # Sentiment Model
        # -----------------------------
        self.sentiment_model = pipeline(
            "sentiment-analysis",
            model="cardiffnlp/twitter-roberta-base-sentiment-latest"
        )

        # -----------------------------
        # Summary Model
        # -----------------------------
        self.tokenizer = AutoTokenizer.from_pretrained(
            "google/flan-t5-base"
        )

        self.summary_model = AutoModelForSeq2SeqLM.from_pretrained(
            "google/flan-t5-base"
        )

        print("Loading saved data...")

        self.df = pd.read_pickle("models/tickets.pkl")

        self.index = faiss.read_index(
            "models/ticket_index.faiss"
        )

        print("AI Engine Ready!")
        # ---------------------------------------------------
    # Summarize Ticket
    # ---------------------------------------------------
    def summarize_ticket(self, ticket):

        prompt = f"""
Summarize this customer support ticket in one concise sentence.

Ticket:
{ticket}

Summary:
"""

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        outputs = self.summary_model.generate(
            **inputs,
            max_new_tokens=40,
            num_beams=4,
            early_stopping=True
        )

        return self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )


    # ---------------------------------------------------
    # Draft Reply
    # ---------------------------------------------------
    def generate_reply(self, ticket, department, resolution):

        prompt = f"""
You are a professional customer support executive.

Department:
{department}

Customer Ticket:
{ticket}

Suggested Resolution:
{resolution}

Write a professional email reply.

Reply:
"""

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        outputs = self.summary_model.generate(
            **inputs,
            max_new_tokens=120,
            num_beams=4,
            early_stopping=True
        )

        return self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True)


    # ---------------------------------------------------
    # Similar Ticket Search
    # ---------------------------------------------------
    def search_similar_tickets(self, ticket, top_k=5):

        query_embedding = self.embedding_model.encode(
            [ticket],
            convert_to_numpy=True
        )

        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        return scores, indices
        # ---------------------------------------------------
    # Main AI Pipeline
    # ---------------------------------------------------
    def analyze_ticket(self, ticket, top_k=5):

        # -------------------------
        # Summary
        # -------------------------
        summary = self.summarize_ticket(ticket)

        # -------------------------
        # Sentiment
        # -------------------------
        sentiment = self.sentiment_model(ticket[:512])[0]

        # -------------------------
        # Similar Tickets
        # -------------------------
        scores, indices = self.search_similar_tickets(ticket, top_k)

        similar = []

        department_scores = defaultdict(float)
        priority_scores = defaultdict(float)

        best_solution = None
        best_similarity = -1

        for score, idx in zip(scores[0], indices[0]):

            row = self.df.iloc[idx]

            similarity = float(score)

            department_scores[row["queue"]] += similarity
            priority_scores[row["priority"]] += similarity

            if similarity > best_similarity:
                best_similarity = similarity
                best_solution = row["answer"]

            similar.append({
                "similarity": round(similarity * 100, 2),
                "department": row["queue"],
                "priority": row["priority"],
                "ticket": row["text"][:250],
                "solution": row["answer"][:250]
            })

        recommended_department = max(
            department_scores,
            key=department_scores.get
        )

        historical_priority = max(
            priority_scores,
            key=priority_scores.get
        )

        final_priority = get_priority_from_rules(
            ticket,
            historical_priority
        )

        draft_reply = self.generate_reply(
            ticket,
            recommended_department,
            best_solution
        )

        return {
            "summary": summary,
            "sentiment": sentiment,
            "recommended_department": recommended_department,
            "recommended_priority": final_priority,
            "suggested_resolution": best_solution,
            "similar_tickets": similar,
            "draft_reply": draft_reply
        }