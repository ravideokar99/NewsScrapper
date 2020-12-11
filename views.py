from django.shortcuts import render
import requests
import json
from django.template.loader import render_to_string
from django.http import JsonResponse





def srcapper(request):

    rrr=requests.get('http://127.0.0.1:5000/')
    data=rrr.json()
    parsed_json = json.loads(data)
    
    #json_string = json.dumps(parsed_json)
    return render(request,'news.html',{'json':parsed_json})
    
    
                
           
   
   

