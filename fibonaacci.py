def fibbo():
    a = 0
    b = 1
    n = int(input("Enter the number of terms: "))
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end="\n")
        a, b = b, a + b
fibbo()

