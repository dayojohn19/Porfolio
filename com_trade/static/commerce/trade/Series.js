
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

// Volume Series
const RsiVolume = chart_volume.addAreaSeries({
    topColor: 'teal',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'teal',
    lineStyle: 0,
    lineWidth: 3,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,

    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
});

const RsiPrice = chart_volume.addAreaSeries({
    topColor: 'violet',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'violet',
    lineStyle: 0,
    lineWidth: 3,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
});

const VolumeTrade = chart_volume.addAreaSeries({
    topColor: 'brown',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'brown',
    lineStyle: 0,
    lineWidth: 3,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,

    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
});
const VolumeQuoteTrade = chart_volume.addLineSeries({
    topColor: 'yellow',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'yellow',
    lineStyle: 0,
    lineWidth: 3,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
});
const PriceTrade = chart_volume.addAreaSeries({
    topColor: 'yellow',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'yellow',
    lineStyle: 0,
    lineWidth: 3,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
});

const PriceOpenTrade = chart_volume.addAreaSeries({
    topColor: 'green',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'green',
    lineStyle: 0,
    lineWidth: 3,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
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

const TradeVolume = chart_volume.addLineSeries({
    color: 'blue',
    lineStyle: 0,
    lineWidth: 3,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,

    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
    // topColor: 'yellow',
    // bottomColor: 'rgba(21, 146, 230, 0)',
    // lineColor: 'yellow',
    // lineStyle: 0,
    // lineWidth: 3,
    // crosshairMarkerVisible: false,
    // crosshairMarkerRadius: 3,
    // lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
});

const TradeVolumeQuote = chart_volume.addLineSeries({
    color: 'violet',
    lineStyle: 0,
    lineWidth: 3,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,

    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
    // topColor: 'yellow',
    // bottomColor: 'rgba(21, 146, 230, 0)',
    // lineColor: 'yellow',
    // lineStyle: 0,
    // lineWidth: 3,
    // crosshairMarkerVisible: false,
    // crosshairMarkerRadius: 3,
    // lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
});

const TradePriceOpen = chart_volume.addLineSeries({
 color: '#42f54b', 

    topColor: 'teal',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'teal',
    lineStyle: 0,
    lineWidth: 1,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
});

const TradePriceClose = chart_volume.addLineSeries({
 color: 'red', 
    topColor: 'red',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'red',
    lineStyle: 0,
    lineWidth: 1,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
});

const Accelaration_Volume_Value = third_chart.addLineSeries({
 color: 'red', 
    topColor: 'red',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'red',
    lineStyle: 0,
    lineWidth: 1,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
});

const Accelarations_VolumeQuote_Value = third_chart.addLineSeries({
 color: 'blue', 
    topColor: 'blue',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'blue',
    lineStyle: 0,
    lineWidth: 1,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
    lastPriceAnimation: LightweightCharts.LastPriceAnimationMode.Continuous,
});

const AccelarationTotal_Volume= third_chart.addLineSeries({
 color: 'yellow', 
    topColor: 'yellow',
    bottomColor: 'rgba(21, 146, 230, 0)',
    lineColor: 'yellow',
    lineStyle: 0,
    lineWidth: 1,
    crosshairMarkerVisible: false,
    crosshairMarkerRadius: 3,
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