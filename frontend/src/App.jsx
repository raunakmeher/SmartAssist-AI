import { useState } from "react";
import Header from "./components/Header";
import TicketForm from "./components/TicketForm";
import AnalysisPanel from "./components/AnalysisPanel";

import "./App.css";

function App() {
  const [analysis, setAnalysis] = useState(null);

  const [loading, setLoading] = useState(false);

  return (
    <div className="container">
      <Header />

      <TicketForm setAnalysis={setAnalysis} setLoading={setLoading} />

      <AnalysisPanel analysis={analysis} loading={loading} />
    </div>
  );
}

export default App;
