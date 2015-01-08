# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 11:04:31 2015

@author: liuweizhi
"""

import os
import re
from datetime import *

global sentence_sep
global word_sep 
sentence_sep = '@@'
word_sep = '##'

class Word():
    def __init__(self):
        self.dir = os.path.join(os.getcwd(), 'words.txt')
        return
    def parse(self, sentence):
        global word_sep
        increment = len(word_sep)
        word_list = []
        left = 0
        right = 0
        while sentence.find(word_sep)!=-1:
            left = sentence.find(word_sep)
            sentence = sentence[left+increment:]
            right = sentence.find(word_sep)
            word_list.append(sentence[:right].strip())    
            sentence = sentence[right+increment:]
        return word_list
    def retrieve(self, content):
        f = open(self.dir, 'w')
        f.write('Date\tWord\tMeaning\tExample\n')
        global sentence_sep
        global word_sep
        sentences = [foo.strip().replace(sentence_sep, '')+'.' for foo in re.split('\.|\!|\?|\n|\r', content) if foo]
        for sen in sentences:          
            #words = re.findall('%s(\S+)%s' % (word_sep, word_sep), sen)
            words = self.parse(sen)
            for word in words:
                f.write('%s\t%s\t%s\t%s\n' % (str(date.today()), word, '', sen.replace(word_sep, '')))
        f.close()
        return
   
class Sentence():
    def __init__(self):
        self.dir = os.path.join(os.getcwd(), 'sentences.txt')
        return
    def retrieve(self, content):
        f = open(self.dir, 'w')
        f.write('Date\tSentence\tComments\n')
        global sentence_sep
        global word_sep
        sentences = [foo.strip().replace(word_sep, '')+'.' for foo in re.split('\.|\!|\?|\n|\r', content) if foo]
        for sen in sentences:
            if sentence_sep in sen:
                f.write('%s\t%s\t%s\n' % (str(date.today()), sen.replace(sentence_sep, ''), ''))
        f.close()
        return
    
class Snippet():
    def __init__(self):
        self.name = 'snippet.txt'
        self.dir = os.path.join(os.getcwd(), self.name)
        return        
    def read(self):
        with open(self.dir, 'r') as snippet:
            self.content = snippet.read()
        return self.content
        
snippet = Snippet()
content = snippet.read()

words = Word()
words.retrieve(content)        
sentences = Sentence()
sentences.retrieve(content)