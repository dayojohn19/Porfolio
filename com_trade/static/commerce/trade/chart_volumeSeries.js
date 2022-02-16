// import { chart_volume } from './chart_volume.js'

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

const VolumeSeriesBlue = chart_volume.addLineSeries({
    color: 'blue',
    lineStyle: 2,
    lineWidth: 3,

});
const VolumeSeriesRed = chart_volume.addLineSeries({
    color: 'red',
    lineStyle: 2,
    lineWidth: 3,
});
const VolumeSeriesOrange = chart_volume.addLineSeries({
    color: 'orange',
    lineStyle: 2,
    lineWidth: 3,
});
const VolumeSeriesGreen = chart_volume.addLineSeries({
    color: 'green',
    lineStyle: 2,
    lineWidth: 3,
});


// export { TradePriceClose,TradePriceOpen,TradeVolumeQuote, TradeVolume, PriceOpenTrade, PriceTrade, VolumeQuoteTrade, VolumeTrade, RsiPrice, RsiVolume }