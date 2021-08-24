


document.addEventListener('DOMContentLoaded', function() {

});

i = document.querySelector('#tab-top');
i.style.display = 'none';
n = document.querySelector('#tab-net');
apl = document.querySelector('#apl');


n.onclick = (i) => {
    i = document.querySelector('#tab-top');
    if (i.style.display == 'none')
   document.querySelector("#tab-top").style.display = 'block';
    else
   document.querySelector("#tab-top").style.display = 'none';
}

///////////////
///////////////
///////////////
///////////////
///////////////
///////////////
    $('.test').click(function(){
    var post_id;
    post_id=$(this).data("catid");
    $.ajax({
    type:"POST",
    url:`${post_id}/like`,
    data:{ 
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        post_id:post_id},
        success: function(data){
            total= $('#'+post_id).attr("data-total")
            if ($('#'+post_id).attr("value") == 'Like')
            {$('#'+post_id).attr("value", parsInt(total)+1);
             $('#c-'+post_id).text((parseInt(total)+1));}
        }
});
  //  location.reload();
    console.log(post_id);
})
///////////////
///////////////
///////////////
function toogle_edit(id) {

    document.querySelector("#same_user"+id).style.display = 'block';
    document.querySelector(".t"+id).style.display = 'none';
    document.querySelector("#con-"+id).style.display = 'none';
}
///////////////
function Like(id){
    fetch(id + "/like", {
        method: 'POST',
        post_id:id,
    });
    x=document.querySelector(".lc-"+id).innerHTML;
    y = parseInt(x)+1;

    document.querySelector(".lc-"+id).innerHTML = y;

    document.querySelector(".ul-"+id).style.display = 'block';
    document.querySelector(".l-"+id).style.display = 'none';
}
///////////////

function UnLike(id){
    fetch(id + "/like", {
        method: 'POST',
        post_id:id,
    });
    x=document.querySelector(".lc-"+id).innerHTML;
    y = parseInt(x)-1;

    document.querySelector(".lc-"+id).innerHTML = y;

    document.querySelector(".ul-"+id).style.display = 'none';
    document.querySelector(".l-"+id).style.display = 'block';


}
///////////////
function share(id){
    alert(` Thank you ${id} for Sharing ! :,)`);
}
///////////////
function Edit(id){
    const c =  document.querySelector(".con"+id).value;
    const con_id = document.querySelector("#con-"+id).innerHTML;
    console.log(id);
        fetch(`posts/${id}/edit`,{
            
            method: 'POST',
            post_id:id,
            body: JSON.stringify({
                c:c
            })
        }).then(response => response.json());
    console.log(c);
    document.querySelector("#con-"+id).innerHTML = c;
    console.log(con_id);
    document.querySelector("#same_user"+id).style.display = 'none';
    alert('Edited Successful');
    document.querySelector(".t"+id).style.display = 'block';
    document.querySelector("#con-"+id).style.display = 'block';
}
///////////////

function testjs(){

    fetch("in2")
    .then(response => response.json())
    .then(xp => {
        console.log(xp);
        xp.forEach(element => {
            const e = element;
            var ce = document.createElement('div');

            ce.id = `${e.id}`;
            textarea = `<input name="textarea">`
            items = `<div style="border-radius: 25px; border: 2px solid rgb(255, 150, 150); background-color: rgb(255, 210, 210);  margin-top: 10px; width: 100%;">
            <h5 style="border-radius: 25px; border: 2px solid rgb(255, 150, 150); background-color: rgb(207, 255, 207);  margin-top: 10px;">By: ${e.user}</h5>
            <p style="color:black;border-radius: 25px; border: 2px solid rgb(255, 150, 150); background-color: rgb(176, 226, 255);  margin-top: 10px;">"${e.content}"</p>
            ${e.timestamp}<br>
            Likes: ${e.likes}`

            ce.innerHTML =`
            <div id="create-posts"> 
            ${items}<br>

            <button onclick="Like(${e.id})"> xLike </button>

            </div>
            

            

            
            </div><br>
            `;

           c2 = document.querySelector("#put").append(ce);
        });
    });
}
