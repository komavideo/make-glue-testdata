# 生成 csv
import random
import csv
from uuid import uuid4

#######################################
# 生成数据条数
DATA_COUNT = 20
# 生成文件名
CSV_FILENAME = "data_0001.csv"
#######################################

# 名称,分类，年龄,语言,平台
gamelist = [
    ["WangZhe", "MOBA", "9", "CN", "iOS"],
    ["WE22", "Sports", "9", "JP", "Steam"],
    ["Zelda", "Action", "All", "JP", "Switch"],
    ["SuperMario", "Action", "All", "JP", "Switch"],
    ["SF6", "VS", "17", "EN", "PS5"],
    ["Sangokushi14", "SIM", "9", "JP", "Steam"],
    ["GTA5", "Violence", "18", "EN", "Steam"],
    ["CIV6", "SIM", "4", "CN", "Steam"],
    ["Pokemon", "VS", "4", "JP", "Switch"],
]
# 卖家
sellers = ["Amazon", "Yahoo", "Rakuten"]


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
