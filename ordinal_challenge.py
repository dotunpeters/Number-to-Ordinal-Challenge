

def check(str_number):
    #return corresponding ordinal prefix
    if str_number == "1":
        return "st"
    elif str_number == "2":
        return "nd"
    elif str_number == "3":
        return "rd"
    else:
        return "th"


def numberToOrdinal(number):
    str_number = str(number)
    teen = int(f"{str_number[-2]}{str_number[-1]}")

    #handling valid input types
    if len(str_number) == 1:
        return f"{str_number}{check(str_number)}"
    elif teen >= 11 and teen <= 19:
        return f"{str_number}th"
    else:
        return f"{str_number}{check(str_number[-1])}"


def main():
    value = input("number: ")

    #handling none integers and 0 input 
    try:
        value = abs(int(value))
    except ValueError:
        try:
            value = abs(round(float(value)))
        except ValueError:
            print("Invalid Input")
            main()
    if value == 0:
        print(value)
        return 0
    print(numberToOrdinal(value))

if __name__ == "__main__":
    main()