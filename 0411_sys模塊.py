import sys, time

# 之前的進度條
for i in range(10):
    sys.stdout.write(str(i))
    sys.stdout.flush()
    time.sleep(0.1)

print(sys.version)
