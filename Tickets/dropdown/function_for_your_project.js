function getText(){
	sel = document.getElementsById("oHeader_ctl00_ctl01_ctl01_ctl00_UltimateTabstrip_UltimateTab1_AllTimePeriodsOEM_criteriaControl");
	text= sel.options[sel.selectedIndex].text;
	return text;
}