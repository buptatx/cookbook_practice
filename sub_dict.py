#！ -*- coding:utf-8 -*-

def create_sub_dict(data):
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    sub_dict_1 = {key:value for key,value in data.items() if key in tech_names}
    print(sub_dict_1)

    sub_dict_2 = {key:value for key,value in data.items() if value > 200}
    print(sub_dict_2)


if __name__ == "__main__":
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    create_sub_dict(prices)