def check_status(value):
    if value >= 50:
        return "High"
    return "Normal"


def main():
    number = 75
    result = check_status(number)

    print("DevSecOps Demo Application")
    print("Input value:", number)
    print("Status:", result)


if __name__ == "__main__":
    main()
