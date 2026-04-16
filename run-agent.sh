#!/usr/bin/env bash
set -Eeuo pipefail

log() { echo "[INFO] $*"; }

# move to project root
cd "$(dirname "$0")"

log "Loading environment variables"
set -a
source news-agent/.env
set +a

log "Running AI News Agent"
.ai-env/bin/python news-agent/main.py

log "Done"