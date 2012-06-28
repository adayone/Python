#!/usr/bin/env python2.5
#coding=utf-8
'''@brief : using minhash to cluster the sim user.
'''
import sys
import minhash as mh

def run(fin, fout, q):
    ''' @fin : user\titemitem1....
        @fout : user\tminItem
        @q : num of min item 
    '''
    for line in fin:
        rs = process(line, q)
        if not rs:
            continue
        fout.write(rs)

def process(line, q):
    ''' @line: user\titemitem1....
        @q : num of min item 
        @return: user\tminItem1minItem2...
    '''
    line = line.strip()
    eleList = line.split('\t')
    if 2 != len(eleList):
        return None
    user = eleList[0]
    items = eleList[1] 
    itemList = items.split('')
    minhashList = mh.getMinSeqItem(itemList, q) 
    return '%s\t%s\n'%(user, ''.join(minhashList))    	


if __name__ == "__main__": 
    run(sys.stdin, sys.stdout, 3)
