from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salez_app/', include('salez_app.urls')),  # Ensure this path is correct
]
