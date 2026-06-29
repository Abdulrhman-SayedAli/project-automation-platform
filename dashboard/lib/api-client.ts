const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export type ApiError = {
  success: false;
  error: {
    code: string;
    message: string;
  };
};

export async function apiGet<TResponse>(path: string): Promise<TResponse> {
  const response = await fetch(`${API_URL}${path}`, {
    headers: {
      Accept: "application/json"
    },
    cache: "no-store"
  });

  if (!response.ok) {
    const payload = (await response.json().catch(() => null)) as ApiError | null;
    throw new Error(payload?.error.message ?? `API request failed with ${response.status}`);
  }

  return (await response.json()) as TResponse;
}

