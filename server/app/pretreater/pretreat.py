import datetime
import os
from _datetime import timedelta

import numpy as np


def read(file):
    f = open(file, "r", encoding="utf-8")
    content = f.read()
    lines = content.split("\n")
    f.close()
    try:
        while lines[len(lines) - 1].isspace() or lines[len(lines) - 1] == "":
            lines.pop(len(lines) - 1)
    except:
        print(file)
    return lines


def write(file, lines):
    f = open(file, "w", encoding="utf-8")
    for line in lines:
        f.write(line + "\n")
    f.close()
    return


def norm(datalist):  # 计算数据的均值和标准差
    x = np.array(datalist)
    mu = np.mean(x)
    sigma = np.std(x)
    list = []
    list.append(mu)
    list.append(sigma)
    return list


def pretreat(resoucedir, targetdir, begin_time, end_time):
    files = os.listdir(resoucedir)
    resfrom = ""
    if "bilibilidate" in resoucedir:
        resfrom = "bilibili_"
    if "weibo" in resoucedir:
        resfrom = "weibo_"
    if "south" in resoucedir:
        resfrom = "south_"
    list = []
    begin = begin_time
    while begin <= end_time:
        realpath = resoucedir + resfrom + str(begin) + ".csv"
        lines = read(realpath)
        list.append(len(lines))
        begin += timedelta(days=1)
        pass
    mu_and_sig = norm(list)
    begin = begin_time
    if resfrom == "south_":
        mu_and_sig[0] = 0
    while begin <= end_time:
        realpath = resoucedir + resfrom + str(begin) + ".csv"
        lines = read(realpath)
        if len(lines) > mu_and_sig[0] - 0.5 * mu_and_sig[1] and len(lines) > 1:
            write(targetdir + resfrom + str(begin) + ".csv", lines)
            pass
        begin += timedelta(days=1)
        pass
    pass


if __name__ == "__main__":
    # weibo
    pretreat("../scraper/store/weibo/", "./store/weibo/",
             datetime.date(2019, 12, 31), datetime.date(2020, 1, 19))
    pretreat("../scraper/store/weibo/", "./store/weibo/",
             datetime.date(2020, 1, 20), datetime.date(2020, 2, 20))
    pretreat("../scraper/store/weibo/", "./store/weibo/",
             datetime.date(2020, 2, 21), datetime.date(2020, 3, 17))
    pretreat("../scraper/store/weibo/", "./store/weibo/",
             datetime.date(2020, 3, 18), datetime.date(2020, 4, 28))
    pretreat("../scraper/store/weibo/", "./store/weibo/",
             datetime.date(2020, 4, 29), datetime.date(2020, 6, 1))
    # bilibili
    # pretreat("../scraper/store/bilibili/", "./store/bilibili/",
    #          datetime.date(2019, 12, 31), datetime.date(2020, 1, 19))
    pretreat("../scraper/store/bilibili/", "./store/bilibili/",
             datetime.date(2020, 1, 23), datetime.date(2020, 2, 20))
    pretreat("../scraper/store/bilibili/", "./store/bilibili/",
             datetime.date(2020, 2, 21), datetime.date(2020, 3, 17))
    pretreat("../scraper/store/bilibili/", "./store/bilibili/",
             datetime.date(2020, 3, 18), datetime.date(2020, 4, 28))
    pretreat("../scraper/store/bilibili/", "./store/bilibili/",
             datetime.date(2020, 4, 29), datetime.date(2020, 6, 1))
    # south
    pretreat("../scraper/store/south/", "./store/south/",
             datetime.date(2019, 12, 31), datetime.date(2020, 6, 1))
