'''
Created on Aug 23, 2012


a very basic white space tokenizer that remove all puncturation (treat as white space) 

@author: vivienne

'''

import re

def tokenize_line(line):
    pname=re.search('([A-Z]\.[A-z]\.)',line)
    if pname:
        names=pname.groups()
        for name in names:
            subname=name.replace('.','#')
            line=line.replace(name,subname)
    line=re.sub('[\.,:!\?;\'\"()+_=-]',' ',line)
    line=re.sub('\s\s*',' ',line)
    line=re.sub('\A\s','',line)
    if pname:
        for name in names:
            subname=name.replace('.','#')
            line=line.replace(subname,name)
    return line

if __name__ == '__main__':
    txt=open('syl_optic.txt').readlines()
    nf=open('tokenized_syo','w')
    for line in txt:
        if line.find('||')>-1:
            title,author,date,nodeid= line.split('||')
            title=tokenize_line(title)
            newline='%s||%s||%s||%s' % (title,author,date,nodeid)
            nf.write(newline)
        else:
            line=tokenize_line(line)
            nf.write(line+'\n')
    nf.close()
