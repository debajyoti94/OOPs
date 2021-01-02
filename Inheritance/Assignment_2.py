
'''
In this code we will create a hierarchy of classes and implement the concept of inheritance

'''

from DSDJ.OOP.Inheritance.FileWrite import LogFile, DelimFile

d = DelimFile('delim.txt', ',')
l = LogFile('logfile.txt')

l.write("first log message")

d.write(['a', 'b', 'c', 'd'])
d.write(['1', '2', '3', '49,9'])

