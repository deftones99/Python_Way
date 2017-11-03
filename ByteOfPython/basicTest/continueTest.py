while True:
    s = input("Enter a word:")

    if s == "quit":
        print("ByeBye")
        break
    if len(s) < 3:
        print("Too Small")
        continue
    print("input is good")
