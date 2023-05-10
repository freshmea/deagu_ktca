import sys
import os
from turtle import *

print(sys.argv)
print(sys.getwindowsversion())
print(sys.copyright)
print(sys.version)
print(sys.version_info)
print(sys.path)

print(os.getcwd())
print(os.listdir())
print(os.chdir('src/'))
print(os.getcwd())
try:
    os.mkdir('test')
except:
    pass
os.rmdir('test')
os.rename('../data/hello.txt', '../data/rename.txt')
os.rename('../data/rename.txt', '../data/hello.txt')
os.system('ipconfig')

# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
#     print(position())
# end_fill()
# done()