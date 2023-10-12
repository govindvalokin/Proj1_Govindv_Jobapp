from django.db import models

# Create your models here.
class Jobseeker(models.Model):
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    country_code = [
                    ('+91','+91'),
                    ('+1','+1')
                    ]
    code = models.CharField(max_length=3,null=False, choices = country_code)
    phone = models.BigIntegerField(null=False)
    email = models.EmailField(null=False)
    dob = models.DateField(null=False)
    genderchoice= [
        ('male','male'),
        ('female','female'),
        ('other','other')
    ]
    gender = models.CharField(null=False, max_length=6, choices = genderchoice)
    jobchoice = [
        ('developer','developer'),
        ('testing','testing'),
        ('devops','devops'),
        ('operations','operations'),
        ('accounting','accounting')
    ]
    job_role = models.CharField(null=False, max_length=10, choices= jobchoice)
    experiencelevel = [
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5+','5+')

    ]
    experience = models.CharField(max_length=2, null=False, choices=experiencelevel)
    address_line_one= models.CharField(null=False, max_length=35)
    address_line_two= models.CharField(null=False, max_length=35)
    city = models.CharField(null=False, max_length=20)
    state = models.CharField(null=False, max_length=20)
    zip_code = models.IntegerField(null=False)
    # countrychoices = [
    #     ('india','india'),
    #     ('us','us')
    # ]
    country = models.CharField(null=False, max_length=5)
    status = models.CharField(null=False, default="test", max_length=10)

    def __str__(self):
        return self.first_name