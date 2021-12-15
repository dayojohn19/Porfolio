
    function trade_it() {
        amount = document.querySelector("input[name='amount'] ").value;
        coin =  document.querySelector("input[name='coin'] ").value;
        price =  document.querySelector("input[name='coin_price'] ").value;

        user_id =  document.querySelector("input[name='user_id'] ").value;
        balance =  document.querySelector("input[name='user_balance'] ").value;
        hash =  document.querySelector("input[name='hash'] ").value;
        fetch("{% url 'user:trade_it' %}", {
            method: 'POST',
            // headers: { "X-CSRFToken": csrftoken },
            body: JSON.stringify({
                amount: amount, 
                coin: coin,
                price: price,

                user_id: user_id,
                balance:balance,
                hash:hash
            })
        }).then(response=> response.json())
        .then(result => {
            alert(result);
        })
    }


        function transfer_it() {
        fetch("{% url 'user:printit' %}")
        .then(response => response.json())
        .then(result => {
            alert(result);
        })
    }

      function Send_Data(sell_coin, buy_coin, price, quantity, side) {
        hash = '111';
        fetch("{% url 'user:js_order_it %}", {
            method: 'POST',
            body: JSON.stringify({
                quantity:quantity,
                sell_coin: sell_coin,
                buy_coin: buy_coin,
                price: price,
                side: side,
                hash:hash
            })
        }).then(response=> response.json())
        .then(result => {
            alert(result);
        })
    }