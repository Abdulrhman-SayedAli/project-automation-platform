import { PageHeader } from "@/components/page-header";
import { EmptyState } from "@/components/empty-state";

export default function ProjectsPage() {
  return (
    <main className="space-y-6">
      <PageHeader title="Projects" description="Repository-backed automation projects" />
      <EmptyState title="No projects" detail="Project records will appear after API integration." />
    </main>
  );
}

