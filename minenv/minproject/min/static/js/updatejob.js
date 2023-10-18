

const form = document.getElementById("Form");
    
function validateForm(event){
    
    if (validateFirstName() && validateLastName() && validatePhone() && validateEmail() && validateJobRole() && validateAddress1() && validateAddress2() && validateCity() && validateState() && validateZipCode() && validateGender() && validateDate() && validateExperience() && validateCountry() === true){
        console.log("submitted");
        event.submit();    
    }
    else{
        event.preventDefault();
        // alert('Please fill the form completely.');
        return;
    }
}




function validateFirstName(event){
    var firstname = document.getElementById("firstName").value.trim();
    
    
        if(firstname===""){
            document.getElementById("validFirstName").innerHTML="Name can not be empty"; 
            // console.log("121");
            return false;
        }
        if((firstname.length<3) || (firstname.length>25)){
            document.getElementById("validFirstName").innerHTML="Number of letters must be between 3 and 25";
            // console.log("2222");
            return false;
        }
        
        else{
            document.getElementById("validFirstName").innerHTML="";
            return true
        }
    
}




function validateLastName(event){
    var lastname = document.getElementById("lastName").value.trim();
    if(lastname===""){
        document.getElementById("validLastName").innerHTML="Name can not be empty";
        // console.log("121");
        return false;
    }
    if((lastname.length<1) || (lastname.length>25)){
        document.getElementById("validLastName").innerHTML="Number of letters must be between 1 and 25";
        return false;
    }
    else{
        document.getElementById("validLastName").innerHTML="";
        return true;
    }
}





function validatePhone(event){
    var phonenumber = document.getElementById("mob").value.trim();
    const regexmob = /^\d{10}$/;
    if(phonenumber===""){
        document.getElementById("validateNumber").innerHTML="Number can not be empty";
        return false;
    }
    if(!regexmob.test(phonenumber)){
        document.getElementById("validateNumber").innerHTML="Phone number is invalid";
        return false;
    }
    else{
        document.getElementById("validateNumber").innerHTML="";
        return true;
    }
}


function validateEmail(event){
    var email = document.getElementById("email").value.trim();
    const regexemail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    if(email===""){
        document.getElementById("validateEmail").innerHTML="Email can not be empty";
        
        return false;
    }
    if(!regexemail.test(email)){
        document.getElementById("validateEmail").innerHTML="Email format is invalid";
        
        return false;
    }
    else{
        document.getElementById("validateEmail").innerHTML="";
        return true;
    }
}


function validateAddress1(event){
    var address1 = document.getElementById("address1").value.trim();
    if(address1==="" || address1==null){
        document.getElementById("validateAddress1").innerHTML="Address can't be null";
        
        return false;
    }
    else{
        document.getElementById("validateAddress1").innerHTML="";
        
        return true;
    }
}
function validateAddress2(event){
    var address2 = document.getElementById("address2").value.trim();
    if(address2==="" || address2==null){
        document.getElementById("validateAddress2").innerHTML="Address can't be null";
        
        return false;
    }
    else{
        document.getElementById("validateAddress2").innerHTML="";
        
        return true;
    }
}
function validateCity(event){
    var city = document.getElementById("city").value.trim();
    if(city==="" || city==null){
        document.getElementById("validateCity").innerHTML="City can't be null";
        
        return false;
    }
    else{
        document.getElementById("validateCity").innerHTML="";
        return true;
    }
}
function validateState(event){
    var state = document.getElementById("state").value.trim();
    if(state==="" || state==null){
        document.getElementById("validateState").innerHTML="State can't be null";
        
        return false;
    }
    else{
        document.getElementById("validateState").innerHTML="";
        return true;
    }
}
function validateZipCode(event){
    var zipcode = document.getElementById("zipCode").value.trim();
    if(zipcode==="" || zipcode==null){
        document.getElementById("validateZipCode").innerHTML="Zip-code can not be empty";
        
        return false;
    }
    if(zipcode.length !=6){
        document.getElementById("validateZipCode").innerHTML="Must be a 6 digit number";
        
        return false;
    }
    if(isNaN(zipcode)=="true"){
        document.getElementById("validateZipCode").innerHTML="Zip-code must be in digits";
        
        return false;
    }
    else{
        document.getElementById("validateZipCode").innerHTML="";
        return true;
    }
}

function validateGender(event){
    var gender=document.getElementsByName('gender');
    var genderFlag = false;
    for(var i=0;i<gender.length;i++){
        if(gender[i].checked){
            genderFlag = true;
            document.getElementById('validateGender').innerHTML="";
            break;    
        }    
    }
    if(genderFlag == false){
        document.getElementById('validateGender').innerHTML="Choose any one option";
        return false;
    }
    return genderFlag;
}







function validateDate(){
    // const currentDate = new Date();
    // console.log("currentdate=",currentDate);
    // const year = currentDate.getFullYear();
    // const month = (currentDate.getMonth() +1);
    // const day = currentDate.getDay();
    // const today = `${year}-${month}-${day}`; //for converting currentdate into yy-mm-dd format in which format html date input is given even though its placeholder shows dd-mm-yy format 
    // console.log("today=",today);

    // const givenDate = dob.value;
    const givenDate = document.getElementById("date").value;
    console.log("givendate=",givenDate);
    const date1 = new Date();
    console.log("date1=",date1);
    const date2 = new Date(givenDate);
    console.log("date2=",date2);
    // const timeDiff = Math.round((date1-date2)/(1000*60*60*24*365.25));
    const timeDiff = (date1-date2)/(1000*60*60*24*365.25);
    console.log(timeDiff)
    if (timeDiff>=18){
        document.getElementById("validateDate").innerHTML="";
        return true;
    }
    else{
        document.getElementById("validateDate").innerHTML="Below 18 years";
        return false;
    }
}

function validateJobRole(){
    var jobRole = document.getElementById("role").value;
    if (jobRole == "" || jobRole == null){
        document.getElementById("validateJobRole").innerHTML="Can not be empty";
        return false;
    }
    else if((jobRole == "Developer") || (jobRole == "Testing") || (jobRole == "Devops") || (jobRole == "Operations") || (jobRole == "Accounting")){
        document.getElementById("validateJobRole").innerHTML="";
        return true;
    }
}

function validateExperience(){
    var experience = document.getElementById("experience").value;
    if(experience == "" || experience == null ){
        document.getElementById("validateExperience").innerHTML="Can not be empty";
        return false;
    }
    else{
        document.getElementById("validateExperience").innerHTML="";
        return true;
    }
}

function validateCountry(){
    var country = document.getElementById("country").value;
    if(country == "" || country == null){
        document.getElementById("validateCountry").innerHTML="Can not be empty";
        return false;
    }
    else{
        document.getElementById("validateCountry").innerHTML="";
        return true;
    }
}

function preventbackbutton(){window.history.forward();}//
setTimeout("preventbackbutton()", 0);
window.onunload=function(){null};