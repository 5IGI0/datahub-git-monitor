from datetime import datetime
import atexit

from .easy_req import easy_req

global __individuals_cache
__individuals_cache = {}

def push_individual(
    emails      :list[str]      =[],
    usernames   :list[str]      =[],
    realnames   :list[str]      =[],
    names       :list[str]      =[],
    first_seen  :datetime|None  =None,
    last_seen   :datetime|None  =None,
    source      :str            =None
):
    global __individuals_cache
    # we need a first_seen or last_seen at least (to be able to set the other one)
    assert(first_seen is not None or last_seen is not None)
    # for now, the search for individuals is based solely on email, so one is at least needed.
    assert(len(emails) != 0 and source is not None)
    # what's the purpose of an email if we don't have any meta linked to it?
    assert(len(usernames) != 0 or len(realnames) != 0 or len(names) != 0)

    if first_seen is None:
        first_seen = last_seen
    elif last_seen is None:
        last_seen = first_seen

    # remove duplicates + sort
    emails      = tuple(sorted(list(set(emails))))
    usernames   = tuple(sorted(list(set(usernames))))
    realnames   = tuple(sorted(list(set(realnames))))
    names       = tuple(sorted(list(set(names))))

    key = (emails, usernames, realnames, names)

    individual = __individuals_cache.get(key, None)
    if individual is None:
        __individuals_cache[key] = (min(first_seen, last_seen), max(first_seen, last_seen), [source])
    else:
        __individuals_cache[key] = (
            min(first_seen, last_seen, individual[0], individual[1]),
            max(first_seen, last_seen, individual[0], individual[1]),
            list(set(individual[2] + [source])))

    if len(__individuals_cache) == 5000:
        flush_individuals()

def flush_individuals():
    global __individuals_cache
    if len(__individuals_cache) == 0:
        return

    individuals = __individuals_cache
    __individuals_cache = {}

    data = []
    for k, v in individuals.items():
        data.append({
            "emails":       list(k[0]),
            "usernames":    list(k[1]),
            "realnames":    list(k[2]),
            "names":        list(k[3]),
            "first_seen":   v[0].isoformat(),
            "last_seen":    v[1].isoformat(),
            "sources":      v[2]
        })
    easy_req("individuals/add", data)

atexit.register(flush_individuals)