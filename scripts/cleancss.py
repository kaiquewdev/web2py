import sys, re
filename=sys.argv[1]
data=open(filename,'r').read()
data=re.compile('\s*{\s*').sub(' { ',data)
data=re.compile('\s*;\s*').sub('; ',data)
data=re.compile('\s*}\s*').sub(' }\n',data)
data=re.compile('[ ]+').sub(' ',data)
print data