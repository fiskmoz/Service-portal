function checkOrderName(username){

   OrderName = document.getElementById("OrderName").value;
   const Http = new XMLHttpRequest();

   const url= 'http://127.0.0.1:8000/API/User/' + username + '/' + OrderName + '/' ;

   Http.open("GET", url);
   Http.send();
   Http.onreadystatechange = function() {
       if (Http.readyState === 4) {
           if (Http.response === "false"){

               checkSystemId()
           }
           else{
               alert("Ordername already exists, please choose another one")

           }
       }

   }


}
