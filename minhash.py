#!/usr/bin/env python
#coding=utf-8
import random
import itertools
import operator

def minhash(userList, q):
    ''' @userList : [(user, [item1, item2.....), (user1, [item3, item4...])...]
        @q : the num of minhash
    '''
    userMinhashList = []
    for user, itemList in userList:
        num = len(itemList)
        minSeqList = getMinSeq(q, num)
        userMinhashList.append((user, [itemList[i] for i in minSeqList]))
    return userMinhashList

def getMinSeq(q, num):
    minSeqList  = []
    for i in range(q):
        seqList = [(i, random.randint(1, 10 ** 6)) for i in range(num)]
        m = min(seqList, key=operator.itemgetter(1))
        minSeqList.append(m[0])
    return minSeqList

        

if __name__ == "__main__":
    userList = [("haoyuan", ["ak420", "ipad", "girlfriend"]),
    ("fenfen", ["ak46", "bayaji", "genjiu"])]
    print minhash(userList, 10)
