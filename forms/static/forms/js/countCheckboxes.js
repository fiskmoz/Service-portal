function countCheckboxes(Medal){
  var inputElems = document.getElementsByTagName("input"),
    count = 0;
    for(var i=0; i<inputElems.length; i++) {
      if(inputElems[i].type === "checkbox" && inputElems[i].checked === true){
        count++;
      }
    }
    //Do something with Medal

    if(count >= 25 && Medal == 'Gold'){
      alert("Order sent");
      document.contract.submit();
    }
    if(count >= 25 && Medal != 'Gold')
      alert("It is recommended you have chosen Service Tier Gold");
    if(count < 25 && count > 10 && Medal == 'Silver'){
      alert("Order sent");
      document.contract.submit();
    }
    if(count < 25 && count > 10 && Medal != 'Silver')
      alert("It is recommended you have chosen Service Tier Silver");
    if(count <= 10 && Medal == 'Bronze'){
      alert("Order sent");
      document.contract.submit();
    }
}
