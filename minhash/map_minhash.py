#!/usr/bin/env python
#coding=utf-8
import sys
import minhash as mh

def run(fin, fout):
    ''' @fin : user\titemitem1....
        @fout : user\tminItem
    '''
    line = fin.readline()
    fout.write(process(line))
    for line in fin:
        fout.write(process(line))

def process(line, q):
    ''' @line: user\titemitem1....
        @q : num of min item 
        @return: user\tminItem1minItem2...
    '''
    line = line.strip()
    eleList = line.split('\t')
    user = eleList[0]
    items = eleList[1] 
    return mh.getMinSeqItem(items, q) 

if __name__ == "__main__": 
    run(sys.stdin, sys.stdout)
