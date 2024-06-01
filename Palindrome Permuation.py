def is_permutation_of_palindrome(input_str):
    # Normalize the string
    input_str = ''.join(char.lower() for char in input_str if char.isalpha())

    # Count characters
    char_count = {}
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Check for palindrome permutation
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False

    return True

def main():
    input_string = input("Enter a phrase: ")
    print(is_permutation_of_palindrome(input_string))

if __name__ == "__main__":
    main()
