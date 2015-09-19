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
listcontent = {}

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
	fOutput = codecs.open(domain + 'result_find_in_content.txt', 'w', encoding = 'utf-8')
	folderContentFinal = './../../../bigdata/'
        
	listFileContentFinal = [ f for f in listdir(folderContentFinal) if isfile(join(folderContentFinal,f)) ]
	listFileContentFinal.sort()

	index = -1
	numDoc = 0
	num_equal = 0
	for fileContentFinal in listFileContentFinal:
		index += 1
		f = codecs.open(folderContentFinal + fileContentFinal, encoding='utf-8')
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
			# content = content.encode('utf-8')
			for keyword in listKeyword:
				if ok == 1:
					break
				if keyword in content:
					for notKeyword in listNotKeyword:
						if notKeyword in content:
							notKeyword = notKeyword.encode('utf-8')
							ok = 1
					if ok == 0:
						numDoc += 1
						print 'in CONTENT : ', domain, numDoc
						print '----------'
						content = content.replace('\n', '')
						content += '\n'
						listcontent[content] = 1
						fOutput.write(source + '============' + title + '============' + content)
						ok = 1

		f.close()
	fOutput.close()



if __name__ == '__main__':

	domains = [ f for f in listdir('domain/') ]
	domains.sort()
	start = time.time()
	index = 0
	domain_number = int(sys.argv[1])
	print 'domain_number : ', domain_number
	for key in domains:
		index += 1
		if index != domain_number:
			continue
		domain = 'domain/' + key + '/'
		listKeyword = {}
		listNotKeyword = {}
		readKeyword()
		readNotKeyword()
		process()
		done = time.time()
		elapsed = done - start
		print(elapsed)