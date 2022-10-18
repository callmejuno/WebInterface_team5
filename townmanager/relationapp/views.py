from django.http import HttpResponse
from .models import Employee, Department, Location

def employee(request) :
    emplist = Employee.objects.all()
    result = ""
    for data in emplist:
        result += str(data) + "\n"
    return HttpResponse(result, content_type="text/plain; charset=UTF-8")

def employeedepartment(request) :
    emplist = Employee.objects.all()
    result = ""
    for data in emplist:
        result += str(data.name) + "-----" +str(data.department.deptname)+ "\n"
    return HttpResponse(result, content_type="text/plain; charset=UTF-8")

def employeedepartmentlocation(request) :
    emplist = Employee.objects.all()
    result = ""
    for data in emplist:
        result += str(data.name) + "-----" + str(data.department.deptname) + "-----" + str(data.department.location.locationname)   + "\n"
    return HttpResponse(result, content_type="text/plain; charset=UTF-8")

def employeedepartmentlocationdooly(request) :
    qs = Employee.objects.filter(name = '둘리')
    data = qs[0]
    result = "<h3>둘리는 "
    result += str(data.department.deptname) + "에서 근무하고 " + str(data.department.location.locationname)   + "지역에서 일해용 ㅎ</h3>"
    return HttpResponse(result, content_type="text/html; charset=UTF-8")

def department(request) :
    deptlist = Department.objects.all()
    result = ""
    for data in deptlist:
        result += str(data) + "\n"
    return HttpResponse(result, content_type="text/plain; charset=UTF-8")

def department10employee(request) :
    target = Department.objects.get(deptid=10)
    result ="<h2>10번 부서("+target.deptname+") 에서 일하고 있는 직원들</h2>"
    source = target.employee_set
    qs = source.all()
    for data in qs :
        result += str(data) +"<br>"
    return HttpResponse(result, content_type="text/html; charset=UTF-8")

def alldepartmentemployee(request) :
    target = Department.objects.all()
    result = ""
    for data in target :
        result += "<h3>" + data.deptname + "</h3><ul>"
        source = data.employee_set
        qs = source.all()
        for data in qs :
            result += "<li>"+ data.name +"</li>"
        result += "</ul>"
    return HttpResponse(result, content_type="text/html; charset=UTF-8")

def employeelocation(request) :
    qs = Employee.objects.all()
    result = ""
    for data in qs :
        result += "<h3>" + data.name + "직원의 근무지는 " + data.department.location.locationname +"입니다요</h3>"
    return HttpResponse(result, content_type="text/html; charset=UTF-8")

def locationemployee(request) :
    target = Location.objects.all()
    for data in  target :
        try:
            qs = data.department.employee_set.all()
            for empdata in qs :
                print(empdata)
        except:
            print(data.locationname+"에서 근무하는 직원이 없습니다.")
    return HttpResponse("수행완료!! 파이참의 장고 터미널에 가서 확인해 보셔용")

def seoullocationemployee(request) :
    seoul = Location.objects.get(locationname = '서울')
    result = "<h2>서울에서 근무중인 직원들</h2><hr><ul>"
    qs = seoul.department.employee_set.all()
    for data in qs :
        result += "<li>"+data.name+"("+data.addr+")</li>"
    return HttpResponse(result, content_type="text/html; charset=UTF-8")
