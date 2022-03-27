from base_converter import manual_convert_to_base_n as convert_base


def bitwise_and(num1, num2):
    result = ''
    for i in range(len(num1)):
        result += '1' if num1[i] == '1' and num2[i] == '1' else '0'
    return result


def bitwise_or(num1, num2):
    result = ''
    for i in range(len(num1)):
        result += '1' if num1[i] == '1' or num2[i] == '1' else '0'
    return result


def bitwise_xor(num1, num2):
    result = ''
    for i in range(len(num1)):
        if (num1[i] == '1' and num2[i] == '0') or \
           (num1[i] == '0' and num2[i] == '1'):
            result += '1'
        else:
            result += '0'
    return result


def main():
    valid_ops = ["and", "or", "xor"]

    num1 = input("Enter first number : ")
    num2 = input("Enter second number: ")
    
    op = input("Enter operator: ")
    
    if op not in valid_ops:
        print("Invalid operator. Please try again.")
        main()
    if len(num1) != len(num2):
        print("Numbers have differing lengths. Please try again.")
        main()
    
    else:
        if op == "and":
            result = bitwise_and(num1, num2)
        elif op == "or":
            result = bitwise_or(num1, num2)
        elif op == "xor":
            result = bitwise_xor(num1, num2)

    print()
    print(f"Result (bin): {result}")
    print(f"Result (hex): {convert_base(result, 2, 16)}")


if __name__ == '__main__':
    while True:
        print()
        main()