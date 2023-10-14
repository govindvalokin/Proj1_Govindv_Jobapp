from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import Jobseeker
from .forms import JobForm
from datetime import date
import re
import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    userdata = Jobseeker.objects.filter(status="added").order_by('-id')
    return render(request,"listing_page.html",{"data":userdata})

def newform(request):
    if request.POST:
        firstName = request.POST.get("firstname")
        lastName = request.POST.get("lastname")
        code = request.POST.get("code")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        role = request.POST.get("role")
        experience = request.POST.get("experience")
        addressLine1 = request.POST.get("addressline1")
        addressLine2 = request.POST.get("addressline2")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zipCode = request.POST.get("zipcode")
        country = request.POST.get("country")
        print(firstName, lastName,code,phone,email,dob,gender,role,experience,addressLine1,addressLine2,city,state,zipCode,country)
        
        def validateFirstName():
            if (firstName == None) or (firstName == "") or (len(firstName) < 3) or (len(firstName) > 25):
                return False
            else:
                return True
            
        def validateLastName():
            if (lastName == None) or (lastName == "") or (len(lastName) < 1) or (len(lastName) > 25):
                return False
            else:
                return True
        def validatePhone():
            regexmob = r'^\d{10}$'
            matchvalue = re.match(regexmob,phone)

            if (phone == "" or matchvalue == None):
                return False
            else:
                return True
        def validateEmail():
            regexemail = r'^[a-zA-Z0-9.!#$%&\'*+/-/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
            matchvalue2 = re.match(regexemail,email)
            if (email == "" or matchvalue2 is None):
                return False
            else:
                return True
        def validateAllAddress():
            if (addressLine1 == "" or addressLine1 == None or addressLine2 == "" or addressLine2 == None or city == "" or city == None or state == "" or state == None):
                return False
            else:
                return True
        def validateZipCode():
            zipCodeValue = int(zipCode)
            if (zipCode == "" or zipCode == None or len(zipCode) != 6):
                return False
            if (type(zipCodeValue) != int):
                return False
            else:
                return True
        def validateGender():
            if (gender != "Male" and gender != "Female" and gender != "Other"):
                return False
            else:
                return True
        def validateRole():
            if (role == "Developer" or role == "Testing" or role == "Devops" or role == "Operations" or role == "Accounting"):
                return True
            else:
                return False
        def validateExperience():
            if (experience == "0" or experience == "1" or experience == "2" or experience == "3" or experience == "4" or experience == "5+"):
                return True
            else:
                return False
        def validateCountry():
            if(country == "India" or country == "US"):
                return True
            else:
                return False
        def validateCode():
            if(code == "+91" or code == "+1"):
                return True
            else:
                return False
        def validateDate():
            today = date.today()
            givenDate = datetime.datetime.strptime(dob, "%Y-%m-%d").date() #converting string to date object
            
            if ((today - givenDate).total_seconds() / 31536000 >= 18):    
                return True
            else:    
                return False


        if (validateFirstName() and validateLastName() and validateCountry() and validateCode() and validateEmail() and validateGender() and validateExperience() and validateRole() and validateZipCode() and validatePhone() and validateAllAddress() and validateDate() == True ):         
            insertqry = Jobseeker.objects.create(first_name = firstName.capitalize(), last_name = lastName.capitalize(), code = code, phone = phone, email = email, dob = dob, gender = gender, job_role = role, experience = experience, address_line_one = addressLine1.capitalize(), address_line_two = addressLine2.capitalize(), city = city.capitalize(), state = state.capitalize(), zip_code = zipCode, country = country, status = "added")   
            insertqry.save()
            messages.success(request,"successfully submitted the application")
            return HttpResponseRedirect("/index")
        messages.error(request,"Something went wrong")
    return render(request,"job.html")

def dform(request):
    form = JobForm()
    return render(request,"form.html",{"form":form})
def dformstore(request):
    if request.method=="POST":
        form = JobForm(request.POST)
        if form.is_valid():
            print(form)
            # form.save()
    #     return redirect("/index")
def updateform(request):
    userid=request.GET['userid']
    userdata=Jobseeker.objects.get(id=userid)
    if request.POST:
        firstName = request.POST.get("firstname")
        lastName = request.POST.get("lastname")
        code = request.POST.get("code")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        role = request.POST.get("role")
        experience = request.POST.get("experience")
        addressLine1 = request.POST.get("addressline1")
        addressLine2 = request.POST.get("addressline2")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zipCode = request.POST.get("zipcode")
        country = request.POST.get("country")

        def validateFirstName():
            if (firstName == None) or (firstName == "") or (len(firstName) < 3) or (len(firstName) > 25):
                return False
            else:
                return True
            
        def validateLastName():
            if (lastName == None) or (lastName == "") or (len(lastName) < 1) or (len(lastName) > 25):
                return False
            else:
                return True
        def validatePhone():
            regexmob = r'^\d{10}$'
            matchvalue = re.match(regexmob,phone)

            if (phone == "" or matchvalue == None):
                return False
            else:
                return True
        def validateEmail():
            regexemail = r'^[a-zA-Z0-9.!#$%&\'*+/-/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
            matchvalue2 = re.match(regexemail,email)
            if (email == "" or matchvalue2 is None):
                return False
            else:
                return True
        def validateAllAddress():
            if (addressLine1 == "" or addressLine1 == None or addressLine2 == "" or addressLine2 == None or city == "" or city == None or state == "" or state == None):
                return False
            else:
                return True
        def validateZipCode():
            print(type(zipCode))
            zipCodeValue = int(zipCode)
            if (zipCode == "" or zipCode == None or len(zipCode) != 6):
                return False
            if (type(zipCodeValue) != int):
                return False
            else:
                return True
        def validateGender():
            if (gender != "Male" and gender != "Female" and gender != "Other"):
                return False
            else:
                return True
        def validateRole():
            if (role == "Developer" or role == "Testing" or role == "Devops" or role == "Operations" or role == "Accounting"):
                return True
            else:
                return False
        def validateExperience():
            if (experience == "0" or experience == "1" or experience == "2" or experience == "3" or experience == "4" or experience == "5+"):
                return True
            else:
                return False
        def validateCountry():
            if(country == "India" or country == "US"):
                return True
            else:
                return False
        def validateCode():
            if(code == "+91" or code == "+1"):
                return True
            else:
                return False
        
        def validateDate():
            today = date.today()
            givenDate = datetime.datetime.strptime(dob, "%Y-%m-%d").date() #converting string to date object            
            if ((today - givenDate).total_seconds() / 31536000 >= 18): #dividing using total no of seconds in an year   
                return True
            else:    
                return False


        if (validateFirstName() and validateLastName() and validateCountry() and validateCode() and validateEmail() and validateGender() and validateExperience() and validateRole() and validateZipCode() and validatePhone() and validateAllAddress() and validateDate() == True ):         
            updateqry = Jobseeker.objects.get(id=userid)     
            updateqry.first_name = firstName.capitalize()
            updateqry.last_name = lastName.capitalize()
            updateqry.code = code
            updateqry.phone = phone
            updateqry.email = email
            updateqry.dob = dob
            updateqry.job_role = role
            updateqry.experience = experience
            updateqry.address_line_one = addressLine1.capitalize()
            updateqry.address_line_two = addressLine2.capitalize()
            updateqry.city = city.capitalize()
            updateqry.state = state.capitalize()
            updateqry.zip_code = zipCode
            updateqry.country = country
            updateqry.save()
            messages.success(request,"Successfully submitted the application")
            return HttpResponseRedirect("/index")
        messages.error(request,"Something went wrong")
    return render(request,"updateform.html",{"data":userdata})

def deleteData(request):
    userid=request.GET['userid']
    Jobseeker.objects.get(id=userid).delete()
    return HttpResponseRedirect("/index")