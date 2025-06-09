import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to handle command line division operations.
    
    This script takes two command line arguments (numerator and denominator)
    and uses the safe_divide function to perform robust division with
    proper error handling.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        print("Example: python main.py 10 5")
        print("Example: python main.py 15.5 2.5")
        sys.exit(1)
    
    # Get the command line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    
    # Perform safe division and display result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()