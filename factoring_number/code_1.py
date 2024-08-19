def find_all_factors(num: int) -> list[int]:
    if num < 1:
        return []
    list_1: list[int] = []
    for divisor in range(1, num + 1):
        quotient = num // divisor
        rest = num % divisor
        print(f"{num} / {divisor} = {quotient} : {rest}")
        if quotient < divisor:
            break
        if rest == 0:
            list_1.append(divisor)
            list_1.append(quotient)
    # list_1 = list(set_1)
    list_1.sort()
    return list_1


def find_all_factors_set(num: int) -> list[int]:
    if num < 1:
        return []
    set_1: set[int] = set()
    for divisor in range(1, num + 1):
        quotient = num // divisor
        rest = num % divisor
        print(f"{num} / {divisor} = {quotient} : {rest}")
        if quotient < divisor:
            break
        if rest == 0:
            set_1.add(divisor)
            set_1.add(quotient)
    list_1 = list(set_1)
    list_1.sort()
    return list_1


# take user input
num = int(72)
# num = int(input("number: "))

# call the function
print(find_all_factors(num))
