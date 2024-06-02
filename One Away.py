def isChanged(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    #s1, s2 = s2, s1
    i = j = diff = 0

    while i < len(s2) and j <len(s1):
        if s1[i] != s2[j]:
            if diff == 1:
                return False
            diff += 1
            if len(s2) != len(s1):
                j +=1
                continue
        i += 1
        j += 1
    return True

def main():
    s1 = input("Enter the original: ")
    s2 = input("Enter the changed version: ")

    print(isChanged(s1, s2))

if __name__ == "__main__":
    main()
    

