# Hexorcist.py

def to_decimal(number_string, original_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_string = number_string.upper()
    decimal_value = 0
    power = 0

    for char in reversed(number_string):
        if char not in digits:
            raise ValueError(f"Invalid character '{char}'.")
        digit_value = digits.index(char)
        if digit_value >= original_base:
            raise ValueError(f"'{char}' not valid in base {original_base}.")
        decimal_value += digit_value * (original_base ** power)
        power += 1
    
    return decimal_value


def from_decimal(decimal_number, target_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if decimal_number == 0:
        return "0"
    result = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        result = digits[remainder] + result
        decimal_number //= target_base
    return result

if __name__ == "__main__":
    print("Welcome to the Hexorcist the converter powered by agony and despair")

    num_str = input("Enter your number (e.g., 'C7'): ").strip().upper()
    orig_base = int(input("Enter the original base (2-36): "))
    target_base = int(input("Enter the target base (2-36): "))

    if not (2 <= orig_base <= 36 and 2 <= target_base <= 36):
        print("Bases must be between 2 and 36. Please follow directions next time.")
        exit(1)

    try:
        decimal_num = to_decimal(num_str, orig_base)
        converted_num = from_decimal(decimal_num, target_base)
        print(f"\n{num_str} (base {orig_base}) = {converted_num} (base {target_base})")
    except ValueError as e:
        print("Error:", e)
