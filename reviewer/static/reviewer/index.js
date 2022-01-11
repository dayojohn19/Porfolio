console.log('Reviewer JS loaded')

function changeDepartment() {
    document.querySelector("#choose").style.display = 'block';
    document.querySelector("#had_chosen").style.display = 'none';
}
function chooseLevel(id)  {
    document.querySelector("#choose").style.display = 'none';
    document.querySelector("#had_chosen").style.display = 'block';
    document.querySelector("#user_department").innerHTML = id;
}


function get_Questions(level)    {
    department = document.querySelector("#user_department").innerHTML; // engine or derc
    window.location.href = `questions/${department}/${level}`;
}


// ----__*****************
// ----__*****************
// ----__*****************
user_acticvity()
    function user_acticvity() {
            // ===== GETTING IP ====
            fetch('/user/user_ip').then(response => response.json()).then(result => {
                if (result == '') {
                    contact = prompt('Your: \n  | Moblie Number |  or  | Email Address | ', '');
                    if (contact) {
                        fetch('/user/user_ip', {
                            method: 'POST',
                            body: JSON.stringify({
                                contact: contact,
                            })
                        });
                        alert('Thank you');
                        //insert fetch to save
                    }
                    fetch('/user/user_ip').then(response => response.json()).then(result => {
                        fetch(`/reviewer/ip/register/${result}`).then(response => response.json()).then(data => {
                            console.log('DATA IS : ', data)
                            // document.querySelector("#userScore").value = data[0];
                            // MakenewQuestion(1);
                            // MakenewQuestion(2);
                        });
                    });
                }
                if (result == 'first_time') {
                    alert('We are accepting Cookies.')
                }
                document.querySelector("#user_ip").value = result

                // console.log('USER_IP: ',document.querySelector("#user_ip").value)
                // fetch(`/reviewer/get_score/${result}`).then(response => response.json()).then(data => {
                //     console.log('DATA: ',data[0]);
                //     document.querySelector("#userScore").value = data[0];
                //     MakenewQuestion(1);
                //     MakenewQuestion(2);
                //     location.reload();
                // });

                return result //MAKE A GET OR CREATE HERE
            });
            // ===== GETTING IP ====
        }
