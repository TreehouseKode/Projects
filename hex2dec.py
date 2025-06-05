import sys

def hex_to_decimal(hex_value):
    # Remove '0x' prefix if present
    if hex_value.startswith('0x'):
        hex_value = hex_value[2:]

    try:
        return int(hex_value, 16)
    except ValueError:
        print(f"Error: '{hex_value}' is not a valid hexadecimal value.")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <hex_value1> <hex_value2> ...")
        sys.exit(1)

    hex_values = sys.argv[1:]
    for hex_value in hex_values:
        decimal_value = hex_to_decimal(hex_value)
        if decimal_value is not None:
            print(f"Hexadecimal '{hex_value}' is Decimal '{decimal_value}'")

if __name__ == "__main__":
    main()
