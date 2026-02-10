import signal
import sys
import time

def handle_sigint(signum, frame):
    print(f"\nsignal {signum} received, shutting down...")
    time.sleep(2)
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

x: int = 0
while True:
    x += 1
    print(x)
    time.sleep(.2)