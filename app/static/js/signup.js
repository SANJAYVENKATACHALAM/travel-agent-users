const form = document.getElementById("signupForm");

const password = document.getElementById("password");

const strength = document.getElementById("strength");

const message = document.getElementById("message");

password.addEventListener("input", () => {

    if(password.value.length < 6){

        strength.innerText="Weak Password";

        strength.style.color="red";

    }

    else if(password.value.length <10){

        strength.innerText="Medium Password";

        strength.style.color="orange";

    }

    else{

        strength.innerText="Strong Password";

        strength.style.color="lime";

    }

});


form.addEventListener("submit", async(e)=>{

e.preventDefault();

message.innerText="";

const name=document.getElementById("name").value;

const email=document.getElementById("email").value;

const pass=password.value;

const confirm=document.getElementById("confirmPassword").value;

if(pass!==confirm){

message.innerText="Passwords do not match";

return;

}

const response=await fetch("/auth/signup",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

name,

email,

password:pass

})

});

const data=await response.json();

if(!response.ok){

message.innerText=data.detail;

return;

}

alert("Account Created Successfully");

window.location.href="/login";

});