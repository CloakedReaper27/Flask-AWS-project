from array import *
import random
import sys
import base64
from collections import OrderedDict

memory_cache = {}
LRUs = OrderedDict()

max_Default = {0 : 1024000} # 1 MB Default
Algo_Default = {0:0}

def mem_cache(key,value):
    img_size = 0

    with open('static/images/'+value, "rb") as img_file:
                
        img_size = base64.b64encode(img_file.read()).decode("utf-8")

    if (max_Default[0]-Total_Size() > sys.getsizeof(img_size)):

        with open('static/images/'+value, "rb") as img_file:
                
            memory_cache[key] = base64.b64encode(img_file.read()).decode("utf-8")
                
        print("current size of cache is : ",Total_Size())
        

    elif (max_Default[0] < sys.getsizeof(img_size)):

        exit

    else:
        i = 0
        mem_list = list(memory_cache.keys())
        LRU_list = list(LRUs.keys())

        print ('Cache full!, executing chosen algorithm')
        while (max_Default[0]-Total_Size() < sys.getsizeof(img_size)):
            if (Algo_Default[0] == 0):

                # l = sorted(memory_cache.items(), key=lambda x: random.random())
                # chosen = l.pop()
                val = random.choice(mem_list)
                memory_cache.pop(val)
                
            elif (Algo_Default[0] == 1):

                key = LRU_list[i]
                print (LRUs.popitem())
                if key in memory_cache:
                    memory_cache.pop(key)
                i += 1
                

        with open('static/images/'+value, "rb") as img_file:
                
            memory_cache[key] = base64.b64encode(img_file.read()).decode("utf-8")
                
        print("current size of cache is : ",Total_Size())            

def Total_Size():
    s = 0
    for i in memory_cache:
        s = s + sys.getsizeof(memory_cache[i])
    return s