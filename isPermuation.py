def isPermutation(str1, str2):
    # Check if the lengths of the strings are different
    if len(str1) != len(str2):
        return False
    
    # Sort the strings and compare
    return sorted(str1) == sorted(str2)

def main():
    str1 = input("Enter the first word: ")
    str2 = input("Enter the second word: ")

    if isPermutation(str1, str2):
        print("These words are permutations of each other")
    else:
        print("These words are not permutations of each other")
    
if __name__ == "__main__":
    main()