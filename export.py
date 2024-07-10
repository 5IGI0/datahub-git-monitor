from libdatahub import push_individual
from datetime import datetime

remote_cache = {}

with open("commits.csv", "r") as fp:
    for line in fp:
        line = line.strip().split("\t")

        if len(line) != 4:
            continue

        if line[3].startswith("kernel-lore-inboxes"):
            source = "kernel.org inboxe: "+('-'.join(line[3][20:].split("-")[:-1]))
        else:
            source = remote_cache.get(line[3])
            if source is None:
                with open(line[3]+"/config") as fp:
                    source = "git repo: " + fp.read().split('[remote "origin"]\n\turl = ')[1].split("\n")[0].strip()
                remote_cache[line[3]] = source

        push_individual(
            emails=[line[2]],
            names=[line[1]],
            first_seen=datetime.fromisoformat(line[0]),
            source=source
        )