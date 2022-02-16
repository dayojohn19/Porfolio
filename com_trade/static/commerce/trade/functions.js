function active_coin() {
    document.querySelector("#coin_name").removeAttribute("disabled");
    console.log('Coin Activated');
}
function active_interval() {
    document.querySelector("#history_intervals").removeAttribute("disabled");
    console.log('Interval Activated');
}
function get_data() {
    message.innerHTML = 'Fetching New Data';
    old_file = document.querySelector("#old_files_name").value;
    fetch(`fetch_old_data/${old_file}`).then((r) => r.json()).then((response) => {
        respond = response;
        // console.log(response);
        message.innerHTML = 'Data Refreshed';
        put_candles();
        OpenHigh_CurrentPrice()

    });

}

function getCurrentDate() {
    function processDate(rawDate) {

        splitDate = rawDate.split('-')
        year = splitDate[0]
        day = splitDate[2]
        month = splitDate[1] - 1

        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        month = months[month]

        return month + ' ' + day + ',' + ' ' + year
    }

    w_date = document.querySelector("#history_date").value;
    processDate(w_date)
    return processDate(w_date)
}

function new_data() {
    new_new = getCurrentDate()
    console.log(new_new);
    message.innerHTML = 'Fetching New Data';
    // let djurl = {% url 'trade:new_data' %};
    // let url = "{% url 'trade:new_data' %}";
    // x = new_new
    what_coin = document.querySelector("#coin_name").value;
    what_interval = document.querySelector("#history_intervals").value;
    fetch(`new_data/${what_coin}/${what_interval}`, {
        method: 'POST',
        body: JSON.stringify({
            new_date: new_new
        })
    }).then((r) => r.json()).then((response) => {
        console.log(response);
        fetch(`fetch_old_data/${response}`).then((r) => r.json()).then((response) => {
            respond = response;
            // console.log(response);
            message.innerHTML = 'Data Refreshed';
            put_candles();
        });



        // respond = response;
        // console.log(response);
        // message.innerHTML = 'Data Refreshed';
        // put_candles();
    });

}


function put_candles() {
    CandleSeries.setData([]);
    for (let i = 0; i < respond.length; i++) {
        var candle = {
            time: parseFloat(respond[i][0]) / 1000,
            open: parseFloat(respond[i][1]),
            high: parseFloat(respond[i][2]),
            low: parseFloat(respond[i][3]),
            close: parseFloat(respond[i][4])
        }
        CandleSeries.update(candle);
    }
    // get_data()
    new Promise(resolve => {
        setTimeout(() => {
            put_volume()
            setTimeout(() => {
                Over_Trade()
                resolve()
            }, 1500)

        }, 2000);
    })
    message.innerHTML = 'Candles Put'
}
