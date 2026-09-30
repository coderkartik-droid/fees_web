from django.urls import path
from . import views

# URL patterns for the fees_app
urlpatterns = [
    # Health check endpoint (public - no authentication required)
    # Used by monitoring services like UptimeRobot to keep the service awake
    path('health/', views.health_check, name='health_check'),
    
    # URL for uploading Excel file (protected - requires staff/superuser authentication)
    path('upload/', views.upload_excel, name='upload_excel'),
    
    # URL for deleting an uploaded file (protected - requires staff/superuser authentication)
    path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
    
    # URL for displaying students with search (public access)
    path('', views.display_students, name='display_students'),
]