import math,sys,os
import re

def socketMerchant(n,arr):
    counter = 0
    i = 0
    sorted_ar = sorted(arr)

    while i < n:
        if i+1 <n and sorted_ar[i]==sorted_ar[i+1]:
            counter+=1
            i+=2
        else:
            i+=1
    return counter

if __name__ == '__main__':
    fin = open(os.environ['OUTPUT_PATH'],'w')
    n = int(input())
    arr = list(map(int,input().rstrip().split()))
    result = socketMerchant(n,arr)
    fin.write(str(result)+'\n')
    fin.close()