from underthesea import chunk

def data_chunk(text):
    _list = chunk(text)
    results_chunk = []
    for index, val in enumerate(_list):
        if val[1] not in ['V', 'R', 'A', 'X', 'C']: continue
        results_chunk.append(val[0])
    return results_chunk


with open('normal/normal.txt', 'r') as normal_data:
    for index, val in enumerate(normal_data):
        line = data_chunk(val.lower())
        line = '/'.join(line)
        if line != '':
            with open('3.txt', 'a+') as normal_chunk:
                normal_chunk.write(line + '\n')



