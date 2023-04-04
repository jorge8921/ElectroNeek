function getText(){
sel = document.getElementsByClassName("form-select")[0]; // [0]  is because there is more than 1 element with the same Class Name
text= sel.options[sel.selectedIndex].text
return text;
}