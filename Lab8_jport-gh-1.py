"""
Program Name: Lab8_jport-gh-1.py
Author: Janet Portillo
Purpose: Validate a 12-digit UPC-A code by calculating the correct check digit
         and comparing it to the user-provided check digit.
Starter Code: No external starter code used.
Date: 06/21/2026
"""

# Function to calculate UPC check digit 

def find_UPC(first11):
   
    #Calculates the correct UPC-A check digit based on the first 11 digits. Returns the expected check digit as an integer.
   
    # Step 1: Sum of digits in odd positions (0,2,4,...)
    odd_sum = 0
    for i in range(0, 11, 2):
        odd_sum += int(first11[i])

    # Step 2: Multiply odd sum by 3
    odd_sum *= 3

    # Step 3: Sum of digits in even positions (1,3,5,...)
    even_sum = 0
    for i in range(1, 11, 2):
        even_sum += int(first11[i])

    # Step 4: Total sum
    total = odd_sum + even_sum

    # Step 5: Calculate check digit
    check_digit = (10 - (total % 10)) % 10
    return check_digit


# MAIN PROGRAM

while True:
    upc = input("Enter a 12-digit UPC: ")

    # Optional challenge: input validation
    if len(upc) != 12 or not upc.isdigit():
        print("Error: UPC must be exactly 12 digits and contain only numbers.\n")
        continue

    first11 = upc[:11]
    provided_check = upc[11]

    print(f"\nThe first 11 digits are '{first11}'.")
    print(f"The provided check digit is '{provided_check}'.\n")

    print("Calculating...")
    expected_check = find_UPC(first11)

    print(f"The expected check digit is {expected_check}.\n")

    if str(expected_check) == provided_check:
        print("This is a VALID UPC.\n")
    else:
        print("This is an INVALID UPC.\n")

    break
