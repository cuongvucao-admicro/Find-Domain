#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import codecs
import re
import time
import operator
import math
import random
import itertools
import re
import sys
from os import listdir
from os.path import isfile, join

listKeyword = {}
listNotKeyword = {}
listSourceRemove = {}
listSourceSkip = {}

domain = ''

def readKeyword():
	f = codecs.open(domain + 'keyword.txt', encoding = 'utf-8')
	for keyword in f:
		keyword = keyword.replace('\n', '')
		# keyword = keyword.encode('utf-8')
		listKeyword[keyword] = 1
	f.close()

def readNotKeyword():
	f = codecs.open(domain + 'not_keyword.txt', encoding = 'utf-8')
	for keyword in f:
		keyword = keyword.replace('\n', '')
		# keyword = keyword.encode('utf-8')
		listNotKeyword[keyword] = 1

	f.close()

def process():
	fOutput = codecs.open('result_find_by_source.txt', 'w', encoding = 'utf-8')

	folderContentFinal = './../../../bigdata/'      
	listFileContentFinal = [ f for f in listdir(folderContentFinal) if isfile(join(folderContentFinal,f)) and f[0] != '.' ]
	listFileContentFinal.sort()

	index = -1
	numDoc = 0
	num_equal = 0
	for fileContentFinal in listFileContentFinal:
		index += 1
		f = codecs.open(folderContentFinal + fileContentFinal, encoding='utf-8-sig')
		print fileContentFinal
		for document in f:
			ok = 0
			array = re.split('----', document)
			if len(array) < 2:
				continue
			content = array[1]
			array_domain_title = re.split('\t', array[0])
			if len(array_domain_title) < 2:
				continue
			title = array_domain_title[1]
			source = array_domain_title[0]
			for keyword in listSourceSkip:
				if keyword in source:
					numDoc += 1
					print numDoc
					fOutput.write(source + '==========' + title + '==========' + content + '\n')
					break

		f.close()
	fOutput.close()

def readSourceRemove():
	f = codecs.open(domain + 'source_remove.txt', encoding = 'utf-8-sig')
	for keyword in f:
		keyword = keyword.replace('\n', '')
		# keyword = keyword.encode('utf-8-sig')
		listSourceRemove[keyword] = 1
	f.close()

def readSourceSkip():
	f = codecs.open(domain + 'source_skip.txt', encoding = 'utf-8-sig')
	for keyword in f:
		keyword = keyword.replace('\n', '')
		# keyword = keyword.encode('utf-8-sig')
		listSourceSkip[keyword] = 1
	f.close()

if __name__ == '__main__':

	domains = [ f for f in listdir('domain/') ]
	domains.sort()
	start = time.time()
	readSourceRemove()
	readSourceSkip()
	index = 0
	process()