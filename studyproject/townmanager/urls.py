from django.conf import settings
# from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'townmanager'
urlpatterns = [
    path('', views.townmanager_index, name = 'townmanager_index'),
    path('myPage', views.myPage, name = 'myPage'),
    path('job_intro', views.job_intro, name = 'job_intro'),
    path('login', views.login, name = 'login'),

    path('index', views.index, name='index'),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),

]