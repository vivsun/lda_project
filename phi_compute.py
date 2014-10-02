'''
Created on Aug 30, 2012

compute phi value based on the lda output
pls refer to Blai's LDA paper for detailed explaination

@author: vivienne

Arg:
    final.beta - from lda-c-dist
    <??>.gamma - from lda inference

output:
    phi/#doc.phi -  #word * #topic
    
'''
from optparse import OptionParser
import math
import re

def get_beta(fname): 
    '''
    get beta (in log space)/gamma from file
    '''
    txt=open(fname).readlines()
    beta=[]
    for line in txt:
        betaline=line.strip().split()
        beta.append(betaline)
    m=len(betaline)
    n=len(beta)
    return beta, n, m
        
def digamma(x):
    '''
    per lda-c-dist
    first derivative of the log lamda function, using Taylor approximation
    '''
    x=float(x+6)
    p=1/(x*x)
    p=(((0.004166666666667*p-0.003968253986254)*p+\
    0.008333333333333)*p-0.083333333333333)*p
    p=p+math.log(x)-0.5/x-1/(x-1)-1/(x-2)-1/(x-3)-1/(x-4)-1/(x-5)-1/(x-6);
    return p

def get_word_doc_freq(fname):
    txt=open(fname).readlines()
    wdf=[]
    for line in txt:
        wdfline=line.strip().split(',')
        if wdfline[0]<>'':
            wdf.append(wdfline[1:len(wdfline)])    
    m=len(wdfline)-1
    n=len(wdf)
    return wdf, n, m    
    
if __name__ == '__main__':
    parser = OptionParser()
    (options, args) = parser.parse_args()
    
    stri=args[0]
    beta,K,N=get_beta('%s_10_est/final.beta'%stri)
    print str(K)+' '+str(N)
    gamma,M,K=get_beta('%s_10_est/final.gamma'%stri)
    print str(M)+' '+str(K)
    wdf,M,N=get_word_doc_freq('wdf-w-vocab')
    print str(M)+' '+str(N)
    for m in range(0,M):
        nf=open(stri+'_phi/'+str(m+1)+'.phi','w')
        newline=''
        for n in range(0,N):
            for k in range(0,K):
                phink=float(beta[k][n])+digamma(float(gamma[m][k]))
                newline+=str(phink)+' '
            newline+='\n'
        nf.write(newline)
        nf.close()
    
        
    
    
    
    
    
