function get_data(){
    message.innerHTML = 'Fetching New Data';
    fetch("fetch_data").then((r) => r.json()).then((response) => {
    respond = response;
    console.log(response);
    message.innerHTML = 'Data Refreshed';
    put_candles();
    });

}

function new_data(){
    new_new = document.querySelector("#new_date").value;
    console.log(new_new);
    message.innerHTML = 'Fetching New Data';
    // let djurl = {% url 'trade:new_data' %};
    // let url = "{% url 'trade:new_data' %}";
    // x = new_new
    fetch(`new_data`,{
        method: 'POST',
        body: JSON.stringify({
            new_date:new_new
        })
    }).then((r) => r.json()).then((response) => {
    respond = response;
    console.log(response);
    message.innerHTML = 'Data Refreshed';
    put_candles();
    });

}


function put_candles(){
    for (let i = 0; i < respond.length; i++) { 
        var candle = {
            time : parseFloat(respond[i][0])/1000,
            open : parseFloat(respond[i][1]),
            high : parseFloat(respond[i][2]),
            low  : parseFloat(respond[i][3]),
            close: parseFloat(respond[i][4])
        }
        CandleSeries.update(candle);
    }
    message.innerHTML = 'Candles Put'
}

    1499040000000,      // Open time 0
    "0.01634790",       // Open 1 
    "0.80000000",       // High 2
    "0.01575800",       // Low 3 
    "0.01577100",       // Close 4 
    "148976.11427815",  // Volume 5
    1499644799999,      // Close time 6
    "2434.19055334",    // Quote asset volume 7
    308,                // Number of trades 8
    "1756.87402397",    // Taker buy base asset volume 9
    "28.46694368",      // Taker buy quote asset volume 10
    "17928899.62484339" // Ignore. 11

    // value_Trade = (array_Trade.reduce((a,aa) => {return a+aa})) / 14;
function Accelaration_Volume() {
    Velocity_VolumeTotal = 0;
    Volume_Marks = [];
    VolumeQuote_Marks = [];
    for (let i = 0; i < respond.length; i++) { 
        Velocity_Volume = respond[i][5];
        Velocity_VolumeQuote = respond[i][7];
        var timestamps = parseInt(respond[i][0])/1000;
        if (Volume_Marks.length >= 3){
            // val_Velocity_Volume = (Volume_Marks.reduce((a,aa) =>{return (aa-a)/aa}))
            
            v1 = (Volume_Marks[0]-Volume_Marks[1])/Volume_Marks[0];
            v2 = (Volume_Marks[1]-Volume_Marks[2])/Volume_Marks[1];
            val_Velocity_Volume = ((v1+v2)/2);

            vv1 = (VolumeQuote_Marks[0]-VolumeQuote_Marks[1])/VolumeQuote_Marks[0];
            vv2 = (VolumeQuote_Marks[1]-VolumeQuote_Marks[2])/VolumeQuote_Marks[1];
            // val_Velocity_VolumeQuote = ((vv1+vv2)/2);
            val_Velocity_VolumeQuote = vv2;
            // val_Velocity_VolumeQuote = (VolumeQuote_Marks.reduce((a,aa) =>{return (aa-a)/aa}))

            Volume_Marks.push(Velocity_Volume);
            VolumeQuote_Marks.push(Velocity_VolumeQuote);

            Volume_Marks.shift();
            VolumeQuote_Marks.shift();
        }
        else {
            Volume_Marks.push(Velocity_Volume);
            VolumeQuote_Marks.push(Velocity_VolumeQuote);
            val_Velocity_Volume = 0;
            val_Velocity_VolumeQuote = 0;
        }
        if (Velocity_VolumeTotal >= 2 ){
            Velocity_VolumeTotal = 2;
            Velocity_VolumeTotal += val_Velocity_Volume;
            Velocity_VolumeTotal += val_Velocity_VolumeQuote;
        }else if (Velocity_VolumeTotal <= -2){
            Velocity_VolumeTotal = -2;
            Velocity_VolumeTotal += val_Velocity_Volume;
            Velocity_VolumeTotal += val_Velocity_VolumeQuote;
        }else {
            Velocity_VolumeTotal += val_Velocity_Volume;
            Velocity_VolumeTotal += val_Velocity_VolumeQuote;
        }



        AccelarationTotal_Volume.update({
            time:timestamps,
            value:Velocity_VolumeTotal
        })
        Accelaration_Volume_Value.update({
            time:timestamps,
            value: val_Velocity_Volume
        });
        Accelarations_VolumeQuote_Value.update({
            time:timestamps,
            value: val_Velocity_VolumeQuote
        });



    }
}
function Over_Trade(){
    isBuy = false;

    for (let i = 0; i < respond.length; i++) {
        var timestamps = parseInt(respond[i][0])/1000;

        trades = parseFloat(respond[i][8]);
        VolumeTraded = respond[i][5];
        VolumeQuoteTraded = respond[i][7];
        PriceOpen =  respond[i][1];
        PriceClose =  respond[i][4];
        TradeVolumeQuoteValue = VolumeQuoteTraded / VolumeTraded
// Violet
        TradeVolumeQuote.update({
            time:timestamps,
            value: TradeVolumeQuoteValue
        });

        TradePriceOpen.update({
            time:timestamps,
            value: PriceOpen
        });
        
        TradePriceClose.update({
            time:timestamps,
            value: PriceClose
        });
        if (PriceOpen >= PriceClose &&  PriceClose >= TradeVolumeQuoteValue){
            markers.push({
                time:parseInt(respond[i][0])/1000,
                position: 'aboveBar',
                color: 'yellow',
                shape: 'arrowUp',
            });
            console.log('BUY');
        } else {
            console.log('SELL');
        }
        if (TradeVolumeQuoteValue >= PriceClose && PriceClose >= PriceOpen && TradeVolumeQuoteValue >= PriceOpen){
            markers.push({
                time:parseInt(respond[i][0])/1000,
                position: 'aboveBar',
                color: 'green',
                shape: 'arrowDown',
            });
            console.log('BUY');
        } else {
            console.log('SELL');
        }
        if ( PriceClose >= TradeVolumeQuoteValue && PriceClose >= PriceOpen && TradeVolumeQuoteValue >= PriceOpen){
            if (isBuy != true){
                markers.push({
                    time:parseInt(respond[i][0])/1000,
                    position: 'aboveBar',
                    color: 'red',
                    shape: 'arrowUp',
                });
                console.log('BUY');
                isBuy= true;
                isMarked = true;
            }


        } else {
            if (isBuy != false) {
                markers.push({
                    time:parseInt(respond[i][0])/1000,
                    position: 'aboveBar',
                    color: 'blue',
                    shape: 'arrowDown',
                });
                console.log('SELL');
                isBuy= false;
            }

            
        }
// Blue
        // TradeVolume.update({
        //     time:timestamps,
        //     value: VolumeTraded * 100
        // })
    };
    TradeVolumeQuote.setMarkers(markers);
    CandleSeries.setMarkers(markers);
}

function put_volume(){
        array_Trade = [];
        array_Quote = [];
        array_Price = [];
    // volume 5 / trade 8 --- red
    for (let i = 0; i < respond.length; i++) { 
        var timestamps = parseInt(respond[i][0])/1000
        var ValuePrice = (parseFloat(respond[i][1]) / respond[i][8])*.005;
        var ValueVolume = parseFloat(respond[i][5]) / respond[i][8];

        // ****** ADDING RSI *********
        // ****** ADDING RSI *********
        // ****** ADDING RSI *********
        // array_Trade.push(parseFloat(respond[i][5]) / respond[i][8]);
        // console.log(array_Trade);
        array_Trade.push(parseFloat(respond[i][8])); //Trade
        array_Quote.push(parseFloat(respond[i][7])); // Quote Volume
        array_Price.push(parseFloat(respond[i][4]));

        if (array_Quote.length == 14) {
            value_Trade = (array_Trade.reduce((a,aa) => {return a+aa})) / 14;
            value_quote = (array_Quote.reduce((a,aa)=>{return a+aa})) / 14;
            value_Price = (array_Price.reduce((a,aa)=>{return a+aa})) / 14;

            rsi_volume_value = parseFloat(((value_Trade/value_quote)) + 1);
            // rsi_volume_value = 100 - 100 / rsi_volume_value;
            rsi_price_value = parseFloat(100/((value_Price/value_Trade)));
            
            array_Price.shift();
            array_Quote.shift();
            array_Trade.shift();
            console.log(array_Quote);
        }
        else 
        {
            rsi_volume_value = 0;
            rsi_price_value  = 0;
        }
        var rsi_volume = {
            time : timestamps,
            value: rsi_volume_value * ValueVolume 
        }
        var rsi_price = {
            time: timestamps,
            value: rsi_price_value* ValueVolume * ValuePrice
        }
        console.log(rsi_volume_value);

        // ********
        // ********
        // ********
        // ********


        var volume = {
            time : parseInt(respond[i][0])/1000,
            value: ValueVolume
        };
        // yellow
        var volume_quote = {
            time : parseInt(respond[i][0])/1000,
            // value:   (((parseFloat(respond[i][7]) / respond[i][8])/100)*ValuePrice)/ValueVolume
            // value:  (ValueVolume/ValuePrice) / (parseFloat(respond[i][5]) / respond[i][8] )
            value: parseFloat(respond[i][7] / respond[i][8])*.005
        };
        // ------------- close 5, open 1 --- green 
        var price = {
            time: parseInt(respond[i][0])/1000,
            // value: (parseFloat(respond[i][4]) / respond[i][8])*.005
            value: ValuePrice
        }
        if (price.value >= volume.value) {
            markers.push({
                time:parseInt(respond[i][0])/1000,
                position: 'aboveBar',
                color: 'yellow',
                shape: 'arrowUp',
            });
            console.log('BUY');
        } else {
            console.log('SELL');
        }

        var priceOpen = {
            time : parseInt(respond[i][0])/1000,
            // value: (parseFloat(respond[i][1]) / respond[i][8])*.005
            value: ValuePrice
        }
        // --------------------
        RsiPrice.update(rsi_price);
        RsiVolume.update(rsi_volume);
        VolumeTrade.update(volume);
        // VolumeQuoteTrade.update(volume_quote);
        PriceTrade.update(price);
        PriceOpenTrade.update(priceOpen);
    }

    message.innerHTML = 'Volume over Trade'
    PriceTrade.setMarkers(markers);
    CandleSeries.setMarkers(markers);
}

// volume over volume quote

function rsi_volume() {
    array_volume = [];
    array_quote = [];


    for (let i = 0; respond.length; i++){

        array_volume.push(respond[i][5] / respond[i][8]);
        array_quote.push(respond[i][7] / respond[i][8]);

        if (array_quote.length == 14) {
            value_volume = (array_volume.reduce((a,aa) => {return a+aa})) / 14;
            value_quote = (array_quote.reduce((a,aa)=>{return a+aa})) / 14;
            rsi_volume_value = 100-(100/1+(value_quote/value_volume));
            array_quote.shift();
            array_volume.shift();
        }
        else 
        {
            rsi_volume_value = 0;
        }
        
        
    }
}


function get_rsi(){
    

    var value = 0;
    var newValue = 2

    if (rsi_data.length != 14){
        rsi_data.push(newValue);
    } else {
        rsi_data.shift();
        rsi_data.push(newValue);
        value = (rsi_data.reduce((a, aa )=>{ return a+aa})) / rsi_data.length

    }
    console.log(value);
    console.log(rsi_data);
}


function RSI(){
        array_volume = [];
    array_quote = [];


    for (let i = 0; i <= respond.length; i++){
        // array_volume.push(parseFloat(respond[i][5]) / respond[i][8]);
        // console.log(array_volume);
        array_volume.push(parseFloat(respond[i][5]) / respond[i][8]);
        array_quote.push(parseFloat(respond[i][7]) / respond[i][8]);

        if (array_quote.length == 14) {
            value_volume = (array_volume.reduce((a,aa) => {return a+aa})) / 14;
            value_quote = (array_quote.reduce((a,aa)=>{return a+aa})) / 14;
            rsi_volume_value = (100-(100/1+(value_quote/value_volume)))*100;
            array_quote.shift();
            array_volume.shift();
        }
        else 
        {
            rsi_volume_value = 0;
        }
        console.log(rsi_volume_value);
    }
    console.log(array_volume);
    console.log(array_quote);
}