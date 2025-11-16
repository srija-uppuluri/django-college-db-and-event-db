from django.http import JsonResponse
from django.shortcuts import render
from college.models import Student
#from college.models import Subject
#from college.models import Enrollments
from eventdb.models import Hosts
from eventdb.models import Events
import requests

API_key=''
'''curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: AIzaSyAF-E-qxpMFYmCPoLP1j9LhEXOc5WDm3C8' \
  -X POST \
  -d 'curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: AIzaSyAF-E-qxpMFYmCPoLP1j9LhEXOc5WDm3C8' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'''

def chatbot(request):
    query=request.GET.get('query',"")
    
    payload={
    "contents": [
      {
        "parts": [
          {
            "text": query
          }
        ]
      }
    ]
  }
    
    params={
        'key':API_key
    }
    result=requests.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",params=params,json=payload)
    response=JsonResponse(result.json())
    try:
        answer = response["candidates"][0]["content"]["parts"][0]["text"]
    except:
        answer = "⚠ Gemini could not generate a response."

    return JsonResponse({"answer": answer})

def chatbot_page(request):
    return render(request, "chatbot.html")

students_list=[]
professors_list=[]
facilities_list=[]

def add_students(request):
    name=request.GET.get('name')
    roll=request.GET.get('roll')

    if name and roll:
        students_list.append({'name':name,'roll':roll})
        return JsonResponse({'message':'student added successfully'})
    else:
        return JsonResponse({'error':'provide correct details'})

def view_students(request):
    students_list=list(Student.objects.values())
    return JsonResponse({'students':students_list})


def add_professors(request):
    name=request.GET.get('name')
    sub=request.GET.get('sub')

    if name and sub:  
        professors_list.append({'name':name,'sub':sub})
        return JsonResponse({'message':'professor added successfully'})
    else:
        return JsonResponse({'error':'provide correct details'})

def view_professors(request):
    return JsonResponse({'professor':professors_list})


def add_facilities(request):
    facility=request.GET.get('facility')

    if facility:
        facilities_list.append({'facility':facility})
        return JsonResponse({'message':'facility added successfully'})
    else:
        return JsonResponse({'error':'provide correct details'})

def view_facilities(request):
    return JsonResponse({'facility ':facilities_list})
    

def fetch_events(request):
    result=Events.objects.all().values()
    return render(request,'event.html',context={'events':list(result)})
    #return JsonResponse(list(result),safe=False)

def add_event(request):
    name_value=request.GET.get('name')
    price_value=request.GET.get('price')
    desc_value=request.GET.get('desc')
    limit_value=request.GET.get('limit')

    Events.objects.create(
       name=name_value,
       price=price_value,
       limit=limit_value, 
       desc=desc_value,
    )
    return JsonResponse({'message':'event added'})

def update_event(request):
    name_value=request.GET.get('name')
    price_value=request.GET.get('price')
    desc_value=request.GET.get('desc')
    limit_value=request.GET.get('limit')

    events=Events.objects.get(name=name_value)
    events.price=price_value
    events.desc=desc_value
    events.limit=limit_value

    events.save()
    return JsonResponse({'message':'event updated'})

def delete_event(request):
    name_value=request.GET.get('name')
    
    events=Events.objects.get(name=name_value)

    events.delete()
    return JsonResponse({'message':'event deleted'})


def fetch_hosts(request):
    result=Hosts.objects.all().values()
    return JsonResponse(list(result),safe=False)