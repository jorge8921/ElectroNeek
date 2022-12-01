function clickBtn(){
	var iframe = document.getElementById('MSOPageViewerWebPart_WebPartWPQ3');
	var doc = iframe.contentDocument || iframe.contentWindow.document;
	var elem = document.getElementById('txtNumDoc');
	elem.value = '1039703263';
}