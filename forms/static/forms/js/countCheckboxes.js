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
      sendOrder();
      document.getElementById('OrderID').submit();
    }
    if(count >= goldLimit && Medal != 'Gold')
      alertUSer('Gold');
    if(count < goldLimit && count > silverLimit && Medal == 'Silver'){
      sendOrder();
      document.getElementById('OrderID').submit();
    }
    if(count < goldLimit && count > silverLimit && Medal != 'Silver')
      alertUSer('Silver');
    if(count <= silverLimit && Medal == 'Bronze'){
      sendOrder();
      document.getElementById('OrderID').submit();
    }
    if(count <= silverLimit && Medal != 'Bronze')
      alert("With the current settings of your order, It is recommended you choose more services to monitor");
}

function sendOrder(){
  alert("Order sent");
}

function alertUser(medal){
  alert("With the current settings of your order, It is recommended you have chosen Service Tier " + medal);
}
