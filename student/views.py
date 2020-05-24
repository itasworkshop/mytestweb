from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Student
from django.shortcuts import get_list_or_404
# Create your views here.

'''
def index(request):
    return HttpResponse("Hello welcome to my first websie page.")
    

def index(request):
    list_dept = Department.objects.order_by('dt_name')[:5]
    output = ','.join([d.dt_name for d in list_dept])
    print(output)
    return HttpResponse(output)
'''

def index(request):
    list_dept = Department.objects.order_by('dt_name')[:5]
    context = {
        'list_dept':list_dept
    }
    print(context)
    return render(request,'student/index.html',context)

def stlist(request,dept_id):
    print(dept_id)
    st_list = get_list_or_404(Student,st_did=dept_id)
    print(st_list)
    return render(request,'student/stlist.html',{'stlist':st_list})

def hello(request):
    return HttpResponse("Hello from hello index.")

def list_department(request):
    pass