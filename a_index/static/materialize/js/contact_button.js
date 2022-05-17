// INSERT <script src="https://smtpjs.com/v3/smtp.js"></script>
// above

console.log('Contact.Js Loaded')
const btn = document.createElement('button')
btn.innerHTML = 'Contact Us'
btn.style.backgroundColor = 'rgb(88, 188, 255)'
btn.style.border = 'none';
btn.style.borderRadius = '8px'
btn.style.padding = '8px'
btn.style.fontSize = 'large'
btn.style.right = '0px'
btn.style.position = 'fixed'
btn.style.top = '88%'
btn.style.zIndex = 2
btn.onclick = function () {
    sendEmail()
}
// btn.onclick = function () { alert('ye') }
document.body.appendChild(btn)



function sendEmail() {
    Email.send({
        Host: "smtp.elasticemail.com",
        Username: "repapaka20@gmail.com",
        Password: "20B28409FAB2EC360F970DEBC62ACB854E4B",
        To: 'dayo_john16@yahoo.com',
        From: "repapaka20@gmail.com",
        Subject: "This is the subject",
        Body: "And this is the body"
    }).then(
        message => alert('Please Check You Spam', message)
    );

}
// btn.onclick = alert('Hey');
// right: 0px;
// height: 4vw;
// border: none;
// // position: absolute;
// z - index: 1;
// top: 95 %;
// position: sticky;