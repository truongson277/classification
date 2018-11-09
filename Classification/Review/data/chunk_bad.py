from  underthesea  import  chunk

def data_chunk(text):
    _list = chunk(text)
    results_chunk = []
    for index, val in enumerate(_list):
        if val[1] not in ['V', 'R', 'A', 'X', 'C']: continue
        results_chunk.append(val[0])
    return results_chunk


with open('bad/bad.txt', 'r') as bad_data:
    for index, val in enumerate(bad_data):
        line = data_chunk(val.lower())
        line = '/'.join(line)
        if line != '':
            with open('bad/1.txt', 'a+') as bad_chunk:
                bad_chunk.write(line + '\n')



