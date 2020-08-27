#!/usr/bin/python
'''
网上收集的字典，有些部分重合，我们将重合部分去掉，生成一个新的字典
'''

import argparse
import sys

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Process some integers.')
  parser.add_argument('src1', type=str, help='one input file name')
  parser.add_argument('src2', type=str, help='one input file name')
  parser.add_argument('meg', type=str, help='output file name')
  args = parser.parse_args()
  print(args.src1)
  print(args.src2)
  print(args.meg)
  
  set_1 = set()
  for line in open(args.src1): 
      set_1.add(line)
      
  set_2 = set()
  for line in open(args.src2): 
      set_2.add(line)
      
  print(args.src1, len(set_1), 'lines')
  print(args.src2, len(set_2), 'lines')

  for one in iter(set_2):
    set_1.add(one)
  print(args.src1, len(set_1), 'lines')
  
  fileObject = open(args.meg, 'w')
  for one in iter(set_1):
    fileObject.write(one)
  fileObject.close()
