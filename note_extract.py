'''
Created on Aug 21, 2012


extract raw text notes from html data dump

@author: vivienne
'''

import os
import re

header = """<ALLNOTES>
"""

footer = """
</ALLNOTES>"""
if __name__ == '__main__':
    dirs=os.listdir('html/')
    nf=open('alltext.xml','w')
    nf.write(header)
    for dir in dirs:
        if os.path.isdir(os.path.join('html',dir)):
            htmlf=open(os.path.join('html',dir,'readercontents.htm'))
            htmltxt=htmlf.read()
            print dir
            head,body=htmltxt.split('<tbody>')
            notes=body.split('<tr>')
            count=0
            nf.write("<FOLDER dir=\"%s\">\n"%dir)
            for note in notes:
                if note<>'':
                    tds=re.split('<td |</td>',note)
                    
                    
                    td=tds[-2]
                    td=td.replace('</td>','')
                    td=td.replace('</tr>','')
                    #td=td.replace('<br>','')
                    td=td.replace('&nbsp;',' ')
                    td=td.replace('\n',' ')
                    td=td.replace('\r',' ')
                    if len(tds)==7:
                        re_exp='<img [^>]*>|<i>|<br>'
                        items=re.split(re_exp,td)
                        #print str(td)
                        noteid=items[1]
                        toss,noteid=noteid.split('NoteID=')
                        noteid,toss=noteid.split('&amp;')
                        print noteid
                        items=items[2:len(items)]
                        idnum=0
                        for item in items:
                            if idnum==0:
                                item=re.sub('</[\w]*>',' ',item)
                                subitems=re.split('<font[^>]*>',item)
                                newline = '<NOTE title=\"%s\" author=\"%s\" date=\"%s\" note_id=\"%s\">\n' % (subitems[0].strip(),subitems[1].strip(),subitems[2].strip(),noteid)
                                nf.write(newline)
                                idnum+=1
                            else:
                                #item=re.sub('</[\w]*>',' ',item)
                                #item=re.sub('<span[^>]*>','<tag>',item)
                                #item=re.sub('</span>','</tag>',item)
                                istag=re.search('<span[^>]*>([^<]*)</span>',item)
                                tag=['']
                                if istag:
                                    tag=istag.groups()
                                item=re.sub('<span[^>]*>[^<]*</span>','<tag class=\"%s\">'%tag[0],item)
                                
                                item=re.sub('</a>',' ',item)
                                item=re.sub('</i>',' ',item)
                                item=re.sub('</sup>',' ',item)
                                item=re.sub('<sup>',' ',item)
                                item=re.sub('</font>','</f>',item)
                                
                                item=re.sub('<font[^>]*>','<f>',item)
                                item=re.sub('<a href="javascript[^&]*&amp;NoteID=','<LINK to_id=\"',item)
                                item=re.sub('&amp;ParentID[^>]*>|\',\'[0-9]*\'[)]\">','\"/>',item)
                                if item.strip()<>'':
                                    '''
                                    print 'item: '+item.strip()
                                    item=item.strip()
                                    subitems=re.split('<span[^>]*>|<font[^>]*>',item)
                                    print str(subitems)
                                    for subitem in subitems:
                                    '''
                                    if item.find("<tag")>-1:
                                        item+='</tag>\n'
                                    else:
                                        item+='\n'
                                    nf.write(item)
                            
                        count+=1
                        nf.write('</NOTE>\n')
            print str(count)
            nf.write('</FOLDER>\n')
    nf.write(footer)



         	
