function tier(sender) {
//	clear("ResponseTime")
//	clear("ServiceTime")

	if(sender.value == "Gold" || sender == "Gold"){

		document.getElementsByName("ResponseTime")[0].disabled = false;
		document.getElementsByName("ResponseTime")[1].disabled = false;
		document.getElementsByName("ResponseTime")[2].disabled = true;

		document.getElementsByName("ResponseTime")[2].checked = false;

		document.getElementsByName("ServiceTime")[0].disabled = false;
		document.getElementsByName("ServiceTime")[1].disabled = false;
		document.getElementsByName("ServiceTime")[2].disabled = true;

		document.getElementsByName("ServiceTime")[2].checked = false;
	}
	else if(sender.value == "Silver" || sender == "Silver"){

		document.getElementsByName("ResponseTime")[0].disabled = true;
		document.getElementsByName("ResponseTime")[1].disabled = false;
		document.getElementsByName("ResponseTime")[2].disabled = false;

		document.getElementsByName("ResponseTime")[0].checked = false;

		document.getElementsByName("ServiceTime")[0].disabled = true;
		document.getElementsByName("ServiceTime")[1].disabled = false;
		document.getElementsByName("ServiceTime")[2].disabled = false;

		document.getElementsByName("ServiceTime")[0].checked = false;
	}
	else{

		document.getElementsByName("ResponseTime")[0].disabled = true;
		document.getElementsByName("ResponseTime")[1].disabled = true;
		document.getElementsByName("ResponseTime")[2].disabled = false;

		document.getElementsByName("ResponseTime")[0].checked = false;
		document.getElementsByName("ResponseTime")[1].checked = false;

		document.getElementsByName("ServiceTime")[0].disabled = true;
		document.getElementsByName("ServiceTime")[1].disabled = true;
		document.getElementsByName("ServiceTime")[2].disabled = false;

		document.getElementsByName("ServiceTime")[0].checked = false;
		document.getElementsByName("ServiceTime")[1].checked = false;
	}
	setTier(sender);
}

var currentTier = "Gold";

function setTier(sender){
	currentTier = sender.value;
}
function setTier2(value){
	currentTier = value;
}
function getTier()
{
	return currentTier;
}
