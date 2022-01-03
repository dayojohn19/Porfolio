
// --------->>>>>>>>


live_markers = []



console.log('Creating Socket.......')
// ============================================================
// ==================== CREATING SOCKET ======================
// ============================================================
// get_live_data()
function get_live_data()    {
    var BinanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_1m");
    BinanceSocket.onmessage = function (event) {
    var message = JSON.parse(event.data);
    const live = message.k;
    // put_console(live);
    
    Go_live(live);
    console.log('\n\n --------------------------------- \n\n')
    console.log('markers: ',markers.length);
    console.log('Buy Position: ',buy_position,  buy_value);
    console.log('Sell Position: ',sell_position, sell_value);
    console.log('max_average: ',max_average)
    console.log('Min Average: ',min_average)
    console.log('Case Highest: ',case_highest_position)
    console.log('Case Hughest Index: ',case_highest_position_index)
    console.log('Case Lowest: ',case_lowest_position)
    console.log('Case Lowest Index: ',case_lowest_position_index)


    console.log('====================\n')
    console.log('Case Highest Position: ',   case_highest_position_index)
    console.log('Case Lowest Position: ',    case_lowest_position_index)
    console.log('Case Highest Ratio: ', case_highest_ratio_index)
    console.log('Case Lowest Ratio: ',  case_lowest_ratio_index)
    console.log('====================\n')

    
    console.log('\n\n --------------------------------- \n\n')
    
    
}
}

// ============================================================
// ============================================================
// ============================================================

// ============================================================
// ==================== FETCHING DATA =========================
// ============================================================
get_data()
get_live_data()

function get_data() {
    fetch("fetch_data").then((r) => r.json()
    .then((response) =>{
            for (i=0;   i<response.length;  i++)    {
                respond     =response[i]
                respond.t   =parseFloat(response[i][0])
                respond.o   =parseFloat(response[i][1])
                respond.v   =parseFloat(response[i][5])
                respond.h   =parseFloat(response[i][2])
                respond.n   =parseFloat(response[i][8])
                respond.c   =parseFloat(response[i][4])
                respond.q  =parseFloat(response[i][5])
                respond.x   =true
                // console.log('Line 1 ',respond.o)

                Go_live(respond)
            }
    }))
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






// <<<<<<<<<------------


// Step 1
function Go_live(live){

    // going to calculations
    if (Live_calculations(live)){
        console.log('\n Done Live_calculations')

        // console.log('markers: ',markers.length)
        // data = {
        //     time : parseFloat(live.t) / 1000,
        //     open : parseFloat(live.o),
        //     high : parseFloat(live.h),
        //     low  : parseFloat(live.l),
        //     close: parseFloat(live.c),
        // }
    }else{
        // do nothing here
        console.log('Failed Live_calculations')
    }

}
// runs every second

function Live_calculations (live){
    //algo_adjust
    timestamp = parseFloat(live.t) / 1000; //getting time                           

    trade   =   parseFloat(live.v) / parseFloat(live.n) *9//8//ad algo_adjust       //'rgba(21, 146, 230, 1)'
    closeit =   parseFloat(live.v) / parseFloat(live.c) *150                        //'rgba(253, 201, 103, 0.76)'
    openit  =   parseFloat(live.v)  /   parseFloat(live.o)   *300                   //rgba(255, 235, 198, 0.76)
    base    =   parseFloat(live.v)  /   parseFloat(live.q)  *0.5//9                      //rgba(213, 255, 63, 0.829)'
    line    =   parseFloat(live.v)  /   parseFloat(live.o)   *600  // parseFloat[live.o]  // /96000                                              //'rgba(38, 250, 38, 0.753)'
    line    =   parseFloat(live.o)  /   96000

// add_it
    for_Each_Constraints(trade,close,open,base,line, timestamp)
        
    make_prediction(live);
    if (live.x){
        main_chart_update(live)
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
            // value   :0.2
        }
        // console.log('TimeStamp: ',timestamp);
        // console.log('Trade: ',  trade);
        // console.log('Close: ',  closeit);
        // console.log('Open: ',   openit);
        // console.log('Base: ',   base);
        // console.log('Line: ',   line)

        volume_trade_series.update(volume_per_trade);
        volume_price_series.update(volume_per_price_close);
        volume_price_open_series.update(volume_per_price_open);
        volume_base_series.update(volume_per_base);
        price_line_series.update(price_line);

    }
    return true
}


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