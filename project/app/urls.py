from . import views
from django.urls import path

urlpatterns = [
    path('/func1',views.func1),
    path('/func2/<int:data>',views.func2)
]