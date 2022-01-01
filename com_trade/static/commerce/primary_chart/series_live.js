// --------->>>>>>>>

buy_value = 0;
buy_position = 0;
sell_value = 0;
sell_position = 0;
live_markers = []


console.log('Creating Socket.......')
// ============================================================
// ==================== CREATING SOCKET ====================
// ============================================================
var BinanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_1m");
// console.log(BinanceSocket);
BinanceSocket.onmessage = function (event) {
    var message = JSON.parse(event.data);
    const live = message.k
    console.log('Message: ',live.x)
    put_console(live);
}


// ============================================================
// ============================================================
// ============================================================

function put_console(live){

    timestamp = parseFloat(live.t) / 1000; //getting time                           
    line    =   parseFloat(live.o) / parseFloat(live.h) //96000                     //'rgba(38, 250, 38, 0.753)'
    openit  =   parseFloat(live.v)  /   parseFloat(live.o)   *75                   //rgba(255, 235, 198, 0.76)
    trade   =   parseFloat(live.v) / parseFloat(live.n) //*9//8//ad algo_adjust       //'rgba(21, 146, 230, 1)'
    closeit =   parseFloat(live.v) / parseFloat(live.c) *50                       //'rgba(253, 201, 103, 0.76)'
    base    =   parseFloat(live.v)  /   parseFloat(live.q)  *1000                    //rgba(213, 255, 63, 0.829)'
    

    console.log(timestamp);
    console.log('Line: ',line);
    console.log('Open: ',openit);
    console.log('Trade: ',trade);
    console.log('Close: ',closeit);
    console.log('Base: ',base);
    

}


// ============================================================
// ============================================================
// ============================================================






function Mark_it(side,live, time){
    if (side == 'buy'){
        position = 'belowBar';
        color = 'rgba(119, 255, 92, 0.759)';
        shape = 'arrowUp';
        buy_position +=1;
        buy_value += parseFloat(live.c);
        high_it = parseFloat(live.h) * 5,
        low_it = parseFloat(live.l)

    } else if (side == 'sell') {
        position = 'aboveBar';
        color = 'rgba(255, 111, 92, 0.759)';
        shape = 'arrowDon'
        sell_position +=1;
        sell_value += parseFloat(live.c);
        high_it = parseFloat(live.h),
        low_it = parseFloat(live.l) * 5
    }
    mark = {
        time:time,
        position: position,
        color:color ,
        shape:shape
    }
    trade_series = {
        time    :parseFloat(live.t),
        open    :parseFloat(live.o) , 
        high    :high_it,
        low     :low_it,
        close   :parseFloat(live.c)
    }
    main_series.update(trade_series);
    live_markers.push(mark);
    console.log('Mark it ..... Done')
}
// <<<<<<<<<------------
function main_chart_update(data){
    serie = {
        time    :parseFloat(data.t) / 1000,
        open    :parseFloat(data.o),
        high    :parseFloat(data.h),
        low     :parseFloat(data.l),
        close   :parseFloat(data.c)
    }
    main_series.update(serie)
}

// Step 1
function Go_live(live){
    // cheking if it is closed 
    if (live.x){ //if closed in 1 min is true
        main_chart_update(live)
    }///
    // going to calculations
    if (Live_calculations(live)){
        data = {
            time : parseFloat(live.t) / 1000,
            open : parseFloat(live.o),
            high : parseFloat(live.h),
            low  : parseFloat(live.l),
            close: parseFloat(live.c),
        }
    }else{
        // do nothing here
    }

}
// runs every second

function Live_calculations (live){
    //algo_adjust
    timestamp = parseFloat(live.t) / 1000; //getting time                           
    trade   =   parseFloat(live.v) / parseFloat(live.n) *9//8//ad algo_adjust       //'rgba(21, 146, 230, 1)'
    closeit =   parseFloat(live.v) / parseFloat(live.c) *150                        //'rgba(253, 201, 103, 0.76)'
    openit  =   parseFloat(live.v)  /   parseFloat(live.o)   *300                   //rgba(255, 235, 198, 0.76)
    base    =   parseFloat(live.v)  /   parseFloat(live.q)  *9                      //rgba(213, 255, 63, 0.829)'
    line    =   parseFloat[live.o]   /96000                                              //'rgba(38, 250, 38, 0.753)'

    volume_per_trade = { //'rgba(21, 146, 230, 1)'
        time    :timestamp,
        value   :trade
    }
    volume_per_price_close = { //'rgba(253, 201, 103, 0.76)'
        time:   timestamp,
        value:  closeit
    }
    volume_per_price_open   =   { //rgba(255, 235, 198, 0.76)
        time    :timestamp,
        value   :openit
    }
    volume_per_base =   {//rgba(213, 255, 63, 0.829)'
        time    :timestamp,
        value   :base
    }
    price_line = { //'rgba(38, 250, 38, 0.753)'
        time    :timestamp,
        value   :line
    }
    console.log('TimeStamp: ',timestamp);
    console.log('Trade: ',  trade);
    console.log('Close: ',  closeit);
    console.log('Open: ',   openit);
    console.log('Base: ',   base);
    console.log('Line: ',   line)

    if (live.x){
        volume_trade_series.update(volume_per_trade);
        volume_price_series.update(volume_per_price_close);
        volume_open_price_series.update(volume_per_price_open);
        volume_price_series.update(volume_per_price_close);
        price_line_series.update(price_line);
    }


    // if (!positioned)    {}
    // // ===== CONSTRAINTS =====
    // if (volume_per_trade.value >= volume_per_price.value) {
    //     Mark_it('buy',  live,   timestamp) //adding buy value or sell value

    // }
    // if (volume_per_trade.value == volume_per_price.value){
    //     Mark_it('sell', live, timestamp)
    // }

    //  =================<<<<

    return true
}




function for_Each_Constraints(trade,close,open,base,line, time){
    testcase=0;
    arr = [trade,close,open,base,line]
        for (i1  =0; i1 <=arr.length-1;  i1++){
            for (i2 =0; i2  <=arr.length-1;   i2++){
                for (i3 =0; i3  <=arr.length-1;   i3++){
                    for (i4=0;  i4  <=arr.length-1;   i4++){
                        for (i5=0;  i5  <=arr.length-1;   i5++){
                            // ---- ------ CONSTRAINTS  --------    -------
                            if (arr[i1] < arr[i2] && arr[i2] < arr[i3] && arr[i3] > arr[i4] && arr[i4] > arr[i5]){ // algo adjust greater or less than
                                //CHANGE ITS VALUE

                                if (current = test_cases.find(e=>e.case == testcase)){
                                    current.position ++;
                                    current.value += line;
                                    current.ratio = (parseFloat(current.value) * 96000) /   parseFloat(current.position)
                                    get_Average_Ratio(test_cases)
                                    if (current.ratio > max_average){
                                        // Constraint_series(time, 'sell')
                                        side = 'sell';
                                        Constraint_series(time,side,line)
                                    }
                                    if (current.ratio < min_average){
                                        side = 'buy';
                                        // Constraint_series(time, 'buy')
                                        Constraint_series(time,side,line)
                                    }
                                    
                                    // current.ratio = (parseFloat(current.value) * 96000 ) / parseFloat(current.position)
                                    // console.log('first: ',current.case,   current.value)
                                } else {
                                    new_case = {
                                        case    :testcase,
                                        position    :1,
                                        value   :line,
                                        ratio   :(parseFloat(line)* 96000) / parseFloat(1)
                                    }
                                    test_cases.push(new_case)
                                    console.log('done UPDATING' )
                                }
                            }
                            if (arr[i1] > arr[i2] && arr[i2] > arr[i3] && arr[i3] < arr[i4] && arr[i4] < arr[i5]) { // algo adjust greater or less than
                                //CHANGE ITS VALUE
                                if (current = test_cases.find(e=>e.case == testcase)){
                                    current.position ++;
                                    current.value += line;
                                    current.ratio = (parseFloat(current.value) * 96000) /   parseFloat(current.position)
                                    get_Average_Ratio(test_cases)
                                    if (current.ratio > max_average){
                                        // Constraint_series(time, 'sell')
                                        side = 'sell';
                                        Constraint_series(time,side,line)
                                    }
                                    if (current.ratio < min_average){
                                        side = 'buy';
                                        // Constraint_series(time, 'buy')
                                        Constraint_series(time,side,line)
                                    }
                                    
                                    // console.log(current.value)
                                    // console.log('second: ',current.case,   current.value)

                                } else {
                                    new_case = {
                                        case    :testcase,
                                        position    :1,
                                        value   :line,
                                        ratio   : (parseFloat(line)* 96000) / parseFloat(1)
                                    }
                                    test_cases.push(new_case)
                                    console.log('done UPDATING elseif' )
                                }
                                
                            }
                            testcase++;


                        }
                    }
                }
            }
        }
}

