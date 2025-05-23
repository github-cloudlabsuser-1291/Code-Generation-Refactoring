# Refactored: Improved clarity, error handling, and user experience

MAX_ELEMENTS = 100

def calculate_sum(numbers):
    return sum(numbers)

def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Sum Elements Program")
    while True:
        n = get_integer(f"Enter the number of elements (1-{MAX_ELEMENTS}): ")
        if 1 <= n <= MAX_ELEMENTS:
            break
        print(f"Invalid input. Please provide a number from 1 to {MAX_ELEMENTS}.")

    numbers = []
    print(f"Enter {n} integers:")
    for i in range(n):
        num = get_integer(f"Element {i+1}: ")
        numbers.append(num)

    total = calculate_sum(numbers)
    print("Sum of the numbers:", total)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
