orders = [
    {'ord': 4},
    {'ord': 10}
]
ask = 6
credit = 0

for order in orders:

    if order['ord'] > ask:
        seller_credit = ask
        credit += ask

        order['ord'] -= ask
        ask -= order['ord']
        if ask < 0:
            ask = 0

        print('remaining order: ',
              order['ord'], 'you ordered: ', ask, 'Seller Credit: ', seller_credit)

    elif order['ord'] < ask:
        seller_credit = order['ord']
        credit += order['ord']

        ask -= order['ord']
        order['ord'] = 0

        print('remaining order ', order['ord'],
              'you ordered: ', ask, 'Seller Credit: ', seller_credit)

if ask > 0:
    print('You make order: ', ask)
elif ask <= 0:
    print('you filled all your Order')

print('you credit: ', credit)

def mprint(a,b):
    print('initializing')
    if a == 'a':
        print(a,'is equal to ',a)
    elif a != 'a':
        print(a,'is not equal to a')
        a='a'
        mprint(a, b)
mprint('b', 'b')

#    // function trade_it() {
#        // quantity = document.querySelector("input[name='quantity'] ").value
#        // coin = document.querySelector("input[name='coin'] ").value
#        // price = document.querySelector("input[name='coin_price'] ").value

#        // user_id = document.querySelector("input[name='user_id'] ").value
#        // balance = document.querySelector("input[name='user_balance'] ").value
#        // hash = document.querySelector("input[name='hash'] ").value
#        // fetch("{% url 'user:trade_it' %}", {
#            // method: 'POST',
#            // csrf_token: '{{csrf_token}}',
#            // body: JSON.stringify({

#                 // quantity: quantity,
#                 // coin: coin,
#                 // price: price,

#                 // user_id: user_id,
#                 // balance: balance,
#                 // hash: hash
#                 //})
#            // }).then(response = > response.json())
#        //             .then(result= > {
#            // alert(result)
#            // })
#        // quantity = 0
#        // price = 0
#        // location.reload()
#        // }
