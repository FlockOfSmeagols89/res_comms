#!/usr/bin/env bash
set -euo pipefail
VER=${1:-dev}
mkdir -p RELEASES
python3 software/scripts/calc_checksums.py > RELEASES/SHA256SUMS-$VER.txt
echo "Release $VER created. Verify with: sha256sum -c RELEASES/SHA256SUMS-$VER.txt"
