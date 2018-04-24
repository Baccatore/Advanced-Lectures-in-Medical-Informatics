#coding:utf8
#Author: yuichiro suga
#rf: https://tech-camp.in/note/technology/1050/
#Modified original code

def linear_search(key, data):
    for i, num in enumerate(data):
        if key == num:
            print 'Found {} in data[{}]'.format(key,i)
            return
    print 'Not found {} in data'.format(key)


data = [3, 5, 9 ,12, 15, 21, 29, 35, 42, 51, 62, 78, 81, 87, 92, 93]

linear_search(62, data)
linear_search(9, data)
linear_search(10, data)
