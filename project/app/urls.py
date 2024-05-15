from . import views
from django.urls import path

urlpatterns = [
    path('func1',views.func1),
    path('company/<int:salary>/<int:service>',views.company),
    path('kseb/<int:units>',views.kseb),
    path('weekday/<int:day>',views.weekday),
    path('monuments/<city>',views.monumnets),
    path('divisible/<int:number>',views.divisible),
    path('bike/<int:cost>',views.bike),
    path('index',views.index),
    path('second',views.second),
    path('third',views.third),
    path('form',views.form),
    path('display',views.display),
    path('student',views.student),
    path('add',views.add),
    path('display_st',views.display_st),
    path('update/<i>',views.update),
    path('delete/<i>',views.delete),
    path('form2',views.form2),
    path('display1',views.display1),
    path('update1/<pk>',views.update1),
    path('delete1/<pk>',views.delete1),
    path('user_form_dis',views.user_form_dis),
    path('m_form',views.m_form),
    path('upld',views.upld),
    path('display_fileupload',views.display_fileupload),
    
]