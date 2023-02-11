from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    #GET
    path('', views.getUser),
    path('getUser/', views.getUser),
    path('getTitle', views.getTitle),
    path('getExp/', views.getExperience),
    path('getGrade_Types/', views.getGrade_Types),
    path('getWorkingRelation/', views.getWorking_Relation),
    path('getEmpSpeci/', views.getSpecialization),
    path('getEmpClass/', views.getEmpClass),
    path('getEmpType', views.getEmpType),

    #POST
    path('postTitle', views.postTitle),
    path('postUser', views.postUser),
    path('postWR/', views.postWR),
]