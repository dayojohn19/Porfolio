//counter for online
if  (!localStorage.getItem('intc'))
{localStorage.setItem('intc',0);}
//function for minutes online
function go () {
  //retreive
  let intc = localStorage.getItem('intc');
  //update
  intc++;
  const xx = intc;
  const yy = Math.trunc(xx/60);
  const jj = yy+' minutes';
  document.querySelector('#h4').innerHTML = jj;
  //store the date
  localStorage.setItem('intc', intc);
}
document.addEventListener('DOMContentLoaded', function() {
//counter
setInterval(go, 1000);
//value of div
document.querySelector('#compose-recipients').onchange = function() {
document.querySelector('#rec').innerHTML= document.querySelector('#compose-recipients').value;
}
//disabling submit
const submit = document.querySelector('#submit');
const body = document.querySelector('#compose-body');
submit.disabled = true;
body.onkeyup = () => {
if (body.value.length == null)
{submit.disabled = true;}
else
{submit.disabled = false}
}
//send test fetch 2
document.querySelector('#submit').onclick = () => cc();
// Clear out composition fields
document.querySelector('#compose-recipients').value = '';
document.querySelector('#compose-subject').value = '';
document.querySelector('#compose-body').value = '';


// Use buttons to toggle between views
document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
document.querySelector('#compose').addEventListener('click', compose_email);
// By default, load the  inbox
load_mailbox('sent');
});



/////////   END OF DOM HERE /
/////////   END OF DOM HERE /
/////////   END OF DOM HERE /

 
//send email in compose 
function cc() {
const body = document.querySelector('#compose-body').value;
const subject = document.querySelector('#compose-subject').value;
const recipients = document.querySelector('#compose-recipients').value;

alert('send');
fetch('/app_mail/application/emails', {
  method: 'POST',
  body: JSON.stringify({
      recipients: recipients,
      subject: subject,
      body: body
  })
})
.then(response => response.json())
.then(result => {
    // Print result
    console.log(result);
    load_mailbox('sent');
});
alert('message sent');
load_mailbox('sent');
console.log('sending');
}
//
function compose_email() {
// Show compose view and hide other views
document.querySelector('#emails-view').style.display = 'none';
document.querySelector('#compose-view').style.display = 'block';
document.querySelector('#side').style.display = 'none';
}


function load_mailbox(mailbox) {
// Show the mailbox and hide other views
document.querySelector('#emails-view').style.display = 'block';
document.querySelector('#compose-view').style.display = 'none';
document.querySelector('#side').style.display = 'none';
// Show the mailbox name
document.querySelector('#emails-view').innerHTML = `<strong><h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3></strong>`;
 

//fetch the emails 
fetch(`/app_mail/application/emails/${mailbox}`)
.then(response => response.json())
.then(emails => {
console.log(emails);
x1 = emails;
x1.forEach((element) => {
if (mailbox == "inbox") {
  if (element.read) 
  is_read = "read";
  else
  is_read = "";
  }
        const e = element
        const ie = document.createElement('div');
                  ur = `<div 
                  class="email_listun";
                  id="ie-${e.id}"> 
                      <h5 style="background-color:yellow;">
                      <strong>${e.subject}</strong>  </h5>from: ${e.sender} <br>Sent on: ${e.timestamp} (GMT)<br> 
<br> </div><hr>`;
        ie.innerHTML = ur;
//When the mail is clicked 
  ie.addEventListener('click',() => {

    xdate();
    show_mail(element.id, mailbox);
  });
  //ie.addEventListener('click',(xalertreadmail));

  function xdate() {
    document.querySelector('#side').style.display = 'block';
    fetch(`/app_mail/application/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    x1 = emails;
    x1.forEach(element => {
              const e = element;
            })});
    //get curent local time 
                            const ti = new Date();
                            const mo = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"];
                            const mn = mo[ti.getMonth()];
                            const da = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
                            const dn = da[ti.getDay()];
                            const md2 = ti.getDate();
                            var hours = ti.getHours();
                            var minutes = ti.getMinutes();
                            var ampm = hours >= 12 ? 'pm' : 'am';
                            hours = hours % 12;
                            hours = hours ? hours : 12; // the hour '0' should be '12'
                            minutes = minutes < 10 ? '0'+minutes : minutes;
                            var tn = hours + ':' + minutes + ' ' + ampm;
  //inside the div when clicked 
              const rd = `<div
              class="email_list"
              id="ie-${e.id}"> 
              <h5><strong>${e.subject}</strong></h5>  </h5>from: ${e.sender} <br>Sent on: ${e.timestamp} (GMT)<br> 
              <strong>Read on:</strong> ${" "+mn+" "+md2+" "+dn+" "+tn} 
              </div>
              <hr>
              `;
  //when mail_clicked
              ie.innerHTML = rd;
              console.log(e);//seeting item
  localStorage.setItem('intcd', e);}
          
  //end of fetch
  document.querySelector("#emails-view").append(ie);
  //end of function_mail
  //get date

});
});
}
///////////////////////////////////////////////////////
///////////////////////////////////////////////////////
///////////////////////////////////////////////////////
function show_mail(id, mailbox) {
fetch(`/app_mail/application/emails/${id}`)
.then((response) => response.json())
.then((email) => {
  e = email;
  // Print email
  // console.log(email);
  document.querySelector("#side").innerHTML = "";
  var de = document.createElement("div");
  de.className = `card`;
/////
  di = `<div id="side" class="email_body">
  <button class="post2" id="archive"></button>
  <button class="post2" id="reply">reply</button>
  
<br> </h5><br> <h2><strong>${e.subject}</strong></h2><br>${e.body}
<br><br><br><br>from:  ${e.sender} <br>Sent on: ${e.timestamp} (GMT)
</div>`;
  de.innerHTML = di;
  di.className = 'post';  
  d2 = document.querySelector('#side').append(de);
  if (mailbox == "sent")
  {document.querySelector("#archive").style.display = 'none';
  document.querySelector("#reply").style.display = 'none';
return;}


  let archive = document.querySelector("#archive");

  archive.addEventListener("click", event => {
    toggle_archive(id, email.archived);
    if (archive.innerText == "Archive") {archive.innerText = "Unarchive"; alert("Mail Archived !!");load_mailbox('archive');}
    else {archive.innerText = "Archive"; alert("Mail Unarchived !!"); load_mailbox('inbox');}
    /////////style 
  });
  if (!email.archived) archive.textContent = "Archive";
  else archive.textContent = "Unarchive";

  let reply = document.querySelector("#reply");
  reply.addEventListener("click", () => {
    reply_mail(email.sender, email.subject, email.body, email.timestamp);
  });
  make_read(id);
});

}

function toggle_archive(id, state) {
fetch(`/app_mail/application/emails/${id}`, {
method: "PUT",
body: JSON.stringify({
  archived: !state,
}),
});
}

function make_read(id) {
fetch(`/app_mail/application/emails/${id}`, {
method: "PUT",
body: JSON.stringify({read: true,}), 
});
}

function reply_mail(sender, subject, body, timestamp) {
compose_email();
if (!/^Re:/.test(subject)) subject = `Re: ${subject}`;
document.querySelector("#compose-recipients").value = sender;
document.querySelector("#compose-subject").value = subject;

pre_fill = `On ${timestamp} ${sender} wrote:\n${body}\n`;

document.querySelector("#compose-body").value = pre_fill;
}


///////////////////////////////////////////////////////
///////////////////////////////////////////////////////
///////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////
////////////////   GIVE   STYLE TO  BUTTON AFTER  CLICK ////////////
///////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////
document.addEventListener('click', event => {

})
///////////////////////////////////////////////////////
///////////////////////////////////////////////////////

//////////////////
//////////////////


//////////////////
//////////////////
//////////////////


//////
