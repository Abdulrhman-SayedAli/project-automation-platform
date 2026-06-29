import { cn } from "@/lib/utils";

type Status = "ready" | "pending" | "failed";

const statusClasses: Record<Status, string> = {
  ready: "border-emerald-200 bg-emerald-50 text-emerald-800",
  pending: "border-amber-200 bg-amber-50 text-amber-800",
  failed: "border-red-200 bg-red-50 text-red-800"
};

type StatusBadgeProps = {
  label: string;
  status: Status;
};

export function StatusBadge({ label, status }: StatusBadgeProps) {
  return (
    <span
      className={cn(
        "inline-flex min-h-8 items-center rounded-md border px-3 text-sm font-medium",
        statusClasses[status]
      )}
    >
      {label}
    </span>
  );
}

