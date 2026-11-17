import tracemalloc


def load_all(path):
    with open(path) as log:
        return log.read().splitlines()


def stream(path):
    with open(path) as log:
        for line in log:
            yield line.rstrip("\n")


for way in (load_all, stream):
    tracemalloc.start()
    failures = 0
    for line in way("year_auth.log"):
        if "Failed password" in line:
            failures += 1
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    print(f"{way.__name__:<9} {peak / 1e6:7.2f} MB  {failures:,} failures")
