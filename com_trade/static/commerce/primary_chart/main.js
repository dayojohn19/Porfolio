console.log('Main loaded')


main_position = document.querySelector("#main_position");
main_option = { width: 1000, height: 300 ,
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
    autoScale: true,
    invertScale: false,
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
    // priceScale: {indexedDB}
};
const Main_chart = LightweightCharts.createChart(main_position, main_option);



// Main_chart.applyOptions({
//         priceScale: {
//         position: 'right',
//         mode: 3,
//         drawTicks: false,
        
//     },
    
// })

main_series_option = {
    upColor: "green",
    downColor: "red",
    borderDownColor: "yellow",
    borderUpColor: "blue",
    wickDownColor:"gray",
    wickUpColor:"black",
}
const main_series = Main_chart.addCandlestickSeries(main_series_option);


// data_set = fetch("fetch_data").then((r) => r.json())
// put_series(data_set)
// .then((response) => {
    
// }

// console.log(data_set)