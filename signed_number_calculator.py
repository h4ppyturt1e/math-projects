from base_converter import manual_convert_to_base_n as convert_base
from base_converter import num_to_dec as to_dec


def binary_addition():
    num1 = input("Enter first binary number: ")
    num2 = input("Enter second binary number: ")
    bits = len(num1)
    largest_bit = 2 ** (bits-1)

    try:
        nums_bool = [num[0] == '1' for num in [num1, num2]]
        num1 = to_dec(num1[1:], 2) - largest_bit if nums_bool[0] else to_dec(num1[1:], 2)
        num2 = to_dec(num2[1:], 2) - largest_bit if nums_bool[1] else to_dec(num2[1:], 2)

    except IndexError:
        print("Invalid input, try again.\n")
        binary_addition()
    
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")

    if int(total) >= largest_bit:
        print(total, "is greater than", largest_bit, ", Incorrect sum.")
        possible_total = total - largest_bit
        possible_answer = get_final_binary(possible_total, bits)
        print(f"Possible answer: {possible_answer}")

    else:
        answer = get_final_binary(total, bits)
        print("Answer:", answer)


def get_final_binary(total, bits):
    converted_total = convert_base(str(abs(total)), 10, 2)
    
    while len(converted_total) != bits:
        converted_total = "0" + converted_total
        
    if converted_total[0] == "1":
        normalized_total = []
        for i in range(bits):
            if converted_total[i] == "1":
                normalized_total.append("0")
            else:
                normalized_total.append("1")

        final_total = convert_base(str(to_dec(''.join(normalized_total), 2) + 1), 10, 2)

    else:
        final_total = converted_total

    return final_total



if __name__ == "__main__":
    print()
    while True:
        binary_addition()
