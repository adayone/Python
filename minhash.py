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
        seqList = [(i, random.randint(1, 10 ** 6)) for i in range(num)]
        m = min(seqList, key=operator.itemgetter(1))
        userMinhashList.append((user, itemList[m[0]]))
    return userMinhashList
        

if __name__ == "__main__":
    userList = [("haoyuan", ["ak420", "ipad", "girlfriend"]),
    ("fenfen", ["ak46", "bayaji", "genjiu"])]
    print minhash(userList, 10)
