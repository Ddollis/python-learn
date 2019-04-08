# -*- coding:utf-8 -*-
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print bicycles[0]
print bicycles
print bicycles[0].title()  # 首字母大写

for i in range(len(bicycles)):
    print bicycles[i]

bicycles.append('qindi')
print bicycles
bicycles.insert(0, 'qindidi')
print bicycles
del bicycles[0]
print bicycles
bicycles.pop(0)
bicycles.pop()
print bicycles
bicycles.remove('redline')
print bicycles

names = ['zhangsan', 'lisi', 'wangwu']
names.remove('lisi')
names.append('zhaoliu')
print names
names.insert(0, 'qindi')
names.insert(2, 'diyy')
names.append('wanglining')
print names

names.pop()
names.pop()
names.pop()
names.pop()
del names[1]
del names[0]
print names