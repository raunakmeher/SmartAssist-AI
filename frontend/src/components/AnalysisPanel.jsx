import MetricCard from "./MetricCard";
import SimilarTickets from "./SimilarTickets";
import LoadingSpinner from "./LoadingSpinner";
function priorityColor(priority) {
  if (!priority) return "#1F2937";

  switch (priority.toLowerCase()) {
    case "high":
      return "#991B1B";

    case "medium":
      return "#B45309";

    case "low":
      return "#166534";

    default:
      return "#1F2937";
  }
}

function AnalysisPanel({ analysis, loading }) {
  if (loading) {
    return (
      <div className="section">
        <h2>AI Analysis</h2>

        <LoadingSpinner />
      </div>
    );
  }

  if (!analysis)
    return (
      <div className="section">
        <h2>AI Analysis</h2>
        <p style={{ color: "#6B7280" }}>
          Submit a customer ticket to receive AI-powered analysis, department
          recommendation, priority assessment, and similar historical cases.
        </p>
      </div>
    );

  return (
    <>
      <div className="section">
        <h2>Summary</h2>

        <p>{analysis.summary}</p>
      </div>

      <div className="metrics-grid">
        <MetricCard
          title="Department"
          value={analysis.recommendedDepartment}
          color="#1F2937"
        />

        <MetricCard
          title="Priority"
          value={analysis.recommendedPriority.toUpperCase()}
          color={priorityColor(analysis.recommendedPriority)}
        />

        <MetricCard
          title="Sentiment"
          value={analysis.sentiment}
          color="#1F2937"
        />

        <MetricCard
          title="Confidence"
          value={analysis.confidence}
          color="#1F2937"
        />
      </div>

      <div className="section">
        <h2>Suggested Resolution</h2>

        <p>{analysis.suggestedResolution}</p>
      </div>

      <SimilarTickets tickets={analysis.similarTickets} />
    </>
  );
}

export default AnalysisPanel;
