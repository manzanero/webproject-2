"""
URL configuration for webproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

import testapp.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('get_example', testapp.views.get_example),
    path('post_example', testapp.views.post_example),
    path('gallery', testapp.views.gallery),
    path('gallery/<photo>', testapp.views.gallery_photo),
    path('calculadora/<numero1>/<operacion>/<numero2>', testapp.views.calculadora),
]
