from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def func1(request):
    return HttpResponse("<h1>Welcome</h1>")
def company(request,salary,service):
    if service>5:
        return HttpResponse("your bonus is :{}".format(0.05*salary))
    else:
        return HttpResponse("Sorry you have no bonus this year")
def kseb(request,units):
    if units<=100:
        return HttpResponse("No charges for you ")
    elif units<=200:
        units=units-100
        bill_amount=units*5
        return HttpResponse("Your bill amount is :{}".format(bill_amount))
    elif units>200:
        units=units=200
        bill_amount=(units*10)+500
        return HttpResponse("Your bill amount is :{}".format(bill_amount))
    else:
        return HttpResponse("Enter a valid number of units")
def weekday(request,day):
    if day==1:
        return HttpResponse("Sunday")
    elif day==2:
        return HttpResponse("monday")
    elif day==3:
        return HttpResponse("Tuesday")
    elif day==4:
        return HttpResponse("wednesday")
    elif day==5:
        return HttpResponse("thursday")
    elif day==6:
        return HttpResponse("Friday")
    elif day==7:
        return HttpResponse("saturday")
    else:
        return HttpResponse("Enter a valid number")
def monumnets(request,city):
    if city=="Delhi":
        return HttpResponse("Monument in Delhi is Red Frot")
    elif city=="Agra":
        return HttpResponse("Monument in Agra is Tajmahal")
    elif city=="Jaipur":
        return HttpResponse("Monument in Jaipur is JalMahal")
    else:
        print("Enter a valid City")
def divisible(request,number):
    lastdigit=number%10
    if lastdigit%3==0:
        return HttpResponse("Last digit of the given number is divisible by 3")
    else:
        return HttpResponse("Last digit of the given number is not divisible by 3")
def bike(request,cost):
    if cost>1000000:
        road_tax=0.15*cost
    elif cost>50000 and cost<=1000000:
        road_tax=0.10*cost
    elif cost<=50000:
        road_tax=0.05*cost
    else:
        return HttpResponse("Go and buy a bike pls")
    return HttpResponse("You need to pay {} as road tax".format(road_tax))


def index(request,firstno,secondno,thirdno):
    data="welcome all to my homepage"
    if firstno<secondno:
        if secondno<thirdno:
            thirdno=str(thirdno)+"Largest"
        else:
            secondno=str(secondno)+"Largest"
    else:
        if firstno<thirdno:
            thirdno=str(thirdno)+"Largest"
        else:
            firstno=str(firstno)+"Largest"
    return render(request,'index.html',{'data':data,'first':firstno,'second':secondno,'third':thirdno})
def second(request):
    data=['Vysakh','Salman','Nihal','Muneeb']
    data1={'name':'Amal','age':21}
    return render(request,'second.html',{"data":data,'data1':data1})
def third(request):
    data=[{'name':'Amal','age':21},
          {'name':'Shibili','age':21},
          {'name':'Reneen','age':21},
          {'name':'Rajesh','age':50},
          {'name':'Ramesh','age':48},
          {'name':'Rathesh','age':46}]
    data1=[]
    data2=[]
    for i in data:
        if i['age']>=30:
            data1.append(i)
        else:
            data2.append(i)
    return render(request,'third.html',{'data1':data1,'data2':data2})
data=[]
def form(request):
    if request.method=='POST':
        id=request.POST['id']
        name=request.POST['name']
        age=request.POST['age']
        place=request.POST['place']
        data.append({'id':id,'name':name,'age':age,'place':place})
        print(data)
        return redirect(display)
    else:
        return render(request,'form.html')
def display(request):
    return render(request,'display.html',{'data':data})
student1s=[]
def student1(request):
    return render(request,'student1.html')
def add(request):
    if request.method=='POST':
        id=request.POST['id']
        name=request.POST['name']
        age=request.POST['age']
        place=request.POST['place']
        course=request.POST['course']
        student1s.append({'id':id,'name':name,'age':age,'place':place,'course':course})
        return redirect(student1)
    else:
        return render(request,'add.html')
def display_st(request):
    return render(request,'display_st.html',{'student1s':student1s})
def update(request,i):
    for user in student1s:
        if user['id']==i:
            std=user
    if request.method=='POST':
        id=request.POST['id']
        name=request.POST['name']
        age=request.POST['age']
        place=request.POST['place']
        course=request.POST['course']
        data=student1s.index(std)
        student1s[data]={'id':id,'name':name,'age':age,'place':place,'course':course}
        return redirect(display_st)
    else:
        return render(request,'update.html',{'user':std})
    
def delete(request,i):
    for user in student1s:
        if user['id']==i:
                student1s.remove(user)
                return redirect(display_st)
def form2(request):
    if request.method=='POST':
        id=request.POST['id']
        name=request.POST['name']
        age=request.POST['age']
        data=student.objects.create(roll=id,name=name,age=age)
        data.save()
        return redirect(display)
    else:
        return render(request,'form2.html')
        