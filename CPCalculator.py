import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factorization(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors

def catalan_number(n):
    if n == 0 or n == 1:
        return 1
    catalan = [0] * (n + 1)
    catalan[0] = catalan[1] = 1
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]
    return catalan[n]

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def exponentiation(base, exp):
    return base ** exp

def factorial(n):
    return math.factorial(n)

def permutations(n, r):
    return math.factorial(n) // math.factorial(n - r)

def combinations(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def to_binary(n):
    return bin(n).replace("0b", "")

def to_octal(n):
    return oct(n).replace("0o", "")

def to_hexadecimal(n):
    return hex(n).replace("0x", "")

def from_binary(s):
    return int(s, 2)

def from_octal(s):
    return int(s, 8)

def from_hexadecimal(s):
    return int(s, 16)

def main():
    print("Welcome to the Competitive Programmer's Calculator!")
    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Check if a number is prime")
        print("6. Prime factorization")
        print("7. Catalan number")
        print("8. Fibonacci number")
        print("9. GCD")
        print("10. LCM")
        print("11. Exponentiation")
        print("12. Factorial")
        print("13. Permutations")
        print("14. Combinations")
        print("15. Modular Exponentiation")
        print("16. Binary Representation")
        print("17. Octal Representation")
        print("18. Hexadecimal Representation")
        print("19. Convert from Binary")
        print("20. Convert from Octal")
        print("21. Convert from Hexadecimal")
        print("22. Exit")
        
        choice = input("Enter your choice (1-22): ")
        
        if choice == '22':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        
        if choice == '1':
            print(f"Result: {add(a, b)}")
        elif choice == '2':
            print(f"Result: {subtract(a, b)}")
        elif choice == '3':
            print(f"Result: {multiply(a, b)}")
        elif choice == '4':
            print(f"Result: {divide(a, b)}")
        elif choice == '5':
            n = int(input("Enter a number: "))
            print(f"Is {n} prime? {'Yes' if is_prime(n) else 'No'}")
        elif choice == '6':
            n = int(input("Enter a number: "))
            print(f"Prime factorization of {n}: {prime_factorization(n)}")
        elif choice == '7':
            n = int(input("Enter a number: "))
            print(f"Catalan number C({n}): {catalan_number(n)}")
        elif choice == '8':
            n = int(input("Enter a number: "))
            print(f"Fibonacci number F({n}): {fibonacci(n)}")
        elif choice == '9':
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            print(f"GCD of {a} and {b}: {gcd(a, b)}")
        elif choice == '10':
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            print(f"LCM of {a} and {b}: {lcm(a, b)}")
        elif choice == '11':
            base = float(input("Enter the base: "))
            exp = int(input("Enter the exponent: "))
            print(f"Result: {exponentiation(base, exp)}")
        elif choice == '12':
            n = int(input("Enter a number: "))
            print(f"Factorial of {n}: {factorial(n)}")
        elif choice == '13':
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))
            print(f"Permutations P({n}, {r}): {permutations(n, r)}")
        elif choice == '14':
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))
            print(f"Combinations C({n}, {r}): {combinations(n, r)}")
        elif choice == '15':
            base = int(input("Enter the base: "))
            exp = int(input("Enter the exponent: "))
            mod = int(input("Enter the modulus: "))
            print(f"Result: {modular_exponentiation(base, exp, mod)}")
        elif choice == '16':
            n = int(input("Enter a number: "))
            print(f"Binary representation of {n}: {to_binary(n)}")
        elif choice == '17':
            n = int(input("Enter a number: "))
            print(f"Octal representation of {n}: {to_octal(n)}")
        elif choice == '18':
            n = int(input("Enter a number: "))
            print(f"Hexadecimal representation of {n}: {to_hexadecimal(n)}")
        elif choice == '19':
            s = input("Enter a binary string: ")
            print(f"Decimal representation of binary {s}: {from_binary(s)}")
        elif choice == '20':
            s = input("Enter an octal string: ")
            print(f"Decimal representation of octal {s}: {from_octal(s)}")
        elif choice == '21':
            s = input("Enter a hexadecimal string: ")
            print(f"Decimal representation of hexadecimal {s}: {from_hexadecimal(s)}")
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
