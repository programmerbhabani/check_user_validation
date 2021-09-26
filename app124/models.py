from django.db import models

state_choices = (
    ("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),
    ("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),
    ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
    ("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
    ("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),
    ("National Capital Territory of Delhi","National Capital Territory of Delhi"),
    ("Puducherry","Puducherry"))


# Create your models here.
class UserModel(models.Model):
    name=models.CharField(max_length=50)
    dob=models.DateField(auto_now_add=False,auto_now=False)
    contact_no=models.IntegerField(unique=True)
    gender=models.CharField(max_length=20)
    pin=models.PositiveIntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(choices=state_choices, max_length=255)
    gmail=models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    profile_image=models.ImageField(upload_to='my_image/',blank=True,null=True)

