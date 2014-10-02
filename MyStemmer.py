'''
Created on Aug 27, 2012

@author: vivienne
'''

import re

class MyStemmer(object):
    '''
    Simple reg exp stemmer -Viv
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass

def Stem(word):
    #remove tailing s, ed, ly:
    reg_exp=re.compile('ed$|s$|ly$')
    test='0'
    
    if len(word)>4 and re.search('ly$|ing$',word):
        word2=re.sub('ly$|ing$', '', word)
    elif re.search('ied$',word):
        word2=re.sub('ied$', 'y', word)
    elif re.search('ized$|ated$|ined$|ved$',word):
        word2=re.sub('d$', '', word)
    elif re.search('ed$',word):
        word2=re.sub('ed$', '', word)
    elif re.search('ses$',word):
        word2=re.sub('ses$', 's', word)
    elif re.search('s$',word) and not re.search('ss$',word):
        word2=re.sub('s$', '', word)
    else:
        word2=word
    return word2