// Main Chart Series


// SAMPLE DATAS
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
    
    for (let i = 3; i < respond.length; i++) { 
        main = {
            time : parseFloat(respond[i][0])/1000,
            open : parseFloat(respond[i][1]),
            high : parseFloat(respond[i][2]),
            low  : parseFloat(respond[i][3]),
            close: parseFloat(respond[i][4])
        }
        main_series.update(main);

        volume_per_trade = { //'rgba(21, 146, 230, 1)'
            time : parseFloat(respond[i][0])/1000,
            value:  parseFloat(respond[i][5]) / parseFloat(respond[i][8]) * 15 ,// 18 adjust algo_adjust
        }
        volume_trade_series.update(volume_per_trade);

        
        volume_per_price = { //'rgba(253, 201, 103, 0.76)'
            time : parseFloat(respond[i][0])/1000,
            value:  parseFloat(respond[i][5]) /  parseFloat(respond[i][4])
        }
        volume_price_series.update(volume_per_price);

        volume_per_base = { //rgba(213, 255, 63, 0.829)'
            time : parseFloat(respond[i][0])/1000,
            value: (parseFloat(respond[i][9])  /  parseFloat(respond[i][5]) ) * 1.12 // 1.12 adjust algo_adjust
        }
        volume_base_series.update(volume_per_base);

        price_line = { //'rgba(38, 250, 38, 0.753)'
            time : parseFloat(respond[i][0])/1000,
            value: parseFloat(respond[i][1]) / 60000,       // Close 4  Open 1
        }
        price_line_series.update(price_line)

        // set marker 
        if (price_line.value > volume_per_base.value && volume_per_base.value > volume_per_price.value > volume_per_trade.value ){
            markers.push({
                time: parseFloat(respond[i][0])/1000,
                position: 'aboveBar',
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

                // x=1

            // } else {
                            markers.push({
                    time : (parseFloat(respond[i][0])/1000 )+ 2,
                    position: 'aboveBar',
                    color: 'rgba(253, 201, 103, 0.76)',
                    shape: 'arrowDown', 
                });
                x=0
            // }
                console.log('BUY_1')
                buy_position +=1
                buy_value += price_line.value
        }  

    }
    // console.log(markers);
    main_series.setMarkers(markers);
    // main_series.setMarkers(sell_markers, markers);

    volume_price_series.setMarkers(markers);
    // volume_price_series.setMarkers(sell_markers);

    console.log('SELL position: ',sell_position, '\n Value: ', sell_value);
    console.log('BUY position: ', buy_position , '\n Value: ', buy_value);
}
//// LONG TERM END



