import time


def no_sleep(log, seconds):
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        log.readline()                   # nothing new: returns "" at once


def with_sleep(log, seconds):
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        if not log.readline():
            time.sleep(0.5)


with open("practice_auth.log") as log:
    log.seek(0, 2)                       # at the end: nothing new arrives
    for wait in (no_sleep, with_sleep):
        start = time.process_time()
        wait(log, 3)
        used = time.process_time() - start
        print(f"{wait.__name__:<11} {used:4.2f} s CPU in 3 s")
