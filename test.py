import time

text = "Hello, \r\nThat was a carriage return"

for i in text:
    print(i, end='', flush=True)
    if i == '\r':
        time.sleep(0.5)
    else:
        time.sleep(0.06)
print("\nDone")