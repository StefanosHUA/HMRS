from django.urls import include, path
from . import views
from django.conf import settings

urlpatterns = [
    #GET
    path('', views.getUser),
    path('getUser/', views.getUser),
    path('getSpecType', views.getSpecType),
    path('getExp/', views.getExperience),
    path('getPreviousGrades', views.getPreviousGrades),
    path('getPreviousSalary', views.getPrevious_Salary_Class),
    path('getDepProfiles', views.getDEP),
    path('getDPprofiles', views.getDP),
    path('getEmpType', views.getEmpType),

    #POST
    # path('postTitle', views.postTitle),
    path('postUser', views.postUser),
    # path('postWR/', views.postWR),

    #take 2

    

]