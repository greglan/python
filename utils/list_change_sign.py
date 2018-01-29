def sign_change(var):
    """
    Given a list of signed numbers, this function indicates whether the sign of numbers change
    :type var: list
    :param var: a list of numbers
    :return:
    """
    n_changes = 0
    for x in range(0, len(var) - 1):
        if var[x] == 0:
            print("Item " + str(x) + " is zero")
            current = 1
            second = 1
        elif var[x + 1] == 0:
            print("Item " + str(x + 1) + "is zero")
            print("Testing a sign change between item " + str(x) + " and item " + str(x + 2))
            if abs(var[x]) == var[x]:
                current = 1
            else:
                current = -1
            if abs(var[x + 2]) == var[x + 2]:
                second = 1
            else:
                second = -1
        else:
            if abs(var[x]) == var[x]:
                current = 1
            else:
                current = -1
            if abs(var[x + 1]) == var[x + 1]:
                second = 1
            else:
                second = -1
        if current * second < 0:
            print("Sign change: item " + str(x + 1) + " and item " + str(x + 2))
            n_changes = n_changes + 1
    print(str(n_changes) + " sign changes detected")
