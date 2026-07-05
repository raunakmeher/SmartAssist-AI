function SimilarTickets({ tickets }) {
  if (!tickets || tickets.length === 0) return null;

  return (
    <div className="section">
      <h2>Similar Tickets</h2>

      <table className="ticket-table">
        <thead>
          <tr>
            <th>Similarity</th>

            <th>Department</th>

            <th>Priority</th>

            <th>Ticket Preview</th>
          </tr>
        </thead>

        <tbody>
          {tickets.map((ticket, index) => (
            <tr key={index}>
              <td>{ticket.similarity}%</td>

              <td>{ticket.department}</td>

              <td>{ticket.priority}</td>

              <td>{ticket.ticket}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default SimilarTickets;
