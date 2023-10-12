from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import Jobseeker
from .forms import JobForm
import re

# Create your views here.
def index(request):
    userdata = Jobseeker.objects.filter(status="added")
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
        print(firstName,lastName,code,phone,email,dob,gender,role,experience,addressLine1,addressLine2,city,state,zipCode,country)
        
        def validateFirstName():
            if (firstName == None) or (firstName == "") or (len(firstName) < 3) or (len(firstName) > 25):
                return False
            else:
                return True
            
        def validateLastName():
            if (lastName == None) or (lastName == "") or (len(lastName) < 3) or (len(lastName) > 25):
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
            if (gender != "male" and gender != "female" and gender != "other"):
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
            if(country == "INDIA" or country == "US"):
                return True
            else:
                return False
        def validateCode():
            if(code == "+91" or code == "+1"):
                return True
            else:
                return False
        # def validateDate():
        #     regexDate = r'^\d{4}-\d{2}-\d{2}$'
        #     matchDate = re.match(dob,)


        if (validateFirstName() and validateLastName() and validateCountry() and validateCode() and validateEmail() and validateGender() and validateExperience() and validateRole() and validateZipCode() and validatePhone() and validateAllAddress() == True ):         
            insertqry = Jobseeker.objects.create(first_name = firstName, last_name = lastName, code = code, phone = phone, email = email, dob = dob, gender = gender, job_role = role, experience = experience, address_line_one = addressLine1, address_line_two = addressLine2, city = city, state = state, zip_code = zipCode, country = country, status = "added")   
            insertqry.save()
            return HttpResponseRedirect("/min/index")
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
            if (lastName == None) or (lastName == "") or (len(lastName) < 3) or (len(lastName) > 25):
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
            if (gender != "male" and gender != "female" and gender != "other"):
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
            if(country == "INDIA" or country == "US"):
                return True
            else:
                return False
        def validateCode():
            if(code == "+91" or code == "+1"):
                return True
            else:
                return False


        if (validateFirstName() and validateLastName() and validateCountry() and validateCode() and validateEmail() and validateGender() and validateExperience() and validateRole() and validateZipCode() and validatePhone() and validateAllAddress() == True ):         
            updateqry = Jobseeker.objects.get(id=userid)     
            updateqry.first_name = firstName
            updateqry.last_name = lastName
            updateqry.code = code
            updateqry.phone = phone
            updateqry.email = email
            updateqry.dob = dob
            updateqry.job_role = role
            updateqry.experience = experience
            updateqry.address_line_one = addressLine1
            updateqry.address_line_two = addressLine2
            updateqry.city = city
            updateqry.state = state
            updateqry.zip_code = zipCode
            updateqry.country = country
            updateqry.save()
            return HttpResponseRedirect("/min/index")
    
    return render(request,"updateform.html",{"data":userdata})
