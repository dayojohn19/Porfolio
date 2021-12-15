def Get_Coin(coin, quantity, price, user_id):

    from models import Coin

    try:
        try:
            orders = Coin.objects.filter(coin=coin, price=price)
            #

            for order in orders:
                print(order.quantity)
                return 'a'
            #
            return orders
            if int(quantity) <= int(order.quantity):
                order.quantity = int(order.quantity) - int(quantity)
                order.save()
                you_get = quantity
                return you_get
            if int(quantity) >= int(order.quantity):
                order.quantity = int(quantity) - int(order.quantity)
                order.save()
                you_get = int(quantity) - int(order.quantity)
                make_order(order.quantity, price, user_id)
                return you_get

        except:

            new_order = Coin.objects.create(
                coin=coin, price=price, quantity=quantity)
            new_order.save()
            return 'new order'

    except:
        # print('successda')

        return 'get_coin failed'
Get_Coin('DCOIN', 5, 2, 111)