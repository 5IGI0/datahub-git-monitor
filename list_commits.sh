#!/bin/sh

if [ ! $# -eq 1 ]
then
	echo "Usage: $0 <url>"
	exit 1
fi

echo "listing $1's commits..."
git -C "$1" log --format='%aI%x09%an%x09%ae%x09'"$1" >> commits.csv