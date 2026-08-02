from datetime import date

from utils import add, divide, multiply, subtract


def main():
    print("Name: Nurullah Mia")
    print(f"Today's date: {date.today()}")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 × 5 = {multiply(10, 5)}")

    try:
        print(f"10 ÷ 2 = {divide(10, 2)}")
        print(f"10 ÷ 0 = {divide(10, 0)}")
    except ValueError as error:
        print(f"Calculator error: {error}")


if __name__ == "__main__":
    main()
