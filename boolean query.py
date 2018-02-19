#Processes Boolean query as argument 

#14095004 Aman Soni
#14095062 Shah Mit Paragbhai
#14095090  Shashwat Sinha

class MyStack:
    def __init__(self):
        self.container = []  

    def isEmpty(self):
        return self.container() == [] 

    def push(self, item):
        self.container.append(item) 

    def pop(self):
        return self.container.pop()

    def top(self):
        return self.container[len(self.container)-1]

import os, sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
def list_files(dir):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).next()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                r.append(subdir + "/" + file)                                                                         
    return r     

ps=PorterStemmer() 
pth='/home/mit/Downloads/Infomation Retrieval/Assignment 2 indexing/20news-18828/alt.atheism'
fls=list_files(pth)
cnt=0
dic={}
for fl in fls:
	f=open(fl,'r')
	cnt+=1
	tmp_dic={}
	words=[]
	for wrd in f:
		#print wrd
		words=wrd.split()
	for wrd in words:
		if wrd in tmp_dic:
			tmp_dic[wrd]+=1
		else:
			tmp_dic[wrd]=1
	f.close()
	cur_file_name=(fl.split('/'))[-1]
	for k in tmp_dic.keys():
		if k in dic:
			dic[k].append((tmp_dic[k],cur_file_name))
		else:
			dic[k]=[]
			dic[k].append((tmp_dic[k],cur_file_name))
	if(cnt%1000==0):
		print cnt
ops = MyStack()
d=dic
#print d

s = MyStack()
list_1 = []
list_2 = []
list_u = []
list_d = []
p1 = []
p2 = []
for i in range(0, len(sys.argv)):
    if sys.argv[i] == '(':
        s.push('(')
        continue
    elif sys.argv[i] == ')':
        temp = []
        cnt=0
        while not(s.top()=='('):
            temp.append(s.top())
            s.pop()
            cnt+=1
        s.pop()
        temp_op=ops.top()
        for i in range(0,cnt-1):
            ops.pop()
        temp_res=temp[0]
        del(temp[0])
        for t in temp:
            if temp_op == 'AND':
                temp_res=(list(set(temp_res) & set(t)))
                #print list(set(list_1) & set(list_2))
                #if len(ops)>0:    
            elif temp_op == 'OR':
                temp_res=(list(set(temp_res) | set(t)))
            elif temp_op == 'NOT':
                temp_res=(list(set(t)-set(temp_res)))
        s.push(temp_res)
    elif sys.argv[i] == 'AND':
        ops.push('AND')
        continue
    elif sys.argv[i] == 'OR':
        ops.push('OR')
        continue
    elif sys.argv[i] == 'NOT':
        ops.push('NOT')
        continue        
    else :
        if i==0:
            continue
        tmp_str=ps.stem(sys.argv[i])    
        s.push(map(list, zip(*d[tmp_str]))[1])  
print s.container

