num_to_letter = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K',
                 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V',
                 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}
letter_to_num = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20,
                 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31,
                 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}

# print("Base converter by h4ppyturt1e\n")

def convert_to_base_n():
    """
    Converts num in cur_base to base_n
    Precondition: 0 < n <= 36
    """
    keep_going = True
    try:
        while keep_going:
            num = input('Input number:')
            num = num.upper()
            cur_base = int(input('Input base:'))
            base_n = int(input('Output:'))
            still_divisible = True
            lodigits = []
            num_in_base_n = ''
            dec = num_to_dec(num, cur_base)
            while still_divisible:
                digit = dec % base_n
                if digit in num_to_letter:
                    lodigits.append(num_to_letter[digit])
                else:
                    lodigits.append(digit)
                dec = dec // base_n
                if dec == 0:
                    still_divisible = False
                print(dec, "R", digit)
            for i in range(len(lodigits) - 1, -1, -1):
                digit = str(lodigits[i])
                num_in_base_n += digit
            print("Your number in base", base_n, "is", num_in_base_n)

            print('\n')
    except ValueError:
        print("Invalid response, try again.")
        print("\n")
        convert_to_base_n()


def num_to_dec(num: str, cur_base: int) -> int:
    """ 
    Converts num in cur_base to decimal(base 10)
    Precondition: 0 < cur_base < (every digit in num)
    """
    num_length = len(num)
    total = 0
    power = 0
    for i in range(num_length - 1, -1, -1):
        letter = num[i]
        if letter.isdigit() and letter != '10':
            digit = int(letter)
        else:
            digit = letter_to_num[num[i]]
        value = digit * cur_base ** power
        total += value
        power += 1
    return total


def manual_convert_to_base_n(num: str, cur_base: int, base_n: int):
    """ 
    Converts num in cur_base to base_n
    Precondition: 0 < n <= 36
    """
    num = num.upper()
    still_divisible = True
    lodigits = []
    num_in_base_n = ''
    dec = num_to_dec(num, cur_base)
    while still_divisible:
        digit = dec % base_n
        if digit in num_to_letter:
            lodigits.append(num_to_letter[digit])
        else:
            lodigits.append(digit)
        dec = dec // base_n
        if dec == 0:
            still_divisible = False
    for i in range(len(lodigits) - 1, -1, -1):
        digit = str(lodigits[i])
        num_in_base_n += digit
    # print(num, "in base", base_n, "is", num_in_base_n)
    return num_in_base_n


if __name__ == '__main__':
    print()
    convert_to_base_n()
