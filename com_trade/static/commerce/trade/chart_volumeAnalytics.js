var rsis = []
var PrevAverageGain = 0
var prevAverageLoss = 0

function GetRSI(val1, val2) {
    var change = val2 - val1

    if (rsis.length > 13) {
        if (PrevAverageGain == 0) {
            var UpAverage = []
            var DownAverage = []

            rsis.map((n) => {
                if (n > 0) {
                    UpAverage.push(n)
                } else {
                    DownAverage.push(n)
                }
            })

            try {
                var ups = UpAverage.reduce((a, b) => { return a + b })
                ups = ups / UpAverage.length
            } catch (err) {
                var ups = 0
                console.log('No UPS')
            }

            try {
                var downs = DownAverage.reduce((a, b) => { return a + b })
                downs = downs / DownAverage.length
            } catch (err) {
                var downs = 0
                console.log('No Downs')
            }

            var rsi = (((ups + downs) + 1) * 1.5)
            PrevAverageGain = ups
            prevAverageLoss = downs

        } else {
            if (change < 0) {
                prevAverageLoss = (prevAverageLoss + change) / 2
                PrevAverageGain = (PrevAverageGain)
            } else {
                PrevAverageGain = (PrevAverageGain + change) / 2
                prevAverageLoss = (prevAverageLoss)
            }
            var rsi = (((PrevAverageGain + prevAverageLoss) + 1) * 0.5) * 100
        }






        rsis.shift()
        rsis.push(change)

        return rsi

    }
    rsis.push(change)
    return 0



}

console.log('LOSS: ', prevAverageLoss)
console.log('Gain: ', PrevAverageGain)
marker2 = [];
function OpenHigh_CurrentPrice() {
    console.log('OpenHigh Making..')
    VolumeSeriesRed.setData([])
    VolumeSeriesBlue.setData([])
    VolumeSeriesOrange.setData([])

    for (let i = 0; i < respond.length - 1; i++) {

        //  Getting RS of current price
        PriceRSI = GetRSI(respond[i][1], respond[i + 1][1])
        // <<<<------ ******
        //  Getting RS of Trade
        TradeRSI = GetRSI(respond[i][8], respond[i + 1][8])
        //  <<<<------ ****
        VolumeRSI = GetRSI(respond[i][5], respond[i + 1][5])
        //  <<<<------ ****
        VolumeTradeRSI = GetRSI(respond[i][5] / respond[i][8], respond[i + 1][5] / respond[i + 1][8])
        //  <<<<------  *****
        timestamp = parseInt(respond[i][0]) / 1000




        VolumeSeriesRed.update({
            time: timestamp,
            value: TradeRSI
        })

        VolumeSeriesOrange.update({
            time: timestamp,
            value: PriceRSI
        })

        VolumeSeriesBlue.update({
            time: timestamp,
            value: VolumeRSI
        })

        VolumeSeriesGreen.update({
            time: timestamp,
            value: VolumeTradeRSI
        })
        // if (VolumeRSI > PriceRSI && PriceRSI > TradeRSI) {
        // MARKERS ***********
        if (TradeRSI > PriceRSI && PriceRSI > VolumeRSI) {
            marker2.push({
                time: timestamp,
                position: 'aboveBar',
                color: 'green',
                shape: 'arrowUp',
            });

            // console.log('MarkerMade')
            // CandleSeries.setMarkers(marker)
            // console.log('MarkerMade')

        }
        if (PriceRSI > VolumeRSI && VolumeRSI > TradeRSI && PriceRSI > TradeRSI) {
            marker2.push({
                time: timestamp,
                position: 'belowBar',
                color: 'yellow',
                shape: 'arrowDown'
            })
        }

    }
    marker2.push({
        time: timestamp,
        position: 'aboveBar',
        color: 'green',
        shape: 'arrowDwon'
    })

    CandleSeries.setMarkers(marker2)
    VolumeSeriesOrange.setMarkers(marker2)
    console.log(marker2)
}




// OpenHigh_CurrentPrice()