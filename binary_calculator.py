
def get_second_compliment(num1):
    first_compliment = get_first_compliment(num1)
    num2 = "1"
    max_length = max(len(first_compliment), len(num2))
    num2 = num2.zfill(max_length)
    result = ''
    carry = 0
    for i in range(max_length - 1, -1, -1):
        # Calculate sum and carry for the current bit
        bit_sum = int(first_compliment[i]) + int(num2[i]) + carry
        # Append the current bit of the sum to the result
        result = str(bit_sum % 2) + result
        # Update carry for the next iteration
        carry = bit_sum // 2
        if carry == 1:
            result = '1' + result
    return result

def get_first_compliment(num1):
    first_compliment = ""
    for bit in num1:
        # Flip
        if bit == "0":
            first_compliment += "1"
        else:
            first_compliment += "0"
    return first_compliment


# Menu 1
while True:
    print("**binary calculator**")
    print("A)Insert new numbers")
    print("B)Exit")
    chosen_letter = input("choose A or B")
    if chosen_letter == "A":

        # check if the number is binary
        while True:
            num1 = input("Please insert a binary number")
            if all(bit in '01' for bit in num1):
                break
            else:
                print("Please enter a valid number")
            # Menu 2
        print("**Please select the operation**")
        print("A)compute one's complement")
        print("B)compute two's complement")
        print("C)addition")
        print("D)subtracion")
        chosen_letter2 = input("choose A or B or C or D ")
        if chosen_letter2 == "A":
            first_compliment = get_first_compliment(num1)
            print("The one's compliment = ", first_compliment)



        elif chosen_letter2 == "B":
            second_compliment = get_second_compliment(num1)
            print("The two's compliment= ", second_compliment)

        elif chosen_letter2 == "C":
            while True:
                num2 = input('Please insert the second number')
                if all(bit in '01' for bit in num2):
                    break
                else:
                    print("please enter a valid number")
            # Ensure both binary strings have same length
            max_length = max(len(num1), len(num2))
            # to make them equal in length
            num1 = num1.zfill(max_length)
            num2 = num2.zfill(max_length)
            # Initialization variables to store the and carry
            result = ''
            carry = 0
            # to iterate binary strings from right to lift
            for i in range(max_length - 1, -1, -1):
                add = int(num1[i]) + int(num2[i]) + carry

                # calculate sum and carry for the current bit
                result = str(add % 2) + result
                carry = add // 2

                # Check if there is a final carry after all additions
            if carry == 1:
                    result = '1' + result
            print("The addition= ", result)
        elif chosen_letter2 == "D":
            while True:
                num2 = input('Please insert the second number')
                if all(bit in '01' for bit in num2):
                    break
                else:
                    print("please enter a valid number")


            def binary_subtraction(num1, num2):
                # Ensure the two binary numbers have the same length
                max_len = max(len(num1), len(num2))
                num1 = num1.zfill(max_len)
                num2 = num2.zfill(max_len)

                result = " "
                borrow = 0

                # Iterate through the digits starting from righ
                for i in range(max_len - 1, -1, -1):
                    bit_diff = int(num1[i]) - int(num2[i]) - borrow
                    if bit_diff < 0:
                        bit_diff += 2
                        borrow = 1
                    else:
                        borrow = 0
                    result = str(bit_diff) + result
                return result.strip('0') or '0'


            difference_binary = binary_subtraction(num1, num2)
            print("The subtraction= " , difference_binary)
    elif chosen_letter == "B":
        exit()
    else:
        print("plaese select a valid choice")