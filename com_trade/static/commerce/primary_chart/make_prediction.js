
last_predicted_price = 0;
predicted_price = new get_accelaration()
function make_prediction(live)  {
    time    =parseFloat(live.t) /1000;
    // difference between last predicted price and current price
    predict_deviation = parseFloat(last_predicted_price) - parseFloat(live.c)
    if (predict_deviation < -500){ predict_deviation = 0}
    deviation_value = (parseFloat(predict_deviation) /   parseFloat(live.c))    *1000
    // console.log('Predict Deviation: ',predict_deviation)

    // make prediction
    make_predicted_price = predicted_price.accelarate(live.c)
    // console.log('Next Price: ', make_predicted_price)

    // Make function here
    last_predicted_price = make_predicted_price

    prediction_value = {
        time    :time,
        value   :deviation_value
    }
    prediction_series = {
        time    :parseFloat(time) + 60,
        value   :make_predicted_price
    }
    main_prediction_series.update(prediction_series);
    price_prediction_series.update(prediction_value);
    
    // Make series
}


function get_accelaration(){
    this.data = 0
    this.accelaration = 0
    this.accelaration_data = []
    this.average = (i) =>{
        if (!i){
            return this.accelaration
        }
        if (this.accelaration_data.length < 4){ //algo_adjust 4
            this.accelaration_data.push(i)
        }   else    {
            this.accelaration_data.shift()
            this.accelaration_data.push(i)
        }
    }

    this.accelarate = (accelarate) => {
        if (!accelarate){
            return this.accelaration
        }
        if (this.data == 0){
            this.data = accelarate;
            this.average(1)
            return accelarate
        } else  {
            changes = accelarate / this.data 
            this.data = accelarate;
            this.average(changes) //= this.data / accelarate 
            // console.log('changes: ',changes)
            this.accelaration = this.accelaration_data.reduce((a,b)=>{return a+b})    /   this.accelaration_data.length

            return this.accelaration * accelarate
        }    
    }
}

