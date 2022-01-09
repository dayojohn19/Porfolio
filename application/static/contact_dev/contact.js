

function contact_dev()  {
    contact_form_position.style.display = 'block';
}


    // <div id="contact-form"></div>
    // <script src="{% static 'contact_dev/contact.js' %}" defer></script>
    // <link href="{% static 'contact_dev/contact.css' %}" rel="stylesheet">
    // <button onclick="contact_dev()">Contact Us</button>
// Note!create DIV #contact-form in line 8
// *********************************************
// *********************************************
// ----------- CONTACT FORM FORM ---------------
// *********************************************
// *********************************************
console.log('contactForm')
contact_form_position = document.querySelector("#contact-form");

contact_form_heading    =   document.createElement("h1");
contact_form_heading.innerHTML  =   "Contact Us"
contact_form_heading.setAttribute("id", "contact-form-heading");

contact_form = document.createElement("form");
contact_form.setAttribute("id",   "contact-form-id")
// contact_form.setAttribute("method",    "post");
// contact_form.setAttribute("action", "urlUrl");


user_contact    =document.createElement("input");
user_contact.setAttribute("type",   "text");
user_contact.setAttribute("name",   "user_contact");
user_contact.setAttribute("placeholder",    "Your Contact Email | or | Number");
user_contact.setAttribute("id", "user_contact_id")
user_contact.style.display  =   "block";
user_contact.style.width    =   "90%";
user_contact.style.fontSize =   "large";

user_name   =document.createElement("input");
user_name.setAttribute("type",  "text");
user_name.setAttribute("name",  "user_name");
user_name.setAttribute("placeholder",   "Your name")
user_name.style.display  =   "block";
user_name.style.width    =   "90%";
user_name.style.fontSize =   "large";
user_name.setAttribute("id",    "user_name_id");

user_message    =document.createElement("textarea");
user_message.setAttribute("type",   "textarea");
user_message.setAttribute("id", "user-message")
// user_message.style.width = "50%";
user_message.style.margin   =   "auto auto";
user_message.style.display  =   "block";
user_message.style.width    =   "60%";
user_message.style.height   =   "200px";
user_message.style.fontSize =   "large";

contact_form_button = document.createElement("button");
contact_form_button.setAttribute("onclick", "submit_message()");
contact_form_button.innerHTML = "Send"
contact_form_button.setAttribute("id", "contact-form-button")

contact_form.appendChild(contact_form_heading);
contact_form.appendChild(user_contact);
contact_form.appendChild(user_name);
contact_form.appendChild(user_message);
contact_form.appendChild(contact_form_button)
// contact_form.appendChild(contact_form_submit);
contact_form_position.appendChild(contact_form);



function submit_message()  {
    fetch(`/application/send/${user_contact.value}/${user_name.value}/${user_message.value}`,{
        method: 'post'
    });
    console.log('done', user_message.value,user_name.value,user_contact.value)
    // contact_form.submit();
    user_contact.value=   '';
    user_name.value   =   '';
    user_message.value=   '';
    contact_form_position.style.display = 'none';
    alert('MESSAGE SENT')
}