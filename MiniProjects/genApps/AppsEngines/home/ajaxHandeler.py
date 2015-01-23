###########################################
## Author : Dipankar Dutta
## Title :
## Description:
## Function: Contains XHR Request handlers- hence it;s a Ajax Request Handlers
###########################################
import json
from bson import json_util
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from CommonLib import utils
from django.shortcuts import render, render_to_response

######################3  Start Feedback Operation using Ajax #########################
from .api import FeedbackManager
@csrf_exempt
def ajax_feedback(request):
    import pdb
    #pdb.set_trace()
    res=None
    if request.method == 'GET':
        page=request.GET.get('page',None)
        limit=request.GET.get('limit',None)

        name=request.GET.get('name',None)
        email=request.GET.get('email',None)
        mobile=request.GET.get('mobile',None)
        res=FeedbackManager.getAllFeedbackWithFilter(name=name, email=email,mobile=mobile,page=page,limit=limit)

    elif request.method == 'POST':
        name=request.POST.get('name',None)
        email=request.POST.get('email',None)
        mobile=request.POST.get('mobile',None)
        feedback=request.POST.get('feedback',None)
        ipaddress  = utils.get_client_ip(request)
        res=FeedbackManager.createFeedback(name=name,email=email,mobile=mobile,feedback=feedback,ipaddress = ipaddress )
    elif request.method ==  'DELETE':
        #Pass No Delete
        pass
    return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')

######################  End Address Operation ############################

###################### TODO Clean Code logic #########################
from AppsEngines.cleanCode.api import *
@csrf_exempt
def ajax_cleancode_compile(request):
    res= {}
    if request.method == 'POST':
        lang=request.POST.get('lang',None)
        name=request.POST.get('name',None)
        code=request.POST.get('code',None)
        input=request.POST.get('input',None)
        # Logic  Here ..
        from CommonLib.codecompile.executeLib import Execute
        ex = Execute(lang,name,code,input)
        ex.save(name,code,input)
        res = ex.compile(name)
        #ex.run(name)
        #ex.testperf(name)
    return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
@csrf_exempt
def ajax_cleancode_run(request):
    res= {}
    if request.method == 'POST':
        lang=request.POST.get('lang',None)
        name=request.POST.get('name',None)
        code=request.POST.get('code',None)
        input=request.POST.get('input',None)
        # Logic  Here ..
        from CommonLib.codecompile.executeLib import Execute
        ex = Execute(lang,name,code,input)
        res = ex.run(name)
        #ex.run(name)
        #ex.testperf(name)
    return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
@csrf_exempt
def ajax_cleancode_perf(request):
    res= {}
    if request.method == 'POST':
        lang=request.POST.get('lang',None)
        name=request.POST.get('name',None)
        code=request.POST.get('code',None)
        input=request.POST.get('input',None)
        # Logic  Here ..
        from CommonLib.codecompile.executeLib import Execute
        ex = Execute(lang,name,code,input)
        res = ex.testperf(name)
    return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
    
    
@csrf_exempt
def download_file(request,id):
    res= {}
    if request.method == 'GET':
        res= CodeManager.getCode(id)        
        if res['res']:
          #build File...
          if res['res']['language'].lower() == 'py':
            file=''
            file +="\n'''\n"+"*"*50+"\n"+" Program Details " +"\n"+"*"*50
            file +="\n Name:"+res['res']['name']
            file +="\n Description:"+res['res']['short_desc']+"\n"+"*"*50+"\n'''\n"
            if res['res']['main']:
              file +="\n#"+"*"*50+"\n"+"Driver Code "+"\n"+"*"*50+"#\n"
              file +=res['res']['main']
            if res['res']['func']:
              file +="\n#"+"*"*50+"\n"+"Function Code "+"\n"+"*"*50+"#\n"
              file +=res['res']['func']
          else:
            file=''
            file +="\n/*"+"*"*50+"\n"+" Program Details " +"\n"+"*"*50
            file +="\n Name:"+res['res']['name']
            file +="\n Description:"+res['res']['short_desc']+"\n"+"*"*50+"*/\n"
            if res['res']['main']:
              file +="\n/*"+"*"*50+"\n"+"Driver Code "+"\n"+"*"*50+"*/\n"
              file +=res['res']['main']
            if res['res']['func']:
              file +="\n/*"+"*"*50+"\n"+"Function Code "+"\n"+"*"*50+"*/\n"
              file +=res['res']['func']
          
          from django.core.servers.basehttp import FileWrapper
          # generate the file
          if res['res']['language'] =='C':
            response = HttpResponse(file, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename=%s.c' %(res['res']['name'])
          
          response['Content-Length'] = len(file)
          return response           
        else:
          return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
@csrf_exempt
def view_file(request,id):
    res= {}
    if request.method == 'GET':
        res= CodeManager.getCode(id)        
        if res['res']:
          return render_to_response('cleanCode_view.html',res['res']);          
        else:
          return HttpResponse(json.dumps(res,default=json_util.default),content_type = 'application/json')
          
######################  End Address Operation ############################

