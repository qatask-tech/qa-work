from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Make sure this line is here
    path('', include('system.urls')),  # Include URLs for your app (system)
    # If there are other apps, add them here (like 'numbercheck', 'marksheet', etc.)
    path('numbercheck/', include('numbercheck.urls')),  # Add your app's URLs
    path('marksheet/', include('marksheet.urls')),
    path('contact/', include('contact.urls')),
    path('news/', include('news.urls')),
]
