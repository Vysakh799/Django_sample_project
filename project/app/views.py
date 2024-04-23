from django.shortcuts import render
from django.http import HttpResponse
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