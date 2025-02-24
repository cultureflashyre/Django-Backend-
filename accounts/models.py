from django.db import models

class CollegeUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    university_college = models.CharField(max_length=100)  # Stores the selected university/college name
    university_college_id = models.CharField(max_length=50)
    email = models.EmailField(unique=True)  # Ensures email is unique
    password = models.CharField(max_length=128)  # Will store the hashed password

    def __str__(self):
        return self.email