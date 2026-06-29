import { EmptyState } from "@/components/empty-state";
import { PageHeader } from "@/components/page-header";

export default function WorkersPage() {
  return (
    <main className="space-y-6">
      <PageHeader title="Workers" description="Stateless execution capacity" />
      <EmptyState title="No workers" detail="Worker heartbeats will appear after worker services exist." />
    </main>
  );
}

