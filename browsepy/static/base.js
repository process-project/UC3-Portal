(function(){
    if(document.querySelectorAll && document.addEventListener){
        var forms = document.querySelectorAll('form'),
            i, j, form, button, inputs, files, buttons;
        for(i = 0; form = forms[i++];){
            buttons = form.querySelectorAll('input[type=submit], input[type=reset]');
            inputs = form.querySelectorAll('input');
            files = form.querySelectorAll('input[type=file]');
            if(files.length == 1 && inputs.length - buttons.length == 1){
                files[0].addEventListener('change', (function(form){
                    return function(e){
                        form.submit();
                    };
                }(form)));
                for(j = 0; button = buttons[j++];){
                    button.style.display = 'none';
                }
            }
        }
    }
}());

if ( !  readCookie("termsandconditions")) {
    popupTerms();
}
function createCookie(name,value,days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        var expires = "; expires=" + date.toUTCString();
    }
    else var expires = "";
    document.cookie = name + "=" + value + expires + "; path=/";
}

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

function eraseCookie(name) {
    createCookie(name,"",-1);
}
function popupTerms()
{
    bootbox.confirm({
		message: terms,
		closeButton: false,
		callback:  function(result){
        		if(result)
        		{
            			createCookie("termsandconditions", "accepted", 21);
        		}
        		else
        		{
            			popupTerms();
        		}
		}
		
   }).off("shown.bs.modal");
}
