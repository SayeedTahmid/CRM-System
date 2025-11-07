import { Navigation } from "../../components/Navigation";
import { ProtectedRoute } from "../../components/ProtectedRoute";
import { ActivityTimeline } from "../../components/ActivityTimeline";
import { PipelineBoard } from "../../components/PipelineBoard";
import { TaskList } from "../../components/TaskList";

export default function DashboardPage() {
  return (
    <ProtectedRoute>
      <Navigation />
      <main>
        <h1 style={{ fontSize: "2rem" }}>Team dashboard</h1>
        <p style={{ color: "rgba(226,232,240,0.75)" }}>
          A live look at your pipeline and activity stream.
        </p>
        <section style={{ display: "grid", gap: "1.5rem", marginTop: "2rem" }}>
          <PipelineBoard deals={[]} />
          <ActivityTimeline activities={[]} />
          <TaskList tasks={[]} />
        </section>
      </main>
    </ProtectedRoute>
  );
}
