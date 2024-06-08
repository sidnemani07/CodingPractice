def isSubstring(s1,s2):
    return s1 in s2

def isRotation(s1, s2):
    if len(s1) != len(s2) or len(s1) == 0:
        return False
    return isSubstring(s1, s2+s2)

def main():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    print(isRotation(s1,s2))

if __name__ == "__main__":
    main()