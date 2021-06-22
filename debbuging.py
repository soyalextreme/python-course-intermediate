class NegativeNumberNotValid(Exception):
    pass

def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    detected_errors = True
    while detected_errors != False:
        try:
            num = int(input("Enter an entire number: "))
            if num < 0:
                raise NegativeNumberNotValid(
                    "We do not accept negative numbers")
            print(divisors(num))
            detected_errors = False
        except ValueError:
            print("Please enter a number")
        except NegativeNumberNotValid as err_negative:
            print(err_negative)
        finally:
            if detected_errors:
                print('Try again')
            else:
                break



if __name__ == "__main__":
    run()
