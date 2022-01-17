console.log('Static Reviewr Question Loaded\n\n')

    function isRight(value, id){
        // answer=0;
        // container=0;
        if (id == 'a1' || id == 'b1')   {
            answer = document.querySelector("#container-1-answer").innerHTML;
            question    =document.querySelector("#container-1-question").innerHTML;
            container = 1
        }
        if (id == 'a2' || id == 'b2') {
            answer = document.querySelector("#container-2-answer").innerHTML;
            question    =   document.querySelector("#container-2-question").innerHTML;
            container = 2
        }
        totalSeconds = 0;
        checkAnswer(value, answer, container, question)
    }

    function checkAnswer(value, answer, container, question){
        if (answer == value) {
            addScore('correct');
            changeContainer(container);
        } else if (answer != value) {
            addScore('wrong');
        }
        prompt(question,answer);
    }

    function AddScoretoDatabase(side){
            score= document.querySelector("#userScore").value;
            tries=  document.querySelector("#tries").value;
            user_ip = document.querySelector("#user_ip").value;
            if (score == undefined)  {
                score   =   0;
                tries   =   0;
                result  =   0;
            }
            fetch(`/reviewer/add_score/${side}/${tries}/${score}/${user_ip}`).then(response => response.json()).then(result => {
                console.log('RESULT: ',result)  
            })
    }



    function addScore(side){
        score   =document.querySelector("#userScore");
        tries   = document.querySelector("#tries");
        numScore =parseInt(score.value)
        if (side == 'correct'){
            score.value  = numScore+=1;
            AddScoretoDatabase('correct')
        } else if ( side == 'wrong')    {
            score.value  = numScore-=3; //score_adjust adjust score algo_adjust
            AddScoretoDatabase('wrong')
        }
        trials = parseInt(tries.value);
        trials +=1;
        tries.value = trials;
        document.querySelector("#userFunction").value = your_function;
    }

    function changeContainer(container) {
        // add correct value
        if (container == 1) {
            containerHide = document.querySelector("#container-1");
            containerShow = document.querySelector("#container-2");
        }
        if (container == 2) {
            containerHide = document.querySelector("#container-2");
            containerShow = document.querySelector("#container-1");
        }
        containerHide.style.display = 'none';
        containerShow.style.display = 'block';
        MakenewQuestion(container)
    }

    function newQuestion(container, FinalAnswer, FinalQuestion, WrongAnswer) {
        if (container == 1) {
            container = document.querySelector("#container-1");
            container_question = document.querySelector("#container-1-question");
            container_question.innerHTML = FinalQuestion; // change innerhtml

            container_answer = document.querySelector("#container-1-answer");
            container_answer.innerHTML = FinalAnswer;

            buttonA = document.querySelector("#a1");
            buttonA.value   =WrongAnswer;
            buttonA.innerHTML   =WrongAnswer;

            buttonB =document.querySelector("#b1");
            buttonB.value   =WrongAnswer;
            buttonB.innerHTML   =WrongAnswer;
            // correct answer
            buttonCorrect = document.querySelector(`#${getRandomString()+1}`)
            buttonCorrect.value = FinalAnswer;
            buttonCorrect.innerHTML = FinalAnswer;
        }

        if (container == 2) {
            container   =document.querySelector("#container-2");
            container_question  =document.querySelector("#container-2-question");
            container_question.innerHTML    = FinalQuestion; //change it

            container_answer    =document.querySelector("#container-2-answer");
            container_answer.innerHTML  =FinalAnswer
            
            buttonA = document.querySelector("#a2")
            buttonA.value = WrongAnswer;
            buttonA.innerHTML = WrongAnswer;

            buttonB = document.querySelector("#b2");
            buttonB.value = WrongAnswer;
            buttonB.innerHTML = WrongAnswer;
            // console.log('done container2')
            // correct answer
            buttonCorrect = document.querySelector(`#${getRandomString()+2}`)
            buttonCorrect.value = FinalAnswer;
            buttonCorrect.innerHTML = FinalAnswer;
        }
    }

    function MakenewQuestion(container){
        // ---------- algo_adjusts score_function ---------

            current_user_score = document.querySelector("#userScore").value;
            current_user_score = parseInt(current_user_score)
            your_function = 'function1';//algo_adjusts score_function
            if (current_user_score > 10){ //algo_adjusts score_function
                your_function = 'function1'//algo_adjusts score_function
            }
            if (current_user_score > 20){ //algo_adjusts score_function
                your_function = 'function2'//algo_adjusts score_function
            }
            if (current_user_score > 30){ //algo_adjusts score_function
                your_function = 'function3'//algo_adjusts score_function
            }

        fetch(window.location.pathname+'/'+your_function+'/getit').then((r) => r.json()).then(data=>{
            FinalQuestion = data[1]
            if (data[6].toLowerCase() == 'd'){ //question adjust answer
                FinalAnswer = data[5]
                WrongAnswer = data[4]
            }
            if (data[6].toLowerCase() == 'b'){ //question adjust answer
                FinalAnswer = data[3]
                WrongAnswer = data[2]
            }
            if (data[6].toLowerCase() == 'c'){ //question adjust answer
                FinalAnswer = data[4]
                WrongAnswer = data[3]
            }
            if (data[6].toLowerCase() == 'a'){ //question adjust answer
                FinalAnswer = data[2]
                WrongAnswer = data[3]
            }

            newQuestion(container, FinalAnswer, FinalQuestion, WrongAnswer)
        });
    }
    // console.log('Make no container: ',MakenewQuestion())

function getRandomString() {
    var randomChars = 'ab';
    var result = '';
    for ( var i = 0; i < 1; i++ ) {
        result += randomChars.charAt(Math.floor(Math.random() * randomChars.length));
    }
    return result;
}


    user_acticvity()


// VERSION 2
    function user_acticvity() {

        // ===== GETTING IP ====
        fetch('/user/user_ip').then(response => response.json()).then(result => {
            if (result == '') {
                contact = prompt('Your: \n  | Moblie Number |  or  | Email Address | ', '');
                if (contact) {
                    // console.log('Score: ',score)
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
                    fetch(`/reviewer/get_score/${result}`).then(response => response.json()).then(data => {
                        // if (data[0] = null) {
                        //     document.querySelector("#userScore").value = 0;
                        // } else {
                            document.querySelector("#userScore").value = data[0];
                            document.querySelector("#user_ip").value    =   data[2]
                        // }

                        // document.querySelector("#tries").value      =   data[1];
                        MakenewQuestion(1);
                        MakenewQuestion(2);
                        // location.reload();
                    });
                });
            }
            if (result == 'first_time') {
                alert('We are accepting Cookies.')
            }
            document.querySelector("#user_ip").value = result
            fetch(`/reviewer/get_score/${result}`).then(response => response.json()).then(data => {
                document.querySelector("#userScore").value = data[0];
                MakenewQuestion(1);
                MakenewQuestion(2);
            });

            return result //MAKE A GET OR CREATE HERE
            // console.log(result);
        });
        // ===== GETTING IP ====
    }

    // Version 2

