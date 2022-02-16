// import { third_chart } from './chart_third.js'




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

const AccelarationTotal_Volume = third_chart.addLineSeries({
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


// export { Accelaration_Volume_Value, Accelarations_VolumeQuote_Value, AccelarationTotal_Volume }