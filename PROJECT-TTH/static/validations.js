function validatePassword(){
    var password1 = document.forms['registrationform']['password'].value;
    var patt = new RegExp("[0-9]");
    var result = patt.test(password1);

    if(result==false  password1.length<5  password1.length>20){
        document.getElementById("password").style.border = "2px solid red";
        var errorpassword = "Password Must Contain 1 digit with 5 to 20 charcters";
        document.getElementById("password").value="";
        document.getElementById("password").placeholder=errorpassword;
        return false;
    }
    else{
        document.getElementById("password").style.border = "2px solid green";
        return true;
    }
}


function validateall(){
    if(validateUserName() & validatePassword()){
        return true;
    }else{
        return false;
    }
}