def check(saying):
    if saying.startswith("hello"):
        print("$0")
    elif saying.startswith("h"):
        print("$20")
    else:
        print("$100")



def main():
    user_saying = input("What would you like to say?: ").lower().strip()
    check(user_saying)


main()