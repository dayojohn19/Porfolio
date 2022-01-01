// Main Chart Series


// SAMPLE DATAS
    1499040000000,      // Open time 0   (t)
    "0.01634790",       // Open 1       (o)
    "0.80000000",       // High 2       (h)
    "0.01575800",       // Low 3        (l)
    "0.01577100",       // Close 4      (c)
    "148976.11427815",  // Volume 5     (v)  Base asset volume
    1499644799999,      // Close time 6 (T)
    "2434.19055334",    // Quote asset volume 7     (q)
    308,                // Number of trades 8       (n)
    "1756.87402397",    // Taker buy base asset volume 9    (v) Base asset volume
    "28.46694368",      // Taker buy quote asset volume 10  (q) Quote asset volume
    "17928899.62484339" // Ignore. 11

get_data()
function get_data() {
    fetch("fetch_data").then((r) => r.json()
    .then((response) =>{
        // Insteer all the functions here
            put_series(response);
    }))
}
// LONG TERM START


function    put_series(respond){
    markers=[];
    sell_markers = [];
    x=0
    sell_position = 0;
    buy_position = 0;
    sell_value = 0;
    buy_value = 0;
    black_position = 0
    test_cases = []
    
    for (let i = 0; i < respond.length; i++) { 
        main = {
            time : parseFloat(respond[i][0])/1000,
            open : parseFloat(respond[i][1]),
            high : parseFloat(respond[i][2]),
            low  : parseFloat(respond[i][3]),
            close: parseFloat(respond[i][4])
        }
        main_series.update(main);
        // CHANGING INTERVAL algo_adjust adjust

        interval_per_minute_test_case(respond, i)
        // interval_per_minute(respond, i)
        // interval_per_day(respond, i)
    }

    
    
    
    // ======== GET THE LOWEST AND HIGHEST TESTCASE VALUE

//     case_max = Math.max.apply(Math, test_cases.map(function(o) { return o.ratio }))
//     case_min = Math.min.apply(Math, test_cases.map(function(o) { return o.ratio }))
// // ====--------
//     get_Average_Ratio(test_cases)
// // ======--------
//     console.log('Highest CASE: ', case_max);
//     console.log('Lowest CASE: ',case_min);
//     console.log('Max Average: ',max_average)
//     console.log('Min Average: ', min_average)
//     function sortByKey(array, key) {
//         return array.sort(function(a, b) {
//             var x = a[key]; var y = b[key];
//             return ((x < y) ? -1 : ((x > y) ? 1 : 0));
//         });
//     }
//     assorted = sortByKey(test_cases, 'ratio')
//     console.log(assorted)


    volume_price_series.setMarkers(markers);
    main_series.setMarkers(markers);
    get_profit([buy_position, sell_position], [buy_value, sell_value]);
}
//// LONG TERM END


function get_profit(position, value){
    buy_position  = position[0];
    sell_position = position[1]

    buy_value = value[0];
    sell_value = value[1];


    buy_ratio = parseFloat(buy_value) / parseFloat(buy_position);
    sell_ratio = parseFloat(sell_value) / parseFloat(sell_position);
// test
    console.log('Black Posistions: ',black_position)
    console.log('Markers: ',markers)

    console.log('SELL position: ',sell_position, '\n Value: ', sell_value);
    console.log('BUY position: ', buy_position , '\n Value: ', buy_value);
    trade_diff =  parseFloat(sell_position) - parseFloat(buy_position);
    console.log('Trade Difference: ', trade_diff)

    console.log('Buying Ratio Must be lower.....')
    console.log('buy Ratio: ', buy_ratio.toFixed(3) +" per Trade");
    console.log('sell Ration: ', sell_ratio.toFixed(3) +" per Trade");
    // ratio_total  = parseFloat(buy_ratio) + parseFloat(sell_ratio);
    // console.log('Total: ', ratio_total );
    ratio_diff = parseFloat(sell_ratio) - parseFloat(buy_ratio)
    console.log('Ratio Diff: ',  ratio_diff.toFixed(5))
    ratio_percentage = (parseFloat(ratio_diff) / parseFloat(buy_ratio) ) * 100
    console.log('Profit Percentage: ', ratio_percentage.toFixed(5)+'%' )

}
// intervals


function interval_per_minute(respond, i) {
        volume_per_trade = { //'rgba(21, 146, 230, 1)'
            time : parseFloat(respond[i][0])/1000,
            value:  parseFloat(respond[i][5]) / parseFloat(respond[i][8]) * 8.75//8 //algo adjust
        }
        volume_trade_series.update(volume_per_trade);

        
        volume_per_price_close = { //'rgba(253, 201, 103, 0.76)'
            time : parseFloat(respond[i][0])/1000,
            value:  parseFloat(respond[i][5]) /  parseFloat(respond[i][4]) *15//*150 //algo adjust
        }
        volume_price_series.update(volume_per_price_close);

        volume_per_price_open = { //rgba(255, 235, 198, 0.76)
            time    :parseFloat(respond[i][0])  /   1000,
            value   :parseFloat(respond[i][5])  /   parseFloat(respond[i][1]) * 350 // 350 algo adjust
        }
        volume_price_open_series.update(volume_per_price_open)

        volume_per_base = { //rgba(213, 255, 63, 0.829)'
            time : parseFloat(respond[i][0])/1000,
            value: (parseFloat(respond[i][9])  /  parseFloat(respond[i][5]) ) *.8
        }
        volume_base_series.update(volume_per_base);

        price_line = { //'rgba(38, 250, 38, 0.753)'
            time : parseFloat(respond[i][0])/1000,
            value: parseFloat(respond[i][1]) / 96000,      
        }
        price_line_series.update(price_line)





            if (price_line.value > volume_per_trade.value && volume_per_trade.value > volume_per_base.value    &&  volume_per_base.value    >   volume_per_price_open.value || volume_per_base.value    <  volume_per_price_open.value  &&  volume_per_price_open.value  >   volume_per_price_close.value    ){
                markers.push({
                    time: parseFloat(respond[i][0])/1000,
                    position: 'belowBar',
                    color: 'rgba(38, 250, 38, 0.753)', 
                    shape: 'arrowUp'
                })
                buy_position +=1;
                buy_value += price_line.value
                console.log('BUY')
            }
            if (volume_per_trade.value > price_line.value && price_line.value > volume_per_price_open.value && volume_per_price_open.value > volume_per_base.value && volume_per_base.value > volume_per_price_close.value){
                markers.push({
                    time: parseFloat(respond[i][0])/1000,
                    position    :'aboveBar',
                    color       :'rgba(255, 113, 94, 0.608)',
                    shape       :'arrowDown'
                });
                sell_position +=1;
                sell_value += price_line.value;
                console.log('SELL')
            }

            if (volume_per_trade.value > price_line.value &&
                price_line.value > volume_per_base.value &&
                volume_per_base.value > volume_per_price_open.value &&
                volume_per_price_open.value > volume_per_price_close.value
                )   {
                    markers.push({
                        time    :parseFloat(respond[i][0])/1000,
                        position    :'aboveBar',
                        color   :'black',
                        shape   :'arrowDown'
                    });
                    black_position +=1;
            }
// ======== === ==  END CONSTRAINTS =====   ====    ==  =

}

function interval_per_minute_test_case(respond, i) {
        volume_per_trade = { //'rgba(21, 146, 230, 1)'
            time : parseFloat(respond[i][0])/1000,
            value:  parseFloat(respond[i][5]) / parseFloat(respond[i][8]) * 9//8
        }
        volume_trade_series.update(volume_per_trade);

        
        volume_per_price_close = { //'rgba(253, 201, 103, 0.76)'
            time : parseFloat(respond[i][0])/1000,
            value:  parseFloat(respond[i][5]) /  parseFloat(respond[i][4]) *150
        }
        volume_price_series.update(volume_per_price_close);

        volume_per_price_open = { //rgba(255, 235, 198, 0.76)
            time    :parseFloat(respond[i][0])  /   1000,
            value   :parseFloat(respond[i][5])  /   parseFloat(respond[i][1]) * 300
        }
        volume_price_open_series.update(volume_per_price_open)

        volume_per_base = { //rgba(213, 255, 63, 0.829)'
            time : parseFloat(respond[i][0])/1000,
            value: (parseFloat(respond[i][9])  /  parseFloat(respond[i][5]) ) *.9
        }
        volume_base_series.update(volume_per_base);

        price_line = { //'rgba(38, 250, 38, 0.753)'
            time : parseFloat(respond[i][0])/1000,
            value: parseFloat(respond[i][1]) / 96000,      
        }
        price_line_series.update(price_line)




    // ================================== TEST CASES ==================================
    trade   =volume_per_trade.value;
    closeit   =volume_per_price_close.value;
    openit    =volume_per_price_open.value;
    base    =volume_per_base.value;
    line    =price_line.value;
    time    =parseFloat(respond[i][0])/1000,
    // console.log(trade,closeit,openit,base,line)
        for_Each_Constraints(trade,closeit,openit,base,line, time)

}

    function interval_per_day(respond, i){
            volume_per_trade = { //'rgba(21, 146, 230, 1)'
            time : parseFloat(respond[i][0])/1000,
            value:  parseFloat(respond[i][5]) / parseFloat(respond[i][8]) * 18,// 18 adjust algo_adjust **IF BY DAY/YEAR VALUE=15
            // * 18 if PER DAY
        }
        volume_trade_series.update(volume_per_trade);

        
        volume_per_price = { //'rgba(253, 201, 103, 0.76)'
            time : parseFloat(respond[i][0])/1000,
            value:  parseFloat(respond[i][5]) /  parseFloat(respond[i][4]) //adjust **IF BY DAY/YEAR=0VALUE
            // * 0 if PER DAY
        }
        volume_price_series.update(volume_per_price);

        volume_per_base = { //rgba(213, 255, 63, 0.829)'
            time : parseFloat(respond[i][0])/1000,
            value: (parseFloat(respond[i][9])  /  parseFloat(respond[i][5]) ) * 1.12// 1.12 adjust algo_adjust
            // * 1.12 IF PER DAY
        }
        volume_base_series.update(volume_per_base);

        price_line = { //'rgba(38, 250, 38, 0.753)'
            time : parseFloat(respond[i][0])/1000,
            value: parseFloat(respond[i][1]) / 60000,       // 60000 adjust algo_adjust price   Close 4  Open 1 **GET THE HIGHEST & LOWEST AVERAGE*** IF BY DAY/YEAR GET HIGHest_AND_LOWEST_AVERAGE_VALUE
            // AVERAGE IF PER DAY
        }
        price_line_series.update(price_line)

        // set marker 
        if (price_line.value > volume_per_base.value && volume_per_base.value > volume_per_price.value > volume_per_trade.value ){
            markers.push({
                time: parseFloat(respond[i][0])/1000,
                position: 'belowBar',
                color: 'rgba(38, 250, 38, 0.753)', 
                shape: 'arrowDown'
            });
            // console.log('green > yellow > browmn > blue')
            console.log('SELL_1')
            sell_position +=1;
            sell_value += price_line.value;
        }
        if (price_line.value > volume_per_price.value && volume_per_price.value > volume_per_base.value && volume_per_base.value > volume_per_trade.value) {
                markers.push({
                time: parseFloat(respond[i][0])/1000,
                position: 'aboveBar',
                color: 'rgba(38, 250, 38, 0.753)', 
                shape: 'arrowDown'
            });
            // console.log('new')
            console.log('SELL_2')
            sell_position +=1
            sell_value += price_line.value;
        }

        if (volume_per_price.value > volume_per_trade.value && volume_per_trade.value > price_line.value) {
            // if (x == 0 ){
                markers.push({
                    time : (parseFloat(respond[i][0])/1000 )- 10000,
                    position: 'belowBar',
                    color: 'rgba(253, 201, 103, 0.76)',
                    shape: 'arrowUp',
                });

                console.log('BUY_1')
                buy_position +=1
                buy_value += price_line.value
            }  
        }





    // TEST CASES TEST CASES TEST CASES
function    Constraint_series(time, side, value) {
    if (side == 'buy'){
        markers.push({
            time    :time,
            position    :'aboveBar',
            color   :'green',
            shape   :'circle'
        });
        buy_position +=1;
        buy_value += value;
    }
    if  (side == 'sell'){
        markers.push({
            time    :time,
            position    :'belowBar',
            color   :'red',
            shape   :'circle'
        });      
        sell_position +=1;
        sell_value += value;
    }
    black_position +=1;

}
function get_Average_Ratio(test_cases){
    if (test_cases.length >=450){ //algo_adjust test_case
        test_cases.shift()
    }
    case_highest_position = Math.min.apply(Math, test_cases.map(function(o) { return o.position }))
    case_highest_position_index = test_cases.find(e=>e.position == case_highest_position)
    // console.log('Index: ',case_highest_position_index)
    max_average=    parseFloat(case_highest_position_index.ratio) * 1.0020376 ;//1.0037 // algo_adjust ratio //BOOSTS SELL
    min_average=    parseFloat(case_highest_position_index.ratio) * 0.996590  ;// 9963 // algo_adjust ratio //BOOSTS BUY
    // console.log('Max Average: ',max_average)
    // console.log('Min Average: ', min_average)
}
function for_Each_Constraints(trade,close,open,base,line, time){
    testcase=0;
    arr = [trade,close,open,base,line]
        for (i1  =0; i1 <=arr.length-1;  i1++){
            for (i2 =0; i2  <=arr.length-1;   i2++){
                for (i3 =0; i3  <=arr.length-1;   i3++){
                    for (i4=0;  i4  <=arr.length-1;   i4++){
                        for (i5=0;  i5  <=arr.length-1;   i5++){
                            // console.log(arr[i1],arr[i2],arr[i3],arr[i4],arr[i5])
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

