import re 
import requests
import os


page=1
pages=str(page)
num=input('num:')
nl=list(num)
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
add=input('add:')
n = 0
for i in range(1,40):
    ii=str(i)
    url='https://www.tujigu.com/a/'+num+'/'+ii+'.html'
    if ii == '1':
        url='https://www.tujigu.com/a/'+num+'/'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    r=res.text
    
    p=re.findall(r'<img src="(.*?)"',r)
    iff=re.findall(r'<title>(.*?)</title>',r)
    print(iff)
    if '404错误 网站改版、请重新访问' in iff:
        break
    for pic in p:
        

        check=list(pic)
        
        nn=str(n)
        picture = requests.get(pic)
        pp=picture.content
        photo = open(add+'\\'+nn+".png","wb")
        photo.write(pp) 
        photo.close()

        if check[27]!=nl[1] or check[28]!=nl[2] or check[29]!=nl[3]:

            os.remove(add+'\\'+nn+".png")
        n+=1



    # name=r'C:\\Users\\92813\\Desktop\\dd\\c.txt'
    # photo=open(name,"wb")
    # photo.write()    
        
    #     if live==picn:
    #         page
    #         picn0+=picn
    #         picn1=picn+1
