N = int(input())

new_n = 1000 - N
count = 0

for i in [500,100,50,10,5,1]:
    count += new_n // i
    new_n = new_n % i

print(count)