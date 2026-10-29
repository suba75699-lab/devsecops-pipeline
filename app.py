
def check_status(value):
    if value <= 50:
        return "Normal"
    return "High"


if __name__ == "__main__":
    print(check_status(25))
    print(check_status(75))
