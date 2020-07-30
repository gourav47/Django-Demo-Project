from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/employees.html',data)
    return(res)
def greetings(request):
    s="<h1>Hello welcome to the first view of testapp</h1>"
    return HttpResponse(s)
def showContact(request):
    s="<h1>Contact Page</h1>"
    s+="<p>Website: mysirg.com</p>"
    s+="<p>Mobile: 9009009001</p>"
    s+="<p>Email: something@gmail.com</p>"
    return HttpResponse(s)
def about(request):
    msg="This is an about page"
    return render(request,'testapp/about.html',{'msg':msg})
