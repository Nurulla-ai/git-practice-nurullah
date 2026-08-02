from datetime import date

from utils import add, subtract


def main():
    print("Name: Nurullah Mia")
    print(f"Today's date: {date.today()}")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")


if __name__ == "__main__":
    main()
