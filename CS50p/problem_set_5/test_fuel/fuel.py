def main():
    percentage = convert(fraction)
    print(gauge(percentage))
def convert(fraction):
    x,y = (fraction).split("/")
    if int(x)/int(y) <= 1:
        fuel = round((int(x) /int(y)) * 100)
        return fuel
def gauge(percentage):
     if percentage >= 99:
        return "F"
     elif percentage <= 1:
        return "E"
     else:
        return(f"{percentage}%")

if __name__ == "__main__":
    main()
