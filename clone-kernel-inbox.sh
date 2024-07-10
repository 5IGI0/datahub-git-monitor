#!/bin/sh

PATH="/usr/local/bin:/usr/bin:/bin"

if [ ! $# -eq 1 ]
then
	echo "Usage: $0 <list name>"
	exit 1
fi

mkdir -p kernel-lore-inboxes/

for i in $(seq 0 100);
do
	if ! git clone --mirror "http://lore.kernel.org/$1/$i" kernel-lore-inboxes/"$1-$i";
	then
		exit 0
	fi
	./list_commits.sh kernel-lore-inboxes/"$1-$i"
done
