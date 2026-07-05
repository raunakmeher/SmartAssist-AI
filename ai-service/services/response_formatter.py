import re


def clean_text(text):
    if not text:
        return ""

    # Remove placeholders
    PLACEHOLDER_MAP = {
    "<name>": "Customer",
    "<acc_num>": "account number",
    "<tel_num>": "phone number",
    "[Name]": "Customer",
    "[acc_num]": "account number"
    }

    for old, new in PLACEHOLDER_MAP.items():
        text = text.replace(old, new)

    return text


def format_response(result):

    sentiment = result["sentiment"]

    return {

        "summary": clean_text(result["summary"]),

        "sentiment": sentiment["label"].capitalize(),

        "sentimentConfidence":
            f"{sentiment['score']*100:.2f}%",

        "recommendedDepartment":
            result["recommended_department"],

        "recommendedPriority":
            result["recommended_priority"].capitalize(),

        "suggestedResolution":
            clean_text(result["suggested_resolution"]),

        "draftReply":
            clean_text(result["draft_reply"]),

        "similarTickets": result["similar_tickets"],

        "confidence":
            f"{result['similar_tickets'][0]['similarity']:.2f}%"
    }