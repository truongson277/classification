import os, glob, json
from underthesea import chunk
from keras.models import load_model
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] ='2'

word_dic = { "_MAX":0 }
root_dir = ""
dic_file = root_dir + "/home/truongson/TS/classification/Classification/Review/static/data/review-dic.json"
global max_words


def main():
    global max_words
    global word_dic
    word_dic = json.load(open(dic_file))
    max_words = word_dic['_MAX']
    f = open('/home/truongson/TS/classification/Classification/Review/static/data/target.txt', 'r')
    # text = f.read()
    # f.close()
    # print(text)
    # good = {}
    # bad = {}
    # normal = {}
    results = {
        'good': {},
        'bad': {},
        'normal': {}
    }
    g = 0
    b = 0
    n = 0
    for i in f:
        i = i.replace('\n', '', 1000)
        if i != '':
            words = data_chunk(i)
            wt = "/".join(words)
            x = count_file_freq(wt)

            model = model_load()
            result = model.predict(np.array([x]))
            ranks = np.arange(1, 4).reshape(3, 1)
            predicted_rank = result.dot(ranks).flatten()
            # print(i)
            # print(wt)
            # print(predicted_rank[0])
            if predicted_rank[0] > 2.5:
                # print('Class = Normal')
                results['normal'].update({
                    n: {
                        'text': i,
                        'chunk': wt
                    }
                })
                n += 1
            elif predicted_rank[0] > 1.8:
                # print('Class = Good')
                results['good'].update({
                    g: {
                        'text': i,
                        'chunk': wt
                    }
                })
                g += 1
            else:
                # print('Class = Bad')
                results['bad'].update({
                    b: {
                        'text': i,
                        'chunk': wt
                    }
                })
                b += 1
    f.close()
    print(results)
    return results


def model_load():
    filename = "/home/truongson/TS/classification/Classification/Review/static/data/model_news.h5"
    loaded_model = load_model(filename)
    # loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model


def data_chunk(text):
    _list = chunk(text)
    results_chunk = []
    for index, val in enumerate(_list):
        if val[1] not in ['V', 'R', 'A', 'X', 'C']: continue
        results_chunk.append(val[0])
    return results_chunk


def text_to_ids(text):
    global word_dic
    text = text.strip()
    text = text.replace('\n', '/')
    words = text.split("/")
    result = []
    for n in words:
        n = n.strip()
        if n == "": continue
        if not n in word_dic: continue
            # if word_dic["_MAX"] > cnt_max:continue
            # wid = word_dic[n] = word_dic["_MAX"]
            # word_dic["_MAX"] += 1
        else:
            wid = word_dic[n]
        result.append(wid)
    return result


def count_file_freq(text):
    global max_words
    cnt = [0 for n in range(max_words)]
    text = text.strip()
    ids = text_to_ids(text)
    for wid in ids:
        cnt[wid] += 1
    return cnt


if __name__ == '__main__':
    main()