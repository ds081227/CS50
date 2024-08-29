def main():
    Greeting = G(input("Greeting: ").split()[0].strip().lower())

def G(response):
    if "hello" in response:
        print("$0")
    elif response.startswith("h"):
        print("$20")
    else:
        print("$100")



main()
