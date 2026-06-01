#!/bin/bash

set -e

cd "$(dirname "$0")"

echo "=== CHECK ENV ==="

if [ ! -f "venv/bin/activate" ]; then
    echo "Creating/Recreating venv..."
    rm -rf venv
    python3 -m venv venv
fi

source venv/bin/activate

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

if [ "$1" = "start" ] || [ -z "$1" ]; then
    echo "=== RUN APP ==="
    python -m src.main
    exit 0
fi

if [ "$1" = "test" ]; then
    echo "=== RUN TESTS ==="
    python -m pytest -q
    exit 0
fi

echo "Usage: start | test"