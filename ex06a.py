def main():
    print("This program illustrates a chaotic function")
    x= eval(input("enter a number between 0 and 1: "))
    for i in range(100):
        x= 3.9 * x * (1 - x)
        print(x)
main()