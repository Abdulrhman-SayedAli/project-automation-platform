export type PlatformStatus = "CREATED" | "PLANNING" | "IMPLEMENTING" | "COMPLETED" | "BLOCKED" | "FAILED";

export type HealthResponse = {
  success: true;
  status: string;
  service: string;
  version: string;
  environment: string;
  components: Record<string, { status: string; detail?: string | null }>;
};

