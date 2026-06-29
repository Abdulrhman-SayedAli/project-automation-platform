import { EmptyState } from "@/components/empty-state";
import { PageHeader } from "@/components/page-header";

export default function EventsPage() {
  return (
    <main className="space-y-6">
      <PageHeader title="Events" description="Append-only platform activity" />
      <EmptyState title="No events" detail="Events will stream from the API event boundary." />
    </main>
  );
}

