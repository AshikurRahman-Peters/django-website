from django.urls import include
from django.contrib import admin
from django.urls import path
from.import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.service, name='service'),
    path('employee/', include('employee.urls')),]

