

def check(str_number):
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
    if len(str_number) == 1:
        return f"{str_number}{check(str_number)}"
    elif number >= 11 and number <= 19:
        return f"{str_number}th"
    else:
        return f"{str_number}{check(str_number[-1])}"


def main():
    value = input("number: ")
    try:
        value = abs(int(value))
    except ValueError:
        try:
            value = abs(round(float(value)))
        except ValueError:
            print("Invalid Input")
            return 0
    if value == 0:
        print(value)
        return 0
    print(numberToOrdinal(value))

if __name__ == "__main__":
    main()