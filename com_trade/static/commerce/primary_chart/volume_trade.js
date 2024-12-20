console.log('Volume / Trade Chart Loaded');

volume_trade_position = document.querySelector("#volume_trade_position");
volume_trade_option = { width: 1000, height: 300 ,
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},

};
Volume_Trade_chart = LightweightCharts.createChart(volume_trade_position, volume_trade_option);
 
Volume_Trade_chart.applyOptions({
        layout: {
        background: {
            type: LightweightCharts.ColorType.VerticalGradient,
            topColor: 'black',
            bottomColor: 'black',
        },
        textColor: 'white',
    },
    // ============= FOR Minutes Trading ============
    timeScale:	{
        rightOffset: 3,
        barSpacing: 12,
        // fixLeftEdge: true,
        // lockVisibleTimeRangeOnResize: true,
        // rightBarStaysOnScroll: true,
        // borderVisible: false,
        // borderColor: '#fff000',
        // visible: true,
        timeVisible: true,
        secondsVisible: false,
    },
    priceScale: {
        position: 'left'
    }
    // ============ END ====================

        // priceScale: {
        //     mode:3
        // }
    //     priceScale: {
    //     position: 'left',
    //     mode: 2,
    //     autoScale: true,
    //     invertScale: false,
    //     alignLabels: false,
    //     borderVisible: false,
    //     borderColor: '#555ffd',
    //     scaleMargins: {
    //         top: 0.30,
    //         bottom: 0.25,
    //     },        
    // },
    
})


volume_trade_series_option = {
    topColor: 'rgba(21, 146, 230, 0.14)',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'rgba(21, 146, 230, 1)',
    lineStyle: 0,
    lineWidth: 3,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
    crosshairMarkerBorderColor: 'rgb(255, 255, 255, 1)',
    crosshairMarkerBackgroundColor: 'rgb(34, 150, 243, 0.1)',
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
}
volume_trade_series = Volume_Trade_chart.addAreaSeries(volume_trade_series_option);
// 
volume_price_series_option = {
    topColor: 'rgba(253, 201, 103, 0.176)',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'rgba(253, 200, 103, 0.2919)',
    lineStyle: 0,
    lineWidth: 3,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
    crosshairMarkerBorderColor: 'rgba(240, 221, 185, 0.919)',
    crosshairMarkerBackgroundColor: 'rgba(255, 212, 131, 0.753)',
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
}
volume_price_series = Volume_Trade_chart.addAreaSeries(volume_price_series_option)
// 

volume_price_open_series_option = {
    topColor: 'rgba(255, 235, 198, 0.176)',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'rgba(255, 235, 198, 0.76)',
    lineStyle: 0,
    lineWidth: 3,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
    crosshairMarkerBorderColor: 'rgba(255, 235, 198, 0.76)',
    crosshairMarkerBackgroundColor: 'rgba(255, 235, 198, 0.76)',
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
}
volume_price_open_series = Volume_Trade_chart.addAreaSeries(volume_price_open_series_option)


volume_base_series_option = {
        topColor: 'rgba(213, 255, 63, 0.129)',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'rgba(201, 255, 5, 0.829)',

}
volume_base_series = Volume_Trade_chart.addAreaSeries(volume_base_series_option)


price_line_option = {
    color: 'rgba(38, 250, 38, 0.753)',
    lineStyle: 0,
    lineWidth: 3,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 6,
    crosshairMarkerBorderColor: 'rgba(38, 250, 38, 0.753)',
    crosshairMarkerBackgroundColor: 'rgba(38, 250, 38, 0.753)',
    lineType: 12,
    // lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
}
price_line_series = Volume_Trade_chart.addLineSeries(price_line_option);


price_prediction_option = {
    color: 'orange',
    lineStyle: 0,
    lineWidth: 3,
    crosshairMarkerVisible: true,
    crosshairMarkerRadius: 6,
    crosshairMarkerBorderColor: 'orange',
    crosshairMarkerBackgroundColor: 'orange',
    lineType: 1,
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
}
price_prediction_series = Volume_Trade_chart.addLineSeries(price_prediction_option);


// volume_price_series = Main_chart.addAreaSeries(volume_price_series_option)
// volume_trade_series = Main_chart.addAreaSeries(volume_trade_series_option);

