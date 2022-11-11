sanitizeEmails(email_messages);

function sanitizeEmails(emails){    
    for (var i=0; i < emails.length; i++) {
        if (emails[i].hasAttachment == true){
            emails[i].date = moment(emails[i].date).format("DD-MM-YYYY");
            emails[i].subject = emails[i].subject.replace(/[^a-zA-Z0-9_ -]/g,'').trim();
            if(emails[i].subject.length>50){
                emails[i].subject = emails[i].subject.slice(0,100);
                }
        test = emails; 
        }
    }   
}