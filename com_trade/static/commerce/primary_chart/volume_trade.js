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
        // priceScale: {
        //     mode:3
        // }
    //     priceScale: {
    //     position: 'right',
    //     mode: 2,
    //     autoScale: false,
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
    topColor: 'rgba(21, 146, 230, 0.4)',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'rgba(21, 146, 230, 1)',
    lineStyle: 0,
    lineWidth: 1,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
    crosshairMarkerBorderColor: 'rgb(255, 255, 255, 1)',
    crosshairMarkerBackgroundColor: 'rgb(34, 150, 243, 1)',
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
}
volume_trade_series = Volume_Trade_chart.addAreaSeries(volume_trade_series_option);
// 
volume_price_series_option = {
        topColor: 'rgba(253, 201, 103, 0.76)',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'rgba(253, 200, 103, 0.919)',
    lineStyle: 0,
    lineWidth: 1,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
    crosshairMarkerBorderColor: 'rgba(240, 221, 185, 0.919)',
    crosshairMarkerBackgroundColor: 'rgba(255, 212, 131, 0.753)',
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
}
volume_price_series = Volume_Trade_chart.addAreaSeries(volume_price_series_option)
// 


volume_base_series_option = {
        topColor: 'rgba(213, 255, 63, 0.829)',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'rgba(201, 255, 5, 0.829)',

}
volume_base_series = Volume_Trade_chart.addAreaSeries(volume_base_series_option)


price_line_option = {
    color: 'rgba(38, 250, 38, 0.753)',
    lineStyle: 0,
    lineWidth: 1,
    crosshairMarkerVisible: true,
    crosshairMarkerRadius: 6,
    crosshairMarkerBorderColor: 'rgba(38, 250, 38, 0.753)',
    crosshairMarkerBackgroundColor: 'rgba(38, 250, 38, 0.753)',
    lineType: 1,
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
}
price_line_series = Volume_Trade_chart.addLineSeries(price_line_option);


// volume_price_series = Main_chart.addAreaSeries(volume_price_series_option)
// volume_trade_series = Main_chart.addAreaSeries(volume_trade_series_option);

