import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8080/api",
  headers: {
    "Content-Type": "application/json",
  },
});

export const analyzeTicket = async (ticket) => {
  const response = await api.post("/analyze", {
    ticket: ticket,
  });

  return response.data;
};
