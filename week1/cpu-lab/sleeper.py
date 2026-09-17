import time

deadline = time.monotonic() + 30

while time.monotonic() < deadline:
    time.sleep(0.1)

print("Sleeper finished.")
