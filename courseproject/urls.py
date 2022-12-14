"""courseproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from django.views.static import serve

from courseapp.views import login_user, logout_user, register, home, intro, homework, quizzes, content, intro_to_java

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('login/', login_user, name="login_user"),
                  path('logout/', logout_user, name="logout_user"),
                  path('register/', register, name="register"),
                  path('', home, name="home"),
                  path('intro/', intro, name="intro"),
                  path('intro-to-java/', intro_to_java, name="intro_to_java"),
                  path('homework/', homework, name="homework"),
                  path('quizzes/', quizzes, name="quizzes"),
                  path('content/', content, name="content"),

                  # url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  # url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
              ] + static('media/', document_root=settings.MEDIA_ROOT)
