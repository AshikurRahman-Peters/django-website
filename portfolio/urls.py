from django.urls import include
from django.contrib import admin
from django.urls import path
from.import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('employee/', include('employee.urls')),]

