import React from "react";

type Deal = {
  id: string;
  title: string;
  value: number;
  stageName: string;
};

type PipelineBoardProps = {
  deals: Deal[];
};

export function PipelineBoard({ deals }: PipelineBoardProps) {
  const grouped = deals.reduce<Record<string, Deal[]>>((acc, deal) => {
    if (!acc[deal.stageName]) {
      acc[deal.stageName] = [];
    }
    acc[deal.stageName].push(deal);
    return acc;
  }, {});

  return (
    <section className="card">
      <h3>Sales Pipeline</h3>
      <div style={{ display: "grid", gap: "1rem", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))" }}>
        {Object.entries(grouped).map(([stage, stageDeals]) => (
          <div key={stage} style={{ background: "rgba(2,6,23,0.6)", borderRadius: "12px", padding: "1rem" }}>
            <h4 style={{ marginTop: 0, color: "var(--purple-500)", textTransform: "uppercase", fontSize: "0.75rem" }}>{stage}</h4>
            <ul style={{ listStyle: "none", padding: 0, margin: 0, display: "grid", gap: "0.75rem" }}>
              {stageDeals.map((deal) => (
                <li
                  key={deal.id}
                  style={{
                    background: "linear-gradient(140deg, rgba(90,50,120,0.25), rgba(8,47,73,0.4))",
                    borderRadius: "10px",
                    padding: "0.75rem"
                  }}
                >
                  <div style={{ fontWeight: 600 }}>{deal.title}</div>
                  <div style={{ color: "rgba(226,232,240,0.7)", fontSize: "0.85rem" }}>${deal.value.toLocaleString()}</div>
                </li>
              ))}
            </ul>
          </div>
        ))}
        {Object.keys(grouped).length === 0 && <p>No deals yet. Start by creating one in the pipeline.</p>}
      </div>
    </section>
  );
}
