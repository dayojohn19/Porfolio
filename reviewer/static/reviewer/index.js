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
    // level = operational or management
    // alert(department+level)
    window.location.href = `questions/${department}/${level}`;
}