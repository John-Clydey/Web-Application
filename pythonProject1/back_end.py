def decToBin(number):
    reversed_list = []
    binary_list = []
    binary_number = 0.0

    def convertDecToBin(local_current_val):
        while local_current_val > 0:
            next_val = int(local_current_val / 2)
            remainder = str(local_current_val % 2)
            reversed_list.append(remainder)
            local_current_val = next_val

        items = len(reversed_list)
        for i in range(items):
            binary_list.append(reversed_list[items - i - 1])
        local_binary_number = "".join(binary_list)
        return local_binary_number

    if number == 0:
        binary_number = 0
        return binary_number
    elif number < 0:
        number = -1 * number
        binary_number = convertDecToBin(number)
        return f"-{binary_number}"
    else:
        binary_number = convertDecToBin(number)
        return binary_number


def binary_to_decimal(binary_string):
    decimal_value = int(binary_string, 2)
    return decimal_value
