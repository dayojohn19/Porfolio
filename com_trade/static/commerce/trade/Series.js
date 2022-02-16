
markers = [];

// ----------------------------
// ---------- Series ----------
// ----------------------------
var CandleSeries = chart.addCandlestickSeries({
  upColor: 'rgba(255, 144, 0, 1)',
  downColor: 'red',
  borderDownColor: 'red',
  borderUpColor: 'rgba(255, 144, 0, 1)',
  wickDownColor: 'rgba(255, 144, 0, 1)',
  wickUpColor: 'rgba(255, 144, 0, 1)',
});


const CalculatedSeries = chart.addLineSeries({
    priceScaleId: 'left',
    title: '',
    scaleMargins: {
        top: 0.5,
        bottom: 0.5,
    },
// ANIMATION
    color: 'red',
    lineStyle: 0,
    lineWidth: 1,
    crosshairMarkerVisible: true,
    crosshairMarkerRadius: 6,
    crosshairMarkerBorderColor: '#ffffff',
    crosshairMarkerBackgroundColor: '#2296f3',
    // lineType: 1,
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
});








// ************************************
// ************ End Series ************
// ************************************

var respond;
var message = document.querySelector("#message");
rsi_data = [1,2,3,4,5,6,7,8];








// function put_volume_quote(){
//     for (let i = 0; i < respond.length; i++) { 
//         var volume_quote = {
//             time: parseInt(respond[i][0]),
//             value: ((parseFloat(respond[i][4]) / parseFloat(respond[i][8]))*parseFloat(15)) 
//         }
//         PriceOVolumeTrade.update(volume_quote);
//     }
//      message.innerHTML = 'Price over Trade'
// }


console.log('Series Loaded');