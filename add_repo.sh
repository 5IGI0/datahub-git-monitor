#!/bin/sh

PATH="/usr/local/bin:/usr/bin:/bin"

if [ ! $# -eq 1 ]
then
	echo "Usage: $0 <url>"
	exit 1
fi

DST_PATH='gits/'"$(echo "$1"|cut -d'/' -f3-|tr '/' '-'|tr ' ' '_')"

git clone --mirror "$1" "$DST_PATH"
./list_commits.sh "$DST_PATH"

