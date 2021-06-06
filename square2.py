n = int(input("How big is the squre? "))
w = 1
while w <= n:
    print(n * "*")
    w += 1
if n == 0:
    print("Please choose a better number next time")