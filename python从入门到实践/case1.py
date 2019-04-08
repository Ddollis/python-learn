# -*- coding:utf-8 -*-
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print bicycles[0]
print bicycles
print bicycles[0].title() # 首字母大写

for i in range(len(bicycles)):
    print bicycles[i]

bicycles.append('qindi')
print bicycles
bicycles.insert(0,'qindidi')
print bicycles
del bicycles[0]
print bicycles
bicycles.pop(0)
bicycles.pop()
print bicycles