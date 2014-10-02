import MyStemmer

vocab=[item.strip() for item in open('vocab').readlines()]

lines=open('tokenized_syo').readlines()
beta=[item.strip().split() for item in open('final.beta').readlines()]
nf=open('topic_all_o','w')
for l in lines:
    
    all=''
    for j in range(0,10):
    
        tuple=l.strip().split()
        
        sum=0
        for t in tuple:
            t=MyStemmer.Stem(t)
            if t in vocab:
                i=vocab.index(t)
                topic_beta=beta[j][i]
            else:
                topic_beta=-800
            sum+=float(topic_beta)
        if len(tuple)<>0:
            all+=str(sum/float(len(tuple)))+' '
    if all<>"":
        nf.write(all+'\n')
        
    
    
