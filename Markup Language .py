#!/usr/bin/env python
# coding: utf-8

# In[10]:


p=open ('test_file_1_html.txt','w')
#creating a new text file which will give input text file for html
p.write('<html>'+'\n')
#starting for every html
dp=open ('test_file_1.txt','r')
x=dp.read()
val = {'$':['<b>','</b><br>'],'@':['<head>','</head><br>'],'!':['<title>','</title><br>'],'_':['<i>','</i><br>'],'#':['<h1>','</h1><br>'],'%':['<h2>','</h2><br>'],'^':['<h3>','</h3><br>'],'*':['<ul>','</ul><br>'],'-':['<ol>','</ol><br>'],'~':['<li>','</li><br>']}
#a.type()
#print(a.split('.')) # spliting lines ending with (.)
a=x.split('.')
#print(val['$'][0])
#print(a)    
for items in a:
    try:
        def recur(st):
            if st.find('$')!=(-1):
                s1=st.replace('$',val['$'][0],1)
                s2=s1.replace('$',val['$'][1],1)
                return recur(s2)
            elif st.find('@')!=(-1):
                s1=st.replace('@',val['@'][0],1)
                s2=s1.replace('@',val['@'][1],1)
                return recur(s2)
            elif st.find('!')!=(-1):
                s1=st.replace('!',val['!'][0],1)
                s2=s1.replace('!',val['!'][1],1)
                return recur(s2)
            elif st.find('_')!=(-1):
                s1=st.replace('_',val['_'][0],1)
                s2=s1.replace('_',val['_'][1],1)
                return recur(s2)
            elif st.find('#')!=(-1):
                s1=st.replace('#',val['#'][0],1)
                s2=s1.replace('#',val['#'][1],1)
                return recur(s2)
            elif st.find('%')!=(-1):
                s1=st.replace('%',val['%'][0],1)
                s2=s1.replace('%',val['%'][1],1)
                return recur(s2)
            elif st.find('^')!=(-1):
                s1=st.replace('^',val['^'][0],1)
                s2=s1.replace('^',val['^'][1],1)
                return recur(s2)
            elif st.find('*')!=(-1):
                s1=st.replace('*',val['*'][0],1)
                s2=s1.replace('*',val['*'][1],1)
                return recur(s2)
            elif st.find('-')!=(-1):
                s1=st.replace('-',val['-'][0],1)
                s2=s1.replace('-',val['-'][1],1)
                return recur(s2)
            elif st.find('~')!=(-1):
                s1=st.replace('~',val['~'][0],1)
                s2=s1.replace('~',val['~'][1],1)
                return recur(s2)
            else:
                return p.write(st)
        recur(items)
    except:
        print("Invalid input!!!")

    else:
        dp.close()
        #closing the input text file
p.write('</html>')
#ending for every html
p.close()
# closing the output text file


# In[ ]:




