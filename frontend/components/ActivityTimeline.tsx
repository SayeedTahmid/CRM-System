import React from "react";

export type Activity = {
  id: string;
  type: string;
  subject: string;
  description?: string;
  dueDate?: string;
  completed?: boolean;
};

type ActivityTimelineProps = {
  activities: Activity[];
};

export function ActivityTimeline({ activities }: ActivityTimelineProps) {
  return (
    <section className="card">
      <h3>Recent Activities</h3>
      <div style={{ display: "grid", gap: "1rem" }}>
        {activities.map((activity) => (
          <article
            key={activity.id}
            style={{
              background: "rgba(15,23,42,0.6)",
              padding: "1rem",
              borderRadius: "12px",
              border: "1px solid rgba(168,85,247,0.2)"
            }}
          >
            <header style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <span style={{ textTransform: "uppercase", fontSize: "0.7rem", letterSpacing: "0.1em", color: "var(--purple-500)" }}>
                {activity.type}
              </span>
              {activity.dueDate && (
                <time style={{ fontSize: "0.75rem", color: "rgba(226,232,240,0.7)" }}>
                  {new Date(activity.dueDate).toLocaleString()}
                </time>
              )}
            </header>
            <h4 style={{ margin: "0.5rem 0", fontSize: "1.1rem" }}>{activity.subject}</h4>
            {activity.description && <p style={{ margin: 0, color: "rgba(226,232,240,0.75)" }}>{activity.description}</p>}
            {activity.completed && <span style={{ fontSize: "0.75rem", color: "#22c55e" }}>Completed</span>}
          </article>
        ))}
        {activities.length === 0 && <p>No activities recorded yet.</p>}
      </div>
    </section>
  );
}
