"""
URL configuration for management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_students',views.add_students,name='students'),
    path('view_students',views.view_students,name='students'),
    path('add_professors',views.add_professors,name='professors'),
    path('view_professors',views.view_professors,name='professors'),
    path('add_facilities',views.add_facilities,name='facilities'),
    path('view_facilities',views.view_facilities,name='facilities'),
    path('fetch_events',views.fetch_events,name='events'),
    path('fetch_hosts',views.fetch_hosts,name='hosts'),
    path('add_event',views.add_event,name='event'),
    path('update_event',views.update_event,name='event'),
    path('delete_event',views.delete_event,name='event'),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('chatbot_page/',views.chatbot_page,name='chatbot'),
]
