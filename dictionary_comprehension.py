import math 

def challenge_key_values(amount):
    """
        Prints the numbers pow of 3 as value and as key the value in a dictionary.
        @params 
            amount -> Integer
    """
    result = {n: n**3 for n in range(1, amount + 1) if n%3 != 0}
    print(result)

def challenge_sqrt_values(amount):
    """
        Print the dictionary with the value of the number as key and as the value
        the square root for the key.
        
        @params 
            amount -> Integer
    """
    result = { n: math.sqrt(n) for n in range(1, amount + 1) }
    print(result)

if __name__ == "__main__":
    """
        Main Entry
    """
    amount = int(input("Amount of numbers for the dictionary:" ))
    # challenge_key_values(amount)
    challenge_sqrt_values(amount)
