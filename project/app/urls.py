from . import views
from django.urls import path

urlpatterns = [
    path('/func1',views.func1),
    path('/company/<int:salary>/<int:service>',views.company),
    path('/kseb/<int:units>',views.kseb),
    path('/weekday/<int:day>',views.weekday),
    path('/monuments/<city>',views.monumnets),
    path('/divisible/<int:number>',views.divisible),
    path('/bike/<int:cost>',views.bike)
]