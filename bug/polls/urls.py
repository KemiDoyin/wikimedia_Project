from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path('register_bug/', views.register_bug, name='register_bug'),
    path('bug/<int:bug_id>/', views.view_bug, name='view_bug'),
    path('bug_list/', views.bug_list, name='bug_list'),
]