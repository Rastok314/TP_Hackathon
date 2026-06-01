#!/bin/bash

set -e

cd "$(dirname "$0")"

echo "=== CHECK ENV ==="

if [ ! -d "venv" ]; then
    echo "Creating venv..."
    python3 -m venv venv
fi

source venv/bin/activate

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

if [ "$1" = "test" ]; then
    echo "=== RUN TESTS ==="
    PYTHONPATH=. pytest -q
    exit 0
fi

echo "=== RUN APP ==="
python src/main.py