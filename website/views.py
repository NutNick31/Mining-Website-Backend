from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import *
from .serializers import *


@csrf_exempt
def faculty_members_api(request):
    if request.method == 'GET':
        list = faculty_member.objects.all()
        serialized_list = faculty_members_serializer(list, many=True)
        return JsonResponse(serialized_list.data, safe=False)
    

@csrf_exempt
def staff_members_api(request):
    if request.method == 'GET':
        list = staff_member.objects.all()
        serialized_list = staff_members_serializer(list, many=True)
        return JsonResponse(serialized_list.data, safe=False) 
    
@csrf_exempt
def research_scholars_api(request):
    if request.method == 'GET':
        list = research_scholar.objects.all()
        serialized_list = research_scholars_serializer(list, many=True)
        return JsonResponse(serialized_list.data, safe=False) 
    

@csrf_exempt
def research_area_api(request):
    if request.method == 'GET':
        list = research_area.objects.all()
        serialized_list = research_area_serializer(list, many=True)
        return JsonResponse(serialized_list.data, safe=False)
    

@csrf_exempt
def education_api(request):
    if request.method == 'GET':
        list = education.objects.all()
        serialized_list = education_serializer(list, many=True)
        return JsonResponse(serialized_list.data, safe=False)
    

@csrf_exempt
def society_api(request):
    if request.method == 'GET':
        list = society.objects.all()
        serialized_list = society_serializer(list, many=True)
        return JsonResponse(serialized_list.data, safe=False)
    

@csrf_exempt
def event_api(request):
    if request.method == 'GET':
        list = event.objects.all()
        serialized_list = event_serializer(list, many=True)
        return JsonResponse(serialized_list.data, safe=False)