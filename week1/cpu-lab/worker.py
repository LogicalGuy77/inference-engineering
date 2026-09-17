import time

deadline = time.monotonic() + 30

while time.monotonic() < deadline:
    pass

print("Worker finished.")
