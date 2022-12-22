# 生成 csv
import random
import csv
from uuid import uuid4

#######################################
# 生成数据条数
DATA_COUNT = 10
# 生成文件名
CSV_FILENAME = "data_0001.csv"
#######################################

# 名称,分类，年龄,语言,平台
gamelist = [
    ["王者荣耀", "MOBA", "9", "汉语", "iOS"],
    ["实况足球22", "体育", "9", "日语", "Steam"],
    ["塞尔达传说", "动作", "全年龄", "日语", "Switch"],
    ["超级马里奥", "动作", "全年龄", "日语", "Switch"],
    ["街头霸王V", "对战", "17", "英语", "PS5"],
    ["三国志14", "策略", "9", "日语", "Steam"],
    ["GTA5", "暴力", "18", "英语", "Steam"],
    ["文明6", "策略", "4", "汉语", "Steam"],
    ["精灵宝可梦", "对战", "4", "日语", "Switch"],
]
# 卖家
sellers = ["亚马逊", "雅虎", "乐天"]


def mkpasswd(length):
    result = ""
    for index in range(length):
        result += random.choice(list("QWERTYUIOPASDFGHJKLZXCVBNM_1234567890"))
    return result


def makecsv():
    datalist = []
    with open(CSV_FILENAME, "w") as file:
        writer = csv.DictWriter(
            file,
            [
                "row_num",  # 行号
                "seller",   # 卖家
                "title",    # 作品名
                "category", # 分类
                "age",      # 年龄
                "lang",     # 语言
                "platform", # 平台
                "quantity", # 销量
                "pwd",      # 密码等须保密数据
            ],
        )
        writer.writeheader()

        for row_num in range(1, DATA_COUNT + 1):
            transaction = gamelist[random.randint(0, len(gamelist) - 1)]
            record = {
                # "id": str(uuid4()),
                "row_num": row_num,
                "seller": sellers[random.randint(0, len(sellers) - 1)],
                "title": transaction[0],
                "category": transaction[1],
                "age": transaction[2],
                "lang": transaction[3],
                "platform": transaction[4],
                "quantity": str(random.randint(1, 100)),
                "pwd": mkpasswd(16),
            }
            print(record)
            writer.writerow(record)
    pass


def main():
    makecsv()
    pass


if __name__ == "__main__":
    main()