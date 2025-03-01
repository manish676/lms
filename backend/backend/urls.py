from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('status/', include('status.urls')),  # Use 'status1' instead of 'status'
]
