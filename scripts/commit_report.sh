#!/usr/bin/env bash
# Leader tool: commits per author. Usage: ./scripts/commit_report.sh [since] [until]
SINCE=${1:-"2026-01-01"}; UNTIL=${2:-"now"}
echo "Commits per author (all branches) since $SINCE:"
git fetch --all --quiet
git shortlog -sne --all --since="$SINCE" --until="$UNTIL"
echo; echo "Branches:"; git branch -r
