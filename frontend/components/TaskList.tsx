import React from "react";
import type { Activity } from "./ActivityTimeline";

type TaskListProps = {
  tasks: Activity[];
};

export function TaskList({ tasks }: TaskListProps) {
  return (
    <section className="card">
      <h3>Upcoming Tasks</h3>
      <ul style={{ listStyle: "none", padding: 0, margin: 0, display: "grid", gap: "0.75rem" }}>
        {tasks.map((task) => (
          <li
            key={task.id}
            style={{
              display: "flex",
              flexDirection: "column",
              gap: "0.3rem",
              background: "rgba(15,23,42,0.6)",
              padding: "0.75rem",
              borderRadius: "10px",
              border: "1px solid rgba(148,163,184,0.15)"
            }}
          >
            <span style={{ fontWeight: 600 }}>{task.subject}</span>
            {task.dueDate && (
              <time style={{ fontSize: "0.8rem", color: "rgba(226,232,240,0.7)" }}>
                Due {new Date(task.dueDate).toLocaleString()}
              </time>
            )}
            {task.description && <p style={{ margin: 0, color: "rgba(226,232,240,0.7)" }}>{task.description}</p>}
          </li>
        ))}
        {tasks.length === 0 && <p>No tasks scheduled. Relax!</p>}
      </ul>
    </section>
  );
}
