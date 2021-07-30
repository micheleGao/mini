from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    # localhost:8000/student
    path('students/', views.StudentList.as_view(), name='student_list'),
    #localhost:8000/student/ followed by a number would route it to the view being defined
    path('students/<int:pk>', views.StudentDetail.as_view(), name='student_detail'),
    #localhost:8000/project
    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('projects/<int:pk>', views.ProjectDetail.as_view(), name='project_detail')
]