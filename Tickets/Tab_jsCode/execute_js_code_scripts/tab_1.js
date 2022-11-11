window.onkeypress = function(e) {
    if (e.which == 13) {
       e.preventDefault();
       var nextInput = inputs.get(inputs.index(document.activeElement) + 1);
       if (nextInput) {
          nextInput.focus();
       }
    }
};