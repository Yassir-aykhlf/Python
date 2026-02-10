import os

pid: int = os.getpid()

# with open(f"/proc/self/status", "r") as f:
with open(f"/proc/{pid}/status", "r") as f:
    for line in f:
        if  line.startswith("Name:") or \
            line.startswith("State:") or \
            line.startswith("VmRSS:"):
            print(' '.join(line.split()))