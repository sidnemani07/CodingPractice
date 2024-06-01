def isUnique(s):
    seen = []
    for letter in s:
        if letter in seen:
            return False
        seen.append(letter)
    return True

def main():
    s = input("Enter a word: ")

    if isUnique(s):
        print("All the characters are unique")
    else:
        print("There are repeat characters")

if __name__ == "__main__":
    main()