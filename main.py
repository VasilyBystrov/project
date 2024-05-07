import json
from utils import sorted_, prepare_msg


def main():
    with open("operations", "r", encoding="utf-8") as file:
        data = json.load(file)

    items = sorted_(data)

    for i in range(5):
        print(prepare_msg(items[i]))
        print()


main()

