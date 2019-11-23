# -*- coding:utf-8 -*-
a = []
token_test_path = r'C:\Users\admin\Desktop\bert-chinese-ner-master\output\output1\token_test.txt'
f1 = open(token_test_path, 'r', encoding='UTF-8').readlines()
label_test_path = r'C:\Users\admin\Desktop\bert-chinese-ner-master\output\output1\label_test.txt'
f2 = open(label_test_path, 'r', encoding='UTF-8').readlines()
for i in range(len(f1)):
    aa=f1[i].split('\n')[0]+' '+f2[i].split('\n')[0]
    a.append(aa)
xx = open('./result.txt','w',encoding='UTF-8')
print(a)
for i in a:
    xx.write(i)
    xx.write('\n')
xx.close()

