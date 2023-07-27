
# api/urls.py
# staff_attendance_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('staff/login/', views.staff_login),
    path('staff/checkin/', views.staff_checkin),
    path('staff/checkout/', views.staff_checkout),
    path('attendance/', views.view_attendance),
]

