def main():
    print("This program illustrates a chaotic function")
    x= eval(input("enter firs number between 0 and 1: "))
    y = eval(input("enter a second number between 0 and 1:"))
    for i in range(10):
        x= 3.9 * x * (1 - x)
    for i in range(10):
        y= 3.9 * y * (1 - y)
        print(x, y)
main()