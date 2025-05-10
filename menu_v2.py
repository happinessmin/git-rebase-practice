#!/usr/bin/env python3
# menu_v2.py

"""
一个简单的点菜程序，支持多菜选择。
"""


def show_menu():
    print("欢迎来到点菜小程序！")
    print("菜单如下：")
    for key, value in MENU.items():
        print(f"{key}. {value}")


def get_choices():
    return input("请输入你想点的菜编号，用空格分隔（例如：1 3 4）：")


def parse_choices(choices_str):
    choices = choices_str.strip().split()
    selected_dishes = []
    invalid_choices = []

    for choice in choices:
        if choice in MENU:
            selected_dishes.append(MENU[choice])
        else:
            invalid_choices.append(choice)

    return selected_dishes, invalid_choices


def print_result(selected, invalid):
    if selected:
        print("\n你点的菜有：")
        for dish in selected:
            print(f"- {dish}")
    if invalid:
        print("\n以下编号无效：")
        for code in invalid:
            print(f"- {code}")
    if not selected and not invalid:
        print("你没有点任何菜。")


MENU = {
    "1": "宫保鸡丁",
    "2": "鱼香肉丝",
    "3": "麻婆豆腐",
    "4": "青椒肉丝"
}


def main():
    show_menu()
    user_input = get_choices()
    selected, invalid = parse_choices(user_input)
    print_result(selected, invalid)


if __name__ == "__main__":
    main()
