def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    print("pausing here")
    return divisors


def run():
    num = int(input("Ingresa un numero: "))
    print(divisors(num))
    print("Termino mi programa")


if __name__ == "__main__":
    run()
