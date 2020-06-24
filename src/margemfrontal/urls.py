"""margemfrontal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import index, oportunidades, houses, construction, security, food, contact
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('oportunidades/',oportunidades, name='oportunidades'),
    path('houses/',houses, name='houses'),
    path('construction/',construction, name='construction'),
    path('security/',security, name='security'),
    path('food/',food, name='food'),
    path('contact/',contact, name='contact'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

