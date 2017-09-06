"""signup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^$',views.runner, name='index'),
    url(r'^(?P<run_code>\w+)/$', views.run, name='run'),
    url(r'^runners/(?P<user_id>\w+)/$', views.user ,name='user'),
    url(r'^(?P<run_code>\w+)/signup/$', views.signup, name='signup'),
    url(r'^(?P<run_code>\w+)/runnerinfo/$',views.runnerinfo, name='runnerinfo'), #requires login
    url(r'^api/registeruser/$',views.registeruser, name='registeruser'),


]
