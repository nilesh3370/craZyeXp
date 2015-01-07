code="""
#include<stdio.h>
int main(){
int n,i;
char data[100];
scanf("%d",&n);
printf("%d",n);
for (i = 0;i<n;i++)
  {
    gets(data);
    puts(data);
  }
return 0;
}
"""

input="""
5
dipankar
dipankar123 
"""

import subprocess
import os
class Execute:
  def __init__(self,ftime=None):
    os.system('mkdir ~/tmp')
    if ftime:      
      os.system('wget wget https://gist.githubusercontent.com/netj/526585/raw/9044a9972fd71d215ba034a38174960c1c9079ad/memusg')
      os.system('chmod 777 memusg')
  
  def save(self,name='hello', code="",input=""):
    with open (''+name+'.c', 'w+') as f: f.write (code)
    with open (''+name+'.in', 'w+') as f: f.write (input)
    self.input =input
    
  def compile(self,name='hello'):
    print 'Compiling program ...'
    cmd = "gcc -o %s %s.c" %(name,name)
    print "Launching command: " + cmd  
    sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    out= sp.communicate()
    res={}; res['stdout'] =  out[0]; res['stderr'] =  out[1]
    if 'error:' in res['stderr']:
      res['msg']='syntax Error : Not able to compile'
    elif 'warning:' in res['stderr']:
      res['msg']='Compiled succesully with warning'
    else:
      res['msg']='Compiled succesully.'
    print '*'*50
    print res
    print '*'*50
    return res
    
  def run(self,name=None):
    print '>>> Running program ...'
    cmd = "%s" %(name)
    print "Launching command: " + cmd  
    sp = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    out= sp.communicate(input=self.input)
    res={}; res['stdout'] =  out[0]; res['stderr'] =  out[1]
    print '*'*50
    print res
    print '*'*50
    return res
  def testperf(self,name=None):
    print 'Testing Performance...'
    cmd = "time %s" %(name)
    print "Launching command: " + cmd  
    sp = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    out= sp.communicate(input=self.input)
    res={}; res['time'] =  out[1];
    sp.poll()
    
    cmd = "./memusg %s" %(name)
    print "Launching command: " + cmd  
    sp = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    out= sp.communicate(input=self.input)
    res['space'] =  out[1]    
    sp.poll()
    
    print '*'*50
    print res
    print '*'*50
    return res

  

