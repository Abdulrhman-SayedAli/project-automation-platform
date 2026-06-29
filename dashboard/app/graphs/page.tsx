import { EmptyState } from "@/components/empty-state";
import { PageHeader } from "@/components/page-header";

export default function GraphsPage() {
  return (
    <main className="space-y-6">
      <PageHeader title="Graphs" description="Project and task graph execution state" />
      <EmptyState title="No graph executions" detail="Graph state is reserved for the LangGraph milestone." />
    </main>
  );
}

