function MetricCard({ title, value, color }) {
  return (
    <div className="metric-card">
      <p className="metric-title">{title}</p>

      <h3 className="metric-value" style={{ color }}>
        {value}
      </h3>
    </div>
  );
}

export default MetricCard;
