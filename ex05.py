def main():
    print("This program illustrates a chaotic function")
    n= eval(input("how many numbers should i print? "))
    x= eval(input("enter a number between 0 and 1: "))
    for i in range(n):
        x= 3.9 * x * (1 - x)
        print(x)
main()