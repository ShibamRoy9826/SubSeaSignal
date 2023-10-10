from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from home import views

urlpatterns = [
    path('',views.index, name="Welcome"),
    path('result',views.User,name='Result')
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
