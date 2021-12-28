print("Enter number: ")
try:
    n = (int(input()))
except ValueError:
          print("Enter an Integer")
collatz(n)
