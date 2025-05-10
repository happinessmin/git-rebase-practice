print("欢迎来到点菜小程序！")
print("菜单如下：")
print("1. 宫保鸡丁")
print("2. 鱼香肉丝")
print("3. 麻婆豆腐")
print("4. 青椒肉丝")

choices = input("请输入你想点的菜编号，用空格分隔（例如：1 3 4）：")

# 菜单映射
menu = {
    "1": "宫保鸡丁",
    "2": "鱼香肉丝",
    "3": "麻婆豆腐",
    "4": "青椒肉丝"
}

# 处理选择
selected = choices.split()
print("\n你点的菜有：")
found = False
for c in selected:
    if c in menu:
        print(f"- {menu[c]}")
        found = True
    else:
        print(f"- 编号 {c} 无效")
        found = True

if not found:
    print("你没有点任何有效的菜。")
