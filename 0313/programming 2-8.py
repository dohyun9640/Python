number = int(input("정수="))
n1 = number % 10
number = number // 10

n2 = number % 10
number = number // 10

n3 = number % 10
number = number // 10

n4 = number

total_sum = n1+n2+n3+n4

print(total_sum)
