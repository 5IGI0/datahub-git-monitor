#!/bin/sh

PATH="/usr/local/bin:/usr/bin:/bin"

HASH_ID=$(cat "$1/refs/heads/master")
if [ -z "$HASH_ID" ]; then
	HASH_ID=$(grep 'refs/heads/master' "$1/packed-refs"|cut -d' ' -f1)
fi

echo "fetching new $1's commits..."
git -C "$1" fetch origin
echo "listing new $1's commits..."
git -C "$1" log "$HASH_ID"..HEAD --format='%aI%x09%an%x09%ae%x09'"$1" >> commits.csv
