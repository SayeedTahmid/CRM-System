import { Navigation } from "../components/Navigation";
import { ActivityTimeline } from "../components/ActivityTimeline";
import { PipelineBoard } from "../components/PipelineBoard";
import { ReportCards } from "../components/ReportCards";
import { TaskList } from "../components/TaskList";

const mockDeals = [
  { id: "1", title: "Enterprise onboarding", value: 42000, stageName: "Discovery" },
  { id: "2", title: "Contract renewal", value: 18000, stageName: "Negotiation" }
];

const mockActivities = [
  { id: "a1", type: "email", subject: "Sent pricing update", description: "Shared the updated pricing deck." },
  { id: "a2", type: "call", subject: "Spoke with CTO", description: "Discussed integration roadmap." }
];

const mockTasks = [
  { id: "t1", type: "task", subject: "Prepare demo", description: "Create custom demo for Monday" },
  { id: "t2", type: "task", subject: "Update proposal", description: "Align proposal with new requirements" }
];

export default function HomePage() {
  return (
    <>
      <Navigation />
      <main>
        <header style={{ marginBottom: "2rem" }}>
          <h1 style={{ fontSize: "2.5rem", marginBottom: "0.5rem" }}>Welcome back 👋</h1>
          <p style={{ color: "rgba(226,232,240,0.75)", maxWidth: "600px" }}>
            Track deals, collaborate with your team, and close more revenue with a unified pipeline connected to Supabase and
            FastAPI services.
          </p>
        </header>

        <ReportCards
          metrics={{ totalDeals: 28, wonDeals: 9, activitiesThisWeek: 34, revenueForecast: 120000 }}
        />

        <section style={{ display: "grid", gap: "1.5rem", marginTop: "2rem" }}>
          <PipelineBoard deals={mockDeals} />
          <ActivityTimeline activities={mockActivities} />
          <TaskList tasks={mockTasks} />
        </section>
      </main>
    </>
  );
}
