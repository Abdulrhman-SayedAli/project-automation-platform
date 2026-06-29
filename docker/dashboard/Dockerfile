FROM node:22-alpine AS deps

WORKDIR /app/dashboard
COPY dashboard/package.json dashboard/package-lock.json ./
RUN npm ci --ignore-scripts --no-audit --no-fund

FROM node:22-alpine AS builder

WORKDIR /app/dashboard
COPY --from=deps /app/dashboard/node_modules ./node_modules
COPY dashboard ./
RUN npm run build

FROM node:22-alpine AS runtime

ENV NODE_ENV=production
WORKDIR /app/dashboard

COPY --from=builder /app/dashboard/.next/standalone ./
COPY --from=builder /app/dashboard/.next/static ./.next/static
COPY --from=builder /app/dashboard/public ./public

EXPOSE 3000

CMD ["node", "server.js"]

