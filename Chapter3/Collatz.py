def collatz(n):
    while n != 1:
        if n % 2==0:
            n = (n//2)
            return (print(int(n)))
        elif n % 2==1:
            n = (3*n+1)
            return (print(int(n)))
        continue

print("Enter number: ")
try:
    n = (int(input()))
except ValueError:
          print("Enter an Integer")
collatz(n)
