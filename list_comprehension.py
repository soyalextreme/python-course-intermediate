def num_nat_square_not_divisible_3(amount):
    """
        Function that prints the list containing square for the natural numbers, divisible 
        for 3.
        @params:
            amount -> integer number 
    """
    results = [ n ** 2 for n in range(1, amount + 1) if n%3 != 0]
    print("results: ", results)


def challenge_list_filter(amount):
    """
        Chanllenge function prints the natural numbers that are divisible between 4, 6 and 9.
        @params:
            amount -> integer number 
    """
    if amount < 36:
        print("Ups, empty list the min amount is 36")
    else:
        results = [n for n in range(1, amount + 1) if n%4 == 0 and n%9 == 0 and n%6 == 0 ]
        print("results: ", results)


if __name__ == "__main__":
    """ 
        Main Entry
    """
    # amount = int(input("Amount of natural numbers to squared: "))
    # num_nat_square_not_divisible_3(amount)
    amount = int(input("Amount of natural numbers divisible between 4, 9 and 6: "))
    challenge_list_filter(amount)
