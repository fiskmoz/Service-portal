function checkSystemId(){
    systemID = document.getElementById("SystemId").value
    const Http = new XMLHttpRequest();
    const url= 'http://127.0.0.1:8000/API/Exists/Systemid/' + systemID + '/' ;

    Http.open("GET", url);
    Http.send();

   Http.onreadystatechange = function() {
       if (Http.readyState === 4) {
           if (Http.response === "true"){

               document.getElementById("orderID").submit();
           }
           else{
               alert("SystemID dosnt exist, please enter correct ID")
           }
       }

   }
}
