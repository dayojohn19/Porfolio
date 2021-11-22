var chart = LightweightCharts.createChart(document.body, {
	width: 1200,
  height: 300,
	layout: {
		backgroundColor: '#000000',
		textColor: 'rgba(255, 255, 255, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	rightPriceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale:	{
        rightOffset: 3,
        barSpacing: 12,
        fixLeftEdge: true,
        lockVisibleTimeRangeOnResize: true,
        rightBarStaysOnScroll: true,
        borderVisible: false,
        borderColor: '#fff000',
        visible: true,
        timeVisible: true,
        secondsVisible: false,
    },
});

console.log('Chart Loaded');




        var candleSeries = chart.addCandlestickSeries({
            upColor: 'rgba(255, 144, 0, 1)',
            downColor: 'red',
            borderDownColor: 'red',
            borderUpColor: 'rgba(255, 144, 0, 1)',
            wickDownColor: 'rgba(255, 144, 0, 1)',
            wickUpColor: 'rgba(255, 144, 0, 1)',
        });

        const PriceSeries = chart.addLineSeries({
            priceScaleId: 'left',
            // priceScaleId: 'left',
            title: '',
            scaleMargins: {
                top: 0.5,
                bottom: 0.5,
            },
            // ANIMATION
            color: '#f48fb1',
            lineStyle: 0,
            lineWidth: 1,

            crosshairMarkerVisible: true,
            crosshairMarkerRadius: 6,
            crosshairMarkerBorderColor: '#ffffff',
            crosshairMarkerBackgroundColor: '#2296f3',
            // lineType: 1,
            lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,

        });

        const ThirdSeries = chart.addLineSeries({
            priceScaleId: 'left',
            // title: 'Series title example',

            scaleMargins: {
                top: 0.1,
                bottom: 0.3,

            },
        });





    markers = []
    console.log('ENDED');
        var BinanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_1m");
        var ii = 0
        // var tradeDiv = document.querySelector("#trades");
        BinanceSocket.onmessage = function (event) {
            // console.log(event.data)
            // chart.removeSeries(PriceSeries);
            var message = JSON.parse(event.data);
            // console.log(message.E);
            var candles = message.k;
            // console.log(candles);
            candleSeries.update({
                time: message.E/1000,
                // time: Date.now(),
                // time: Date.now(),
                open: candles.o,
                high: candles.h,
                low: candles.l,
                close: candles.c,
            });
            // PriceSeries.update({
            //     time:message.E,
            //     value:candles.c,
            // });
            // PriceSeries.setData({
            //     time:parseFloat(message.E)+parseFloat(400),
            //     value:parseFloat(candles.c)+parseFloat(25),
            // });
            PriceSeries.setData([
                { time: message.E, value: candles.c },
                { time: parseFloat(message.E) + parseFloat(400), value: parseFloat(candles.c) + parseFloat(15) },
                { time: parseFloat(message.E) + parseFloat(1000), value: parseFloat(candles.c) + parseFloat(50) },
            ]);

            ThirdSeries.setMarkers(markers);
            markers.push({
                time: parseFloat(message.E) + parseFloat(800),
                position: 'aboveBar',
                color: 'yellow',
                shape: 'arrowDown',
            });

            ThirdSeries.update({
                time: parseFloat(message.E) + parseFloat(800),
                value: parseFloat(candles.c) + parseFloat(50),
            });

            // added = message.E;
            // newadded = parseFloat(message.E)+parseFloat(10000)
            // added = new Date(added);
            // newadded = new Date(newadded);
            // console.log(added);
            // console.log(newadded);
        }
        console.log('ENDED');