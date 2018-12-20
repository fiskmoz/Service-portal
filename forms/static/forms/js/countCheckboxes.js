function countCheckboxes(Medal){
  var inputElems = document.getElementsByTagName("input"), count = 0;
    for(var i=0; i<inputElems.length; i++) {
      if(inputElems[i].type === "checkbox" && inputElems[i].checked === true){
        count++;
      }
    }
    var amountOfCheckboxes = inputElems.length;
    var goldLimit = amountOfCheckboxes / 2;
    var silverLimit = amountOfCheckboxes / 5;
    if(count >= goldLimit && Medal == 'Gold'){
      alert("Order sent");
      document.contract.submit();
    }
    if(count >= goldLimit && Medal != 'Gold')
      alert("It is recommended you have chosen Service Tier Gold");
    if(count < goldLimit && count > silverLimit && Medal == 'Silver'){
      alert("Order sent");
      document.contract.submit();
    }
    if(count < goldLimit && count > silverLimit && Medal != 'Silver')
      alert("It is recommended you have chosen Service Tier Silver");
    if(count <= silverLimit && Medal == 'Bronze'){
      alert("Order sent");
      document.contract.submit();
    }
    if(count <= silverLimit && Medal != 'Bronze')
      alert("It is recommended you choose more services to monitor");
}
