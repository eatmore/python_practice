import os
path1 = os.getcwd()
print('\n' + path1)
os.chdir('/Users/wangyanjun/Documents/code/')
path2 = os.getcwd()
print(path2)

os.makedirs('/Users/wangyanjun/Documents/code/pyhon_manage')

print(os.path.abspath('.'))
