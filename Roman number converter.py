def roman_to_int(roman_numeral):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    prev_value = 0
    
    for numeral in reversed(roman_numeral):
        value = roman_numerals[numeral]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    
    return result

def int_to_roman(number):
    if not 0 < number < 4000:
        raise ValueError("Number out of range (1-3999)")
    
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }
    
    result = ""
    
    for value in sorted(roman_numerals.keys(), reverse=True):
        while number >= value:
            result += roman_numerals[value]
            number -= value
    
    return result

# Test the functions
while True:
    choice = input("Enter '1' to convert Roman numeral to integer, '2' to convert integer to Roman numeral, or 'q' to quit: ")
    
    if choice == '1':
        roman_numeral = input("Enter a Roman numeral: ")
        integer_value = roman_to_int(roman_numeral)
        print(f"The integer value of {roman_numeral} is {integer_value}")
    elif choice == '2':
        try:
            number = int(input("Enter an integer between 1 and 3999: "))
            roman_numeral = int_to_roman(number)
            print(f"The Roman numeral representation of {number} is {roman_numeral}")
        except ValueError as e:
            print(e)
    elif choice.lower() == 'q':
        break
    else:
        print("Invalid choice. Please enter '1', '2', or 'q'.")
