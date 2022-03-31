function login(){
    var username=document.getElementById("uname").value
    var password=document.getElementById("psw").value
  
  //username
    if(username==""){
      document.getElementById("uname1").innerHTML="Please enter your username"
      document.getElementById("uname1").style.color="red"
      document.getElementById("uname").style.border="1px red solid"
      return false
    }
    else{
        document.getElementById("uname1").innerHTML=""
        document.getElementById("uname").style.border="1px black solid"
    }
//password
    if(password==""){
      document.getElementById("spsw").innerHTML="please enter your password"
      document.getElementById("spsw").style.color="red"
      document.getElementById("psw").style.border="1px red solid"
      return false
    }
    else{
      document.getElementById("spsw").innerHTML=""
      document.getElementById("psw").style.border="1px black solid"
    }
  }
