import signal
import time
import sys
import os

def handle_sigint(signal, frame):
    who = "Parent" if os.getpid() != 0 else "Child"
    print(f"\n{who} Signal {signal} received. Exiting")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

def readSatus(pid: int | str) -> None:
    path = f"/proc/{pid}/status"
    try:
        with open(path, "r") as f:
            print(f"--- Reading {path} ---")
            for line in f:
                if  line.startswith(("Name:", "State:", "VmRSS:", "PPid:")):
                    print(line.strip())
    except FileNotFoundError:
        print(f"Error: process {pid} not found")
    except PermissionError:
        print(f"Error: Permission denied reading process {pid}")

print(f"Root process ({os.getpid()}) starting...")

pid: int = os.fork()

if pid < 0:
    print(f"Fork failed!")
    exit(1)

elif pid == 0:
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    print(f"\n[Child] ({os.getpid()}), working...")
    time.sleep(20)
    print(f"\n[Child] Done. Exiting.")
    sys.exit(0)

else:
    print(f"\n[Parent] ({os.getpid()}), child is ({pid}):")
    readSatus("self")
    time.sleep(0.1)
    print(f"\n[Parent] Inspecting Child ({pid})...")
    readSatus(pid)
    print("\nWaiting for child..")
    os.wait()
    print("\nParent exiting...")
    sys.exit(0)