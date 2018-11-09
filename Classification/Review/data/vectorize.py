import os, glob, json
import numpy as np
root_dir = ""
dic_file = root_dir + "review-dic.json"
data_file = root_dir + "review-data.json"

word_dic = {"_MAX": 0}
X = []
Y = []

global max_words
import time

def main():
    global X
    global Y
    global word_dic
    global max_words

    start_time = time.time()

    if os.path.exists(dic_file):
        word_dic = json.loads(open(dic_file))
    else:
        register_dic()
        json.dump(word_dic, open(dic_file, "w"))
    max_words = word_dic["_MAX"]

    count_freq()
    json.dump({"X": X, "Y": Y}, open(data_file, "w"))
    print(time.time() - start_time)


def text_to_ids(text):
    global word_dic
    text = text.strip()
    text = text.replace('\n', '/')
    words = text.split("/")
    result = []
    for n in words:
        n = n.strip()
        if n == "" : continue
        if not n in word_dic:
            # if word_dic["_MAX"] > cnt_max:continue
            wid = word_dic[n] = word_dic["_MAX"]
            word_dic["_MAX"] += 1
        else:
            wid = word_dic[n]
        result.append(wid)
    print(word_dic["_MAX"])
    return result


def file_to_ids(fname):
    with open(fname, "r") as f:
        text = f.read()
        return text_to_ids(text)


def register_dic():
    files = glob.glob(root_dir+"*.txt", recursive=True)
    for i in files:
        file_to_ids(i)


def count_file_freq(rank):
    global X
    global Y
    global word_dic
    global max_words
    path = str(rank) + ".txt"
    print("path:" + path)
    print("max:" + str(max_words))
    f = open(path, "r")
    for line in f:
        cnt = [0 for n in range(max_words)]
        text = line.strip()
        ids = text_to_ids(text)
        for wid in ids:
            cnt[wid] += 1
        X.append(cnt)
        Y.append(rank)
    f.close()


def count_freq():
    for rank in range(1, 4):
        count_file_freq(rank)
        print(str(rank) + ":ok")


if __name__ == '__main__':
    main()