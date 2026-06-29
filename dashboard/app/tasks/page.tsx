import { EmptyState } from "@/components/empty-state";
import { PageHeader } from "@/components/page-header";

export default function TasksPage() {
  return (
    <main className="space-y-6">
      <PageHeader title="Tasks" description="GitHub issue backed implementation work" />
      <EmptyState title="No tasks" detail="Task rows will load from the FastAPI task endpoints." />
    </main>
  );
}

