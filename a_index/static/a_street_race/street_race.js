let y = 0;
setInterval(() => {
//getting the joiner
    //getting the message

        fetch('fetch')
        .then(response => response.json())
        .then(messages => {
            x = messages.length;
            if((y-x) == 0) {
                console.log('nonew ' + x);
            }else {
                latest = messages.slice(Math.max(messages.length - 3, 0))
                //.reverse()
                console.log(latest);
                y=x;
                console.log(y);
            
            
            latest.forEach((element) => {
                const e = element;

                console.log(e);
                div = document.createElement('div');

                    content = `<div class="all_message">
                                ${e.time}&nbsp;:   &nbsp;&nbsp;&nbsp;
                                ${e.message}
                            </div>`;
                    xx = div.innerHTML = content;
            });
            all = div;
            document.querySelector(".list_messages").prepend(all);
        }
        });

    
}, 1500);


function message_general(){
    message_u = document.querySelector(".message_general").value;
    fetch('send',{
            method: 'POST',
            body: JSON.stringify({
                message_u : message_u,
                player:'noname',
                chat_id : 1,
            })
        });
        document.querySelector(".message_general").value = '';

}