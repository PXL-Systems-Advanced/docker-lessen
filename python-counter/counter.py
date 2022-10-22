import time

starttime = time.time()
count = 0

while True:
    count += 1
    print(count)
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))
