#test.tci
import pdb
import sys
import urllib
import subprocess
url = None
flag =0
c_success =0
c_fail =0
fname=sys.argv[1] #raw_input('Enter the text file name:')
with open(fname) as f:
    for line in f:
      if not line.strip():
        continue
      if line[0] == '#':
        continue
      if flag == 0:
        url = line.strip()
      else:
        print '-'*50
        print 'Executing case#',flag,'::',line
        #==================
        line =[l.strip() for l in line.split('|')]
        
        cmd = 'curl -H "Accept: application/json"  -X '+line[0] 
        if urllib.urlencode(eval(line[2])):
         cmd+= '  -d  "'+urllib.urlencode(eval(line[2]))+'"'
        cmd+='  '+url+line[1]
        print cmd
        result = subprocess.check_output(cmd, shell=True)
        if line[3] in result:
          print 'TEST CASE SUCCED....'
          c_success+=1
        else:
          c_fail+=1
          print 'TEST CASE FAILED....'
          print result
        #==================
      flag = flag+1

print '='*50
print 'SUMMARY'
print 'TOATAL EXECUTED:',flag-1
print 'SUCCESS:',c_success
print 'FAILED:',c_fail

print '='*50
