while True:
    s = input("Enter something:")
    if s == "quit":
        print("ByeBye")
        break
    else:
        print("The Length of {}".format(s),len(s))

    print("Done")