
def credit_card_validator(num):
    # Define card issuer prefixes and lengths
    VISA_PREFIX = ["4"]
    MASTERCARD_PREFIXES = [str(i) for i in range(51, 56)] + [str(i) for i in range(2221, 2721)]
    AMEX_PREFIXES = ["34", "37"]
    
    VISA_LENGTH = 16
    MASTERCARD_LENGTH = 16
    AMEX_LENGTH = 15
    
    # Function to check if a number starts with a valid prefix
    def has_valid_prefix(num, prefixes):
        return any(num.startswith(prefix) for prefix in prefixes)
    
    # Check card type and length
    if has_valid_prefix(num, VISA_PREFIX) and len(num) == VISA_LENGTH:
        pass
    elif has_valid_prefix(num, MASTERCARD_PREFIXES) and len(num) == MASTERCARD_LENGTH:
        pass
    elif has_valid_prefix(num, AMEX_PREFIXES) and len(num) == AMEX_LENGTH:
        pass
    else:
        return False
    
    # Luhn algorithm to validate checksum
    def luhn_check(card_number):
        digits = [int(d) for d in card_number]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        return sum(digits) % 10 == 0
    
    return luhn_check(num)

