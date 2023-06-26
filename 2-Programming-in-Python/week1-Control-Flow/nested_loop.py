import time
# Outer Loop
start_time = time.time()
for i in range(100):
    # inner loop
    for j in range(10000):
        print(0, end=" ")
    print()
print(round((time.time() - start_time), 2))

# print("single line only")
# for i in range(1):
#     # inner loop
#     for j in range(10):
#         print(0, end=" ")
#     print()
