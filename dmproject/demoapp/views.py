from django . http import HttpResponse
from django.shortcuts import render
from . models import Place,Name

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Name.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})




















# def demo(request):
#     return render(request,"home.html")
# def addition(request):
#     x = int( request.GET['num1'])
#     y = int( request.GET['num2'])
#     res = x + y
#     res1 = x - y
#     res2 = x * y
#     res3 = x // y
#     return render(request,"result.html",{'result':res,'result1':res1,'result2':res2,'result3':res3})

# def subtraction(request):
#     x = int( request.GET['num1'])
#     y = int( request.GET['num2'])
#     res1 = x - y
#     return render(request,"result.html",{'result1':res1})
# def multiplication(request):
#     x = int( request.GET['num1'])
#     y = int( request.GET['num2'])
#     res = x * y
#     return render(request,"result.html",{'result':res})
# def division(request):
#     x = int( request.GET['num1'])
#     y = int( request.GET['num2'])
#     res = x / y
#     return render(request,"result.html",{'result':res})


# def home(request):
#     return HttpResponse("home")
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("contact")
# def details(request):
#     return render(request,"home.html")
# def thanks(request):
#     return HttpResponse("thanks")

# def addition(request):
#     x = int( request.GET['num1'])
#     y = int( request.GET['num2'])
#     res = x + y
#     res1 = x - y
#     res2 = x * y
#     res3 = x / y
#     return render(request,"result.html",{'result':res,'result':res1,'result':res2,'result':res3})


# def demo(request):
#     return HttpResponse("hello world")