#!/usr/bin/env bash
set -Eeuo pipefail

# -----------------------------
# Config
# -----------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR=".ai-env"
REQ_FILE="${SCRIPT_DIR}/requirements.txt"

# -----------------------------
# Logging helpers
# -----------------------------
log()   { echo -e "[INFO]  $*"; }
warn()  { echo -e "[WARN]  $*" >&2; }
error() { echo -e "[ERROR] $*" >&2; }

trap 'error "Failed at line $LINENO: $BASH_COMMAND"' ERR

# -----------------------------
# Pre-flight checks
# -----------------------------
command -v python3 >/dev/null || { error "python3 not found"; exit 1; }
command -v pip3 >/dev/null || { error "pip3 not found"; exit 1; }

# -----------------------------
# Virtual environment
# -----------------------------
if [[ ! -d "$VENV_DIR" ]]; then
  log "Creating virtual environment at $VENV_DIR"
  python3 -m venv "$VENV_DIR"
else
  log "Virtual environment already exists"
fi

log "Activating virtual environment"
source "$VENV_DIR/bin/activate"

# -----------------------------
# Pip setup
# -----------------------------
log "Upgrading pip"
python -m pip install --upgrade pip setuptools wheel

# -----------------------------
# Python dependencies
# -----------------------------
if [[ -f "$REQ_FILE" ]]; then
  log "Installing Python dependencies from $REQ_FILE"
  python -m pip install -r "$REQ_FILE"
else
  warn "requirements.txt not found — skipping Python deps"
fi

# -----------------------------
# Finish
# -----------------------------
log "Deactivating virtual environment"
deactivate

log "AI python environment setup completed successfully."
