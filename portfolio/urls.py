from django.urls import include
from django.contrib import admin
from django.urls import path
from.import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('abahaiahasdhskdjshd/', views.about, name='about'),
    path('contact/', views.contact),
    path('employee/', include('employee.urls')),]

