def URLify(s):
    s = s.strip()
    return s.replace(" ", "%20")

def main():
    s = input("Enter a word: ")
    print(URLify(s))

if __name__ == "__main__":
    main()