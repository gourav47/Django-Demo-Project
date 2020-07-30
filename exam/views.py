from django.shortcuts import render
from django.http import HttpResponse
def showTest(request):
    que="Who developed C Language"
    a="Ken Thompson"
    b="Denis Ritche"
    c="Bajarne Stroustrup"
    d="James Gosling"
    level="Easy"
    data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level}
    res=render(request,'exam/test.html',context=data)
    return res
def showResult(request):
    s="<h1>This is show Result Page</h1>"
    return HttpResponse(s)

# Create your views here.
