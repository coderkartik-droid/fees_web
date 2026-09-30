from django.db import models

# Create your models here.

# Model to track uploaded Excel files
class UploadedFile(models.Model):
    # Original filename of the uploaded Excel file
    filename = models.CharField(max_length=255)
    
    # Timestamp when the file was uploaded
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        # String representation of the uploaded file
        return f"{self.filename} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"
    
    class Meta:
        # Order files by upload date (newest first)
        ordering = ['-uploaded_at']

# Student model to store student information
class Student(models.Model):
    # Name of the student
    name = models.CharField(max_length=100)
    
    # Class/grade of the student
    student_class = models.CharField(max_length=50)
    
    # Father's name
    fathers_name = models.CharField(max_length=100)
    
    # Remaining fees amount
    fees_remaining = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Foreign key to associate student with the uploaded file
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE, related_name='students')
    
    # Timestamp when the record was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        # String representation of the student object
        return f"{self.name} - Class {self.student_class}"
