Num1 = int(input())
Num2 = int(input())

A = []
B = []

if Num1 > Num2:
    Num3 = Num1

else:
    Num3 = Num2

for i in range(1,Num3+1):
    if Num1 % i == 0 and Num2 % i == 0:
        A.append(i)
        
print(A[len(A) - 1])
