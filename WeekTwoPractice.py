"""Find all the prime numbers between 1 to 100"""
n=100
for i in range(2, n):
    for j in range(2, i):
        if (i % j) == 0:
            break
    else:
        print(i)

for _ in range(10):
    print("*"*(_+1))
    