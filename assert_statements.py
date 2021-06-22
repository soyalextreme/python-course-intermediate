def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    try:
        num = input("Enter a number: ")
        assert num.isnumeric(), "Not a number, please run again"
        assert int(num) > 0, "Please enter a positive number"
        print(divisors(int(num)))
        print("Finish!!")
    except AssertionError as assertion_error:
        print(assertion_error)


if __name__ == "__main__":
    run()
