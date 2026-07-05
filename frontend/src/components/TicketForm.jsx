import { useState } from "react";
import { analyzeTicket } from "../services/api";

function TicketForm({ setAnalysis, setLoading }) {
  const [ticket, setTicket] = useState("");

  const submit = async () => {
    if (ticket.trim() === "") {
      alert("Please enter a ticket.");

      return;
    }

    try {
      setLoading(true);

      const result = await analyzeTicket(ticket);

      setAnalysis(result);
    } catch (e) {
      alert("Failed to analyze ticket.");

      console.log(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="section">
      <h2>Customer Ticket</h2>

      <textarea
        placeholder="Describe the customer's issue..."
        value={ticket}
        onChange={(e) => setTicket(e.target.value)}
      />

      <button onClick={submit}>Analyze Ticket</button>
    </div>
  );
}

export default TicketForm;
