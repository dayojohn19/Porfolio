
//   var h = document.createElement("H1");
//   var t = document.createTextNode("Volume / Trade");
//   h.appendChild(t);
//   document.body.appendChild(h);


var chart_volume = LightweightCharts.createChart(document.body, {
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
        // rightOffset: 3,
        // barSpacing: 12,
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

  var h = document.createElement("H1");
  var t = document.createTextNode("Volume Quote / Trade and Price / Trade");
  h.appendChild(t);
  document.body.appendChild(h);


// var chart_PVT = LightweightCharts.createChart(document.body, {
// 	width: 600,
//   height: 300,
// 	layout: {
// 		backgroundColor: '#000000',
// 		textColor: 'rgba(255, 255, 255, 0.9)',
// 	},
// 	grid: {
// 		vertLines: {
// 			color: 'rgba(197, 203, 206, 0.5)',
// 		},
// 		horzLines: {
// 			color: 'rgba(197, 203, 206, 0.5)',
// 		},
// 	},
// 	crosshair: {
// 		mode: LightweightCharts.CrosshairMode.Normal,
// 	},
// 	rightPriceScale: {
// 		borderColor: 'rgba(197, 203, 206, 0.8)',
// 	},
// 	timeScale: {
// 		borderColor: 'rgba(197, 203, 206, 0.8)',
// 	},
// });

var chart_PVT = LightweightCharts.createChart(document.body, {
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

console.log('Fully Loaded');