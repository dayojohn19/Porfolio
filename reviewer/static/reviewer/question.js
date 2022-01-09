console.log('Static Reviewr Question Loaded\n\n')

    function isRight(value, id){
        // answer=0;
        // container=0;
        if (id == 'a1' || id == 'b1')   {
            answer = document.querySelector("#container-1-answer").innerHTML;
            question    =document.querySelector("#container-1-question").innerHTML;
            console.log('ans',answer)
            container = 1
        }
        if (id == 'a2' || id == 'b2') {
            answer = document.querySelector("#container-2-answer").innerHTML;
            question    =   document.querySelector("#container-2-question").innerHTML;
            container = 2
            console.log('ans',answer)

        }
        totalSeconds = 0;
        checkAnswer(value, answer, container, question)
        
        // checkAnswer(value, answer)
    }

    function checkAnswer(value, answer, container, question){

        if (answer == value) {
            addScore('correct');
            changeContainer(container);
            // alert('Correct: '+answer);
            // newQuestion(container);
        } else if (answer != value) {
            addScore('wrong');
            // alert(answer);
            // prompt('Your: \n  | Moblie Number |  or  | Email Address | ', '');
        }
        prompt(question,answer);
    }
    // BECAUSE NEGATIVE IT FAILS
    function AddScoretoDatabase(side){
        // score=0;
        // tries=0;
        // result=0;
        // try {
            score= document.querySelector("#userScore").value;
            tries=  document.querySelector("#tries").value;
            user_ip = document.querySelector("#user_ip").value;
            fetch(`/reviewer/add_score/${side}/${tries}/${score}/${user_ip}`).then(response => response.json()).then(result => {
                console.log('RESULT: ',result)  
            })
        // }
        // catch(err){}
        

    }
                        // console.log(result);



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
        // console.log('NumScore',numScore)
        document.querySelector("#userFunction").value = your_function;
        // console.log("second Function ",your_function)
        // fetch add to database
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
        // newQuestion(container)
        MakenewQuestion(container)
    }

    // function newQuestion(container) {
    function newQuestion(container, FinalAnswer, FinalQuestion, WrongAnswer) {

        // console.log('container',container);
        // newSet = new MakenewQuestion()
        // console.log(newSet)
        // console.log('NewSet: ',newSet.FinalAnswer)
        // console.log(newSet)
        // test_question   =FinalQuestion
        // test_answer =FinalAnswer
        // test_wrong  =WrongAnswer
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
            console.log('done container1')
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
            console.log('done container2')
            // correct answer
            buttonCorrect = document.querySelector(`#${getRandomString()+2}`)
            buttonCorrect.value = FinalAnswer;
            buttonCorrect.innerHTML = FinalAnswer;
        }
    }

    // function SaveData(fq, fa, wa){
    //     // console.log(fq, fa, wa)
    //     this.answer = fa
    //     var fq = fq
    //     return [fq, fa, wa]
    // }
    function MakenewQuestion(container){
        // ---------- algo_adjusts score_function ---------
        console.log('Making New')
        // var FinalAnswer = [];
        // fetch("{% url 'reviewer:new_question'%}").then((r) => r.json()).then(data=>{
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
            console.log("YOUR FUNCTION", your_function)
        // fetch('/reviewer/new_question').then((r) => r.json()).then(data=>{
        fetch(window.location.pathname+'/'+your_function+'/getit').then((r) => r.json()).then(data=>{
        // fetch('questions/deck/management/getit').then((r) => r.json()).then(data=>{

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
            console.log('Makenew: ', data)
            newQuestion(container, FinalAnswer, FinalQuestion, WrongAnswer)
        });
    }
    console.log('Make: ',MakenewQuestion())

function getRandomString() {
    var randomChars = 'ab';
    var result = '';
    for ( var i = 0; i < 1; i++ ) {
        result += randomChars.charAt(Math.floor(Math.random() * randomChars.length));
    }
    return result;
}



// USER ACTIVITY
user_acticvity()
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
                     })
                    alert('Thank you')
                    //insert fetch to save
                }   
            }
            if (result == 'first_time'){
                alert('We are accepting Cookies.')
            }
            console.log('Result: ',result);
            document.querySelector("#user_ip").value = result
            fetch(`/reviewer/get_score/${result}`).then(response => response.json()).then(data => {
                document.querySelector("#userScore").value  =   data[0];
                // document.querySelector("#tries").value      =   data[1];
                MakenewQuestion(1);
                MakenewQuestion(2);
                
            });
            
            return result //MAKE A GET OR CREATE HERE
            // console.log(result);
        });
        // ===== GETTING IP ====
    }
    // x = user_acticvity()
