#! -*- coding:utf-8 -*-

def test_dict_value():
    d = {"ACME":45.23,
        "AAPL":612.78,
        "IBM":205.55,
        "HPQ":37.20,
        "FB":10.75}

    print("max")
    print(max(zip(d.values(), d.keys())))
    print("min")
    print(min(zip(d.values(), d.keys())))


if __name__ == "__main__":
    test_dict_value()
