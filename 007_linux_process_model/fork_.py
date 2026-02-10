import os
import time
import sys

print(f"Starting... PID: {os.getpid()}")
pid: int = os.fork()

if pid == 0:
    print(f"I am Child (PID: {os.getpid()})")
    time.sleep(5)
    print("Child exiting...")
    sys.exit(0)
elif pid > 0:
    print(f"I am Parent (PID: {os.getpid()}, Child is {pid})")
    os.wait()
