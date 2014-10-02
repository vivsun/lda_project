'''
Created on Aug 23, 2012


extract plain text note from xml

@author: vivienne
'''
import os
import re

if __name__ == '__main__':
    xmltxt=open('alltext.xml').readlines()
    nf=open('plaintxt','w')
    for xmlline in xmltxt:
        if re.search('<FOLDER',xmlline):
            re_exp = '<FOLDER dir=\"([^"]*)">'
            m = re.search(re_exp, xmlline)
            if m:
                folder_name = m.groups()
            else:
                raise Exception("Malformed FOLDER tag: %s" % (xmlline))
            nf.write("\n<%s>\n"%folder_name[0])
        elif re.search('<NOTE',xmlline):
            re_exp = 'NOTE title=\"([^"]*)"\s*author=\"([^"]*)"\s*date=\"([^"]*)"\s*note_id=\"([^"]*)"\s*>'
            m = re.search(re_exp, xmlline)
            if m:
                title,author,date,id = m.groups()
                author=author.replace('by ','')
                date=date.replace('[','')
                date=date.replace(']','')
            else:
                raise Exception("Malformed FOLDER tag: %s" % (xmlline))
            newline='\n%s||%s||%s||%s\n' % (title,author,date,id)
            nf.write(newline)
        else:
            newline=re.sub('<[^>]*>','',xmlline)
            if re.search('\w',newline):
                nf.write(newline.rstrip()+'\n')
    nf.close()        
        
        
