'''
Created on Aug 30, 2012

print an html file with color coded topic-assignment

@author: vivienne
'''

header = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head><link rel="stylesheet" type="text/css" href="topicStyles.css" /></head>
<body>"""

footer = """</body>
</html>"""

navigator="""<table><tr>
<td><a href='#T5'>5 alpha</a><td>
<td><a href='#T6'>6 alpha</a><td>
<td><a href='#T7'>7 alpha</a><td>
<td><a href='#T8'>8 alpha</a><td>
<td><a href='#T9'>9 alpha</a><td>
<td><a href='#T10'>10 alpha</a><td>
<td><a href='#T11'>11 alpha</a><td>'
<td><a href='#T12'>12 alpha</a><td>
<td><a href='#T13'>13 alpha</a><td>
<td><a href='#T14'>14 alpha</a><td>
<td><a href='#T15'>15 alpha</a><td>
<td><a href='#T16'>16 alpha</a><td>
<td><a href='#T17'>17 alpha</a><td>
</tr></table>"""

from optparse import OptionParser
import os
import sys
import math
import re

def get_beta(fname): 
    '''
    get beta (in log space)/gamma from file
    '''
    txt=open(fname).readlines()
    beta=[]
    for line in txt:
        betalinestr=line.strip().split()
        betaline=[]
        for betastr in betalinestr:
            betaline.append(float(betastr))
        beta.append(betaline)
    m=len(betaline)
    n=len(beta)
    return beta, n, m

def get_vocab(fname):
    txt=open(fname).readlines()
    vocab=txt[0].split(',') 
    vocab=vocab[1:len(vocab)]
    dicvocab={}
    i=0
    for word in vocab:
    	word2=re.sub('[\'\s]','',word.lower())
        dicvocab[word2]=i
        i+=1
    return dicvocab

def color_code(topic_num):
	colormap={}
	colormap[1]='#7FFFD4'
	colormap[2]='#8A2BE2'
	colormap[3]='#DC143C'
	colormap[4]='#7FFF00'
	colormap[5]='#A9A9A9'
	colormap[6]='#FF8C00'
	colormap[7]='#483D8B'
	colormap[8]='#FF1493'
	colormap[9]='#FFD700'
	colormap[10]='#ADFF2F'
	colormap[11]='#FF69B4'
	colormap[12]='#000080'
	colormap[13]='#A52A2A'
	colormap[14]='#FF7F50'
	colormap[15]='#008080'
	colormap[16]='#006400'
	colormap[0]='#9ACD32'
	return colormap[topic_num]

def color(segment, color):
    
    return "<font color=%s>%s</font>" % (color, segment)

def get_doc(fname):
    '''
    input:
        fname: filename of plain txt of all notes
    output:
        doc: list of individual notes
    '''
    doc=[]
    txt=open(fname).readlines()
    note=''
    for line in txt:
        if re.search('<[^>]*>',line):
            pass
        elif re.search('\|\|',line):
            if note<>'':
                doc.append(note)
                note=line
        else:
            note+=line
    return doc 
   
def print_topics(betafname,vocabfile,numtopics):
    '''
    input: 
        betafname: final beta file name
        vocabfile: file name of word document frequency file
        numtopics: index (number of topics, or in this case alpha value)
    print:
        print topic key words table
        print notes with highest gamma value
    
    '''
    doc=get_doc('plaintxt')
    txt=open(vocabfile).readlines()
    vocab=txt[0].split(',') 
    vocab=vocab[1:len(vocab)]	
    indices = range(len(vocab))
    topic_no = 0
    print '<br/><table style=\"border: 1px solid black; border-collapse:collapse;\">'
    for topic in file(betafname, 'r'):
		printline=''
		cc=color_code(topic_no)
		topic_title=color('Topic %03d' % topic_no, cc)
		topic = map(float, topic.split())
		indices.sort(lambda x,y: -cmp(topic[x], topic[y]))
		keywords=''
		
		for i in range(10):
			keywords+='   %s' % vocab[indices[i]]
		topic_no = topic_no + 1
		printline='<tr style=\"border: 1px solid black; border-collapse:collapse;\"> \
		<td style=\"border: 1px solid black; border-collapse:collapse; padding: 5px;\">%s</td>\
		<td style=\"border: 1px solid black; border-collapse:collapse; padding: 5px;\">%s</td></tr>' % (topic_title,color(keywords,cc))
		print printline
    print '</table><br/>'
    written_files=[]
    gammas_list=[]
    for irt in range(0,3):
        
        wf,gammas =print_sample_files(str(numtopics)+'_10_est/final.gamma',numtopics,written_files)
        written_files.append(wf)
        gammas_list.append(gammas)
    for i in range(0,10):
        print "<br/><h4>Sample docs for topic #%s</h4><br/>"%str(i)
        #for towrite in written_files:
        for j in range(0,len(written_files)):
            
            print_note(doc,written_files[j][i]+1,numtopics,i,gammas_list[j][i])
                #print str(written_files)


def test_written(i,topic,written_files):
    tw=0
    for wfiles in written_files:
        if i == wfiles[topic]:
            tw=1
    return tw

def print_sample_files(gammafname,numtopics,written_files):
	doc=get_doc('plaintxt')
	topic_no = 0
	sample_file_nums=[]
	sample_file_gamma_values=[]
	temp=[]
	for i in range(0,10):
		sample_file_nums.append(0)
		sample_file_gamma_values.append(0.0)
	for i in range(0,10):
		topics=open(gammafname).readlines()
                
                for j in range(0,len(topics)):
                    topiclist = map(float, topics[j].split())
                    if topiclist[i]>sample_file_gamma_values[i] and not test_written(j,i,written_files) and j not in [136,96,80,118,81,115, 103, 101]:
                        sample_file_nums[i]=j
                        sample_file_gamma_values[i]=topiclist[i]
                        
    		#print(str(sample_file_nums[0]))
	#for i in range(0,numtopics):               
		#print_note(doc,sample_file_nums[i]+1,numtopics,i) 
	return sample_file_nums,sample_file_gamma_values

def print_note(doc,doc_num,numtopics,indexnum,gamma_value):
	dicvocab=get_vocab('wdf-w-vocab')

	print "<br/><h6>Record #%s, gamma = %f</h6><br/>"% (str(doc_num),gamma_value)
	phi,pn,pm=get_beta(str(numtopics)+'_phi/'+str(doc_num)+'.phi')
        
	note=doc[doc_num]

	lines=note.split('\n')
	printline=''
        print '<p>'
	for line in lines:
            if re.search('\|\|',line):
                print '<i>%s</i><br/>'%line
            else:
		words=line.split()

		printline=''
                for word in words:
                    tword=re.sub('[\.,:!\?;\'\"()+_=-]','',word.lower())
                    #print tword
                    try:
                        word_num=dicvocab[tword]
                        #print str(word_num)
                    except KeyError:
                        word_num=800
                    if word_num<>800:
                        phin=phi[word_num]
                        
                        #print str(phin)
                        sorted_phin=[]
                        for num in phin:
                            sorted_phin.append(num)
                        sorted_phin.sort()
                        max=sorted_phin[-1]
                        
                        topic_num=phin.index(max)
                        
                        cc=color_code(topic_num)
                        printline+=color(word,cc)+'<sup>'+str(topic_num)+'</sup>'+' '
                    else:
                        cc=[0,0,200]
                        printline+=color(word,cc)+' '
                    
                if printline<>'':
                    print printline+'<br/>'
        print '</p>'
        print "<a href='#T5'>Back to top</a>"
	
if __name__ == '__main__':
    parser = OptionParser()
    (options, args) = parser.parse_args()
    
    #doc_num=args[0]
    #phi,pn,pm=get_beta('phi/'+doc_num+'.phi')
    doc=get_doc('plaintxt')
    dicvocab=get_vocab('wdf-w-vocab')
    #print str(dicvocab)
    print header
    print navigator
    for i in range(5,18):
    	print '<a name=\"T%s\"><h1>Alpha = %s</h1></a>'%(str(i),str(i))
    	print_topics(str(i)+'_10_est/final.beta','wdf-w-vocab',i)
        print navigator+'<br/>'
    print footer
	
        
    
    
