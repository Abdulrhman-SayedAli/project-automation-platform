FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      bash \
      build-essential \
      ca-certificates \
      curl \
      docker-cli \
      git \
      nodejs \
      npm \
      python3 \
      python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspaces

