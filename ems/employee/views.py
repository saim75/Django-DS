from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime


# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        eid = request.POST.get('eid')
        ename = request.POST.get('ename')
        eemail = request.POST.get('eemail')
        econtact = request.POST.get('econtact')
        salary = request.POST.get('salary')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')
        emp = Employee(eid=eid,ename=ename,eemail=eemail,econtact=econtact,salary=salary,dept=dept,role=role,phone=phone,hire_date=datetime.now())
        emp.save()
        return render(request,'index.html')
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse('Invalid Request')
    
def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
            emp = Employee.objects.get(id=emp_id)
            emp.delete()
            return HttpResponse('Employee Deleted')
        except:
            return HttpResponse('Employee Not Found')
    
    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        eid = request.POST['eid']
        ename = request.POST['ename']
        eemail = request.POST['eemail']
        emps = Employee.objects.all()
        if ename:
            emps = emps.filter(ename__icontains=ename)
        if eid:
            emps = emps.filter(eid__icontains=eid)
        if eemail:
            emps = emps.filter(eemail__icontains=eemail)
        
        context = {'emps':emps}
        return render(request,'filter.html',context)
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('Invalid Request')
    
