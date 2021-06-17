def main():
    """
        Working with the list and dictionary on the same structure
    """ 
    my_list = [1, "Hello", True, 4.5]
    my_dic = {"firstname": "Alejandro", "lastname": "Andrade"}

    super_list = [
              {"firstname": "Alejandro", "lastname": "Andrade"},
              {"firstname": "Miguel", "lastname": "Martinez"},
              {"firstname": "Tomas", "lastname": "Hernandez"}
            ]

    super_dict = {
                "natural_nums": [1, 2, 3, 4, 5],
                "integer_nums": [-1, -2, 0, 1, 2],
                "floating_nums": [1.1, 4.5, 6.43]
            }

    print("PRINTING THE SUPER DICTIONARY")
    for key, value in super_dict.items():
        print(key, "-", value)

    print("PRINTING THE SUPER DICTIONARY")
    for i in super_list:
        for key, value in i.items():
            print(key, "-", value, end=" | ")
        print("\n")


if __name__ == "__main__":
    """ Main Entry """
    main()
