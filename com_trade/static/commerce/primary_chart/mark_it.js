
function Mark_it(side,live, time){
    if (side == 'buy'){
        position    = 'belowBar';
        color       = 'rgba(119, 255, 92, 0.759)';
        shape       = 'arrowUp';
        buy_position +=1;
        buy_value += parseFloat(live.c);
        high_it     = parseFloat(live.h) * 5,
        low_it      = parseFloat(live.l)

    } else if (side == 'sell') {
        position    = 'aboveBar';
        color       = 'rgba(255, 111, 92, 0.759)';
        shape       = 'arrowDon'
        sell_position +=1;
        sell_value += parseFloat(live.c);
        high_it     = parseFloat(live.h),
        low_it      = parseFloat(live.l) * 5
    }
    mark = {
        time    :time,
        position: position,
        color   :color ,
        shape   :shape
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