"""
URL configuration for libraryWebapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from librarysystem import views
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_view,name='login_view'),
    path('login_view',views.login_view,name='login_view'),
    path('register',views.register,name='register'),
    path('index',views.index,name='index'),
    path('addbooks',views.addbooks,name='addbooks'),
    path('search', views.search, name='search'),
    path('globalLib',views.globalLib,name='globalLib'),
    path('globalLib/<int:book_id>/delete/', views.globalLib, name='delete_book'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

