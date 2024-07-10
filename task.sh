#!/bin/sh

PATH="/usr/local/bin:/usr/bin:/bin"

mkdir -p kernel-lore-inboxes gits archives

find gits/ kernel-lore-inboxes/ -maxdepth 1 -mindepth 1 -type d -exec \
    ./fetch_commits.sh '{}' ';'

echo "sending to datahub..."
if python3 export.py; then
    gzip -c commits.csv >> "archives/$(date +%Y-%m-%d).csv.gz"
    rm commits.csv
fi