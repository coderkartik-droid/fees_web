from django.contrib import admin
from .models import Student, UploadedFile

# Register your models here.

# Register the UploadedFile model with the admin site (read-only for viewing only)
# Django Admin is used only for authentication, not for file management
@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('filename', 'uploaded_at')
    
    # Order by upload date (newest first)
    ordering = ('-uploaded_at',)
    
    # Make all fields read-only - admin is for authentication only
    readonly_fields = ('filename', 'uploaded_at')
    
    # Disable adding/deleting through admin - use custom upload page instead
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

# Register the Student model with the admin site (read-only for viewing only)
# Django Admin is used only for authentication, not for student management
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('name', 'student_class', 'fathers_name', 'fees_remaining', 'uploaded_file', 'created_at')
    
    # Enable searching by name in admin
    search_fields = ('name', 'fathers_name')
    
    # Order by creation date (newest first)
    ordering = ('-created_at',)
    
    # Make all fields read-only - admin is for authentication only
    readonly_fields = ('name', 'student_class', 'fathers_name', 'fees_remaining', 'uploaded_file', 'created_at')
    
    # Disable adding/deleting through admin - use custom upload page instead
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
