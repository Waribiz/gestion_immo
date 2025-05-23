"""
URL configuration for api_gest_immo project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
# On dit à Django : "Quand une URL commence par /api/, regarde dans les apps pour savoir quoi faire."
  # ex login :
  # http://127.0.0.1:8000/api/users/login
  #on envoit au format json le username, 

    path('api/users/', include('users.urls')), 
    path('api/properties/', include('properties.urls')),
    path('api/rentals/', include('rentals.urls')),

]
