'''
Created on Aug 23, 2012

convert tokenized plain text to word frequency matrix


@author: vivienne
'''
import re
import MyStemmer

stopwordlist='i you u he she they my your ur his her their mine them it its myself \
that this these those there are is am be been do doe did have has \
in on to of down up into onto upto between behind until after before out \
light because so and but a an the if off how however too we also would then should not with \
like about were for from me us him'
stopwords=stopwordlist.split()

def gen_word_list(txt):
    wordset=[]
    for line in txt:
        if not re.search('<[^>]*>',line) and re.search('\w',line):
            if line.find('||')>-1:
                title, author, date, nodeid=line.split('||')
                for word in title.split():
                    word=word.lower()
                    word=MyStemmer.Stem(word)
                    if word not in wordset:
                        if re.search('\w',word) and word not in stopwords:
                            wordset.append(word)
            else:
                for word in line.split():
                    word=word.lower()
                    word1=word
                    word=MyStemmer.Stem(word)
                    if word not in wordset:
                        if re.search('\w',word) and word not in stopwords:
                            wordset.append(word)
                            #print word1+'-->'+word
    i=0
    dic={}
    for word in wordset:
        dic[word]=i
        i+=1
    return wordset,dic

if __name__ == '__main__':
    txt=open('tokenized').readlines()
    wordlist,dic=gen_word_list(txt)
    doclist=[]
    dwordlist=[]
    #print str(dic)
    for line in txt:
        if not re.search('<[^>]*>',line) and re.search('\w',line):
            if line.find('||')>-1:
                title, author, date, nodeid=line.split('||')
                if dwordlist<>[]:
                    doclist.append(dwordlist)
                    dwordlist=[]
                    
                dwordlist.append(nodeid.strip())
                    
                for i in range(0,len(wordlist)):
                    dwordlist.append(0)
                for word in title.split():
                    word=word.lower()
                    word=MyStemmer.Stem(word)
                    if re.search('\w',word) and word not in stopwords:
                        dwordlist[dic[word]+1]+=1
            else:
                if dwordlist<>[]:
                    for word in line.split():
                        word=word.lower()
                        word=MyStemmer.Stem(word)
                        if re.search('\w',word) and word not in stopwords:
                            dwordlist[dic[word]+1]+=1
    doclist.append(dwordlist)
    newline=str(wordlist)
    newline=newline.replace('[','')
    newline=newline.replace(']','')
    newline=','+newline
    print newline
    #print wordlist
    #print str(len(wordlist))
    for dwordlist in doclist:
        newline=str(dwordlist)
        newline=newline.replace('[','')
        newline=newline.replace(']','')
        print newline
                        
