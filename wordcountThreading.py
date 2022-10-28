import threading
import time
from typing import List

def countWord(dt, res_list):
    wdict = {}
    for word in dt:
        word = word.lower()
        if(wdict.get(word)):
            wdict[word] += 1
            continue

        wdict[word] = 1
    res_list.append(wdict)
    return res_list
    
def fileOpen(fname, mode):
    with open(fname, mode, encoding='utf8') as f:
        data = f.read()
    return data
    
def divide_chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]
    
def mergeResult(lst, fdic):
    count = 0
    for item in lst:
        for key, value in item.items():
            if(fdic.get(key)):
                fdic[key] += value
                count += value
                continue
            
            fdic[key] = value
            count += value
    return fdic, count            

def main():
    # Starting time of ex after input
    st = time.time()

    # Reading file content
    data = fileOpen(fileName, mode).replace('\n','').split(' ')
    
    length = len(data)
    try:
        chunk = length//instances
    except ZeroDivisionError:
        chunk = 1
    divList = divide_chunks(data, chunk)
    # print(f"{len(divList)} instances created")

    # storing all threads
    threads = list()
    # for storing result
    res_list = list()
    # concat the result in one dict
    fdic = dict()

    for item in range(len(divList)):
        try:
            x = threading.Thread(target=countWord, name=f't{item}', args=(divList[item] ,res_list ,))
            threads.append(x)
            x.start()
        except:
            print("Error: unable to start thread")

    for index, thread in enumerate(threads):
            thread.join()

    # print(f'Result list is :{res_list}')

    fdic, count = mergeResult(res_list, fdic)
    print(f'Total count is :{count}')

    # ending time of ex
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    print(f'Execution time: {elapsed_time} seconds')

    return elapsed_time, instances

if __name__ == "__main__":
    etList = list()
    insList = list()
    while True:
        fileName = input("Enter filename to read :")
        if(fileName == ''):
            break

        mode ='r'
        instances = int(input("Enter no of Map instances :"))
        et, ins = main()
        etList.append(et)
        insList.append(ins)
    
    with open('result.txt', 'w') as f:
        f.write(str([etList, insList]))
        f.close()
    
