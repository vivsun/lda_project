'''
Created on Aug 28, 2012

generate input data for the lda implement
input: word frequency csv

@author: vivienne
'''

if __name__ == '__main__':
    mat=open('wdf.csv').readlines()
    nf=open('ldainput.dat','w')
    for line in mat:
        cells=line.split(',')
        nodeid=cells[0]
        if nodeid<>'':
            term_freq=cells[1:len(cells)]
            newline=''
            i=0
            m=0
            for term in term_freq:
                term_count = int(term)
                if  term_count<>0:
                    m+=1
                    newline+='%s:%s ' % (str(i),str(term_count))
                i+=1
            newline=str(m)+' '+newline
            nf.write(newline+'\n')
            
