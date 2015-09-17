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
from os import listdir
from os.path import isfile, join

listKeyword = {}
listNotKeyword = {}

domain = 'smartphone/'

def readKeyword():
	f = codecs.open(domain + 'keyword.txt', encoding = 'utf-8-sig')
	for keyword in f:
		keyword = keyword.replace('\n', '')
		# keyword = keyword.encode('utf-8-sig')
		listKeyword[keyword] = 1
	f.close()

def readNotKeyword():
	f = codecs.open(domain + 'not_keyword.txt', encoding = 'utf-8-sig')
	for keyword in f:
		keyword = keyword.replace('\n', '')
		# keyword = keyword.encode('utf-8-sig')
		listNotKeyword[keyword] = 1
	f.close()

def process():
	fOutput = codecs.open(domain + 'result.txt', 'w', encoding = 'utf-8-sig')
	folderContentFinal = './../../bigdata/'
        
	listFileContentFinal = [ f for f in listdir(folderContentFinal) if isfile(join(folderContentFinal,f)) ]
	listFileContentFinal.sort()
	pre_content = ''
	pre_title = ''
	index = -1
	numDoc = 0
	for fileContentFinal in listFileContentFinal:
		print fileContentFinal
		index += 1
		if index == 0:
			continue
		f = codecs.open(folderContentFinal + fileContentFinal, encoding='utf-8-sig')
		for document in f:
			array = re.split('----', document)
			if len(array) < 2:
				continue  
			content = array[1]
			array_domain_title = re.split('\t', array[0])
			if len(array_domain_title) < 2:
				continue
			title = array_domain_title[1]
			if title == pre_title or content == pre_content:
				continue
			# content = content.encode('utf-8-sig')
			for keyword in listKeyword:
				if content.find(keyword) != -1 and title.find(keyword) != -1:
					for notKeyword in listNotKeyword:
						if content.find(notKeyword) == -1:
							# content = content.encode('utf-8-sig')
							numDoc += 1
							print numDoc
							pre_content = content
							pre_title = title
							fOutput.write(content)
		f.close()
	fOutput.close()



if __name__ == '__main__':
	start = time.time()
	readKeyword()
	readNotKeyword()
	process()
	done = time.time()
	elapsed = done - start
	print(elapsed)