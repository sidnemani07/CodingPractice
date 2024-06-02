def compression(s):
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    compressed = ''.join(compressed)
    if len(compressed) < len(s):
        return compressed
    else:
        return s

def main():
    s = input("Enter a phrase: ")
    print(compression(s))

if __name__ == "__main__":
    main()