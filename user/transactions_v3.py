from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse


def Transfer():
    return 'successd'


def Hash_it():
    return 'hashed'


def Trade_it(user_id, balance, hashed, quantity, coin, price):
    from app_mail import models as mail
    try:

        user = mail.User.objects.get(
            id=user_id, last_name=balance, first_name=hashed)

        amount = int(price) * int(quantity)
        quantity = int(quantity)
        price = int(price)

        if int(balance) >= int(amount):

            x = Get_Order(coin, quantity, price, user_id)
            print('x is : ', x)
            transaction(user_id, last_name=balance,
                        first_name=hashed, amount=amount, what='subtract')
            return x

        else:
            return 'not Enough Balance'
    except:
        return 'Trade_it Failed'


def transaction(id, last_name, first_name, amount, what):

    try:
        user = mail.User.objects.get(
            id=user_id, last_name=balance, first_name=hashed)
        if what == 'subtract':
            user.last_name = int(user.last_name - amount)
            user.hash = int(user.hash - 1)
            user.save()

    except:
        return 'transaction failed'


def credit_to(user_id, amount, coin, what):
    from app_mail.models import User
    from . models import User_Coins
    print('trying to Credit....')

    try:
        print('trying to Credit....', amount, coin, what)
        if coin != 'peso':

            wallet = User_Coins.objects.get_or_create(
                user_id=user_id, coin=coin)

            wallet = User_Coins.objects.get(user_id=user_id, coin=coin)
            print('entering Not Peso', what, amount, wallet.quantity)
            if what == 'add':

                y = int(wallet.quantity) + int(amount)

            elif what == 'subtract':
                y = int(wallet.quantity) - int(amount)
            wallet.quantity = y
            wallet.save()
            print('Credit SUCCESS ..')
        elif coin == 'peso':

            user = User.objects.get(id=user_id)

            if what == 'add':
                x = int(user.last_name) + int(amount)
                user.last_name = x
            elif what == 'subtract':
                x = int(user.last_name) - int(amount)
                user.last_name = x

            user.save()
        print('SUCCESS credited to')
    except:
        print('FAILED credited to')


def Get_Order(coin, quantity, price, user_id):

    from . models import Order

    try:

        try:

            orders = Order.objects.filter(
                coin=coin, price=price).order_by('id').reverse()
            #
            credit = 0
            ask = int(quantity)

            for order in orders:
                if ask > 0:
                    if int(order.quantity) >= int(ask):
                        # credit to seller
                        # seller_credit = int(ask) * int(price)
                        seller_credit = ask
                        credit_to(order.coin_id, seller_credit,
                                  coin, 'add')
                        #
                        credit += int(ask)

                        order.quantity -= ask
                        order.save()
                        ask -= int(order.quantity)

                        if int(order.quantity) <= 0:
                            order.delete()
                        if ask <= 0:
                            ask = 0

                    elif order.quantity < ask:

                        # seller_credit = int(order.quantity) * int(price)
                        seller_credit = order.quantity
                        credit_to(order.coin_id, seller_credit,
                                  coin, 'add')
                        #
                        credit += int(order.quantity)

                        ask -= int(order.quantity)

                        if ask <= 0:
                            ask = 0
                        order.delete()
                        # return credit
# -------------- 1
            if int(ask) > 0:
                make_order(coin, ask, price, user_id)
            credit_to(user_id, int(credit) * int(price), 'peso', 'subtract')
            credit_to(user_id, credit, coin, 'add')
            return 'credit', credit, 'ask', ask
# --------------1 End
# ---------2
            # total = int(ask) - int(credit)
            # amount_filled = int(credit) * int(price)
            # if (total == 0):
            #     if (ask > 0):
            #         ask = abs(ask)
            #         make_order(coin, ask, price, user_id)
            #         return 'order ask', 'ask:', ask, 'credit:', credit

            #     # credit_to(user_id, amount_filled, coin, what)
            #     return 'all orders are filled ', 'ask:', ask, 'credit:', credit
            # elif (total < 0):
            #     if (ask > 0):
            #         ask = abs(ask)
            #         make_order(coin, ask, price, user_id)
            #         return 'order ask', 'ask:', ask, 'credit:', credit
            #     else:
            #         return 'zero total zero ask'

            # elif (total > 0):
            #     # credit_to(user_id, amount_filled, coin, what)
            #     make_order(coin, ask, price, user_id)
            #     return 'order made', 'ask:', ask, 'credit:', credit
            # return 'transaction ended'
# ------------2 End
# -----------3 Start
            #
            # return orders
            # if int(quantity) <= int(order.quantity):
            #     order.quantity = int(order.quantity) - int(quantity)
            #     order.save()
            #     you_get = quantity
            #     return you_get
            # if int(quantity) >= int(order.quantity):
            #     order.quantity = int(quantity) - int(order.quantity)
            #     order.save()
            #     you_get = int(quantity) - int(order.quantity)
            #     make_order(order.quantity, price, user_id)
            #     return you_get
# ----------3 END
        except:
            if ask > 0:
                make_order(coin, ask, price, user_id)
            return 'new order'

    except:
        # print('successda')

        return 'get_coin failed'


def cancel_order(user_id, sell_coin, buy_coin, quantity, price, side):
    from . models import Order

    order = Order.objects.get(sell_coin=sell_coin, buy_coin=buy_coin,
                              coin_id=user_id, quantity=quantity, price=price)
    if side == 'buy':
        credit_to(user_id, int(quantity) * int(price), sell_coin, 'add')
    elif side == 'sell':
        credit_to(user_id, quantity, buy_coin, 'add')
    order.delete()


def fill_order(sell_coin, buy_coin, quantity, price, user_id, side):
    try:
        try:
            print('1 trying')
            from . models import Order
            print('is it buy or sell')
            # getting the orders
            if side == 'buy':
                orders = Order.objects.filter(
                    buy_coin=buy_coin, sell_coin=sell_coin, price=price, sell=True).order_by('id')
                print(' it is buy')
            elif side == 'sell':
                orders = Order.objects.filter(
                    buy_coin=buy_coin, sell_coin=sell_coin, price=price, buy=True).order_by('id')
                print('it is sell')
            # order got
            print('2 order filling ....', quantity, ' quantity')
            credit = 0
            quantity = int(quantity)

            for order in orders:
                if quantity > 0:

                    if quantity >= int(order.quantity):
                        print('quantity is greater than ORDER')
                        quantity -= int(order.quantity)
                        credit += int(order.quantity)

                        if side == 'buy':
                            credit_to(order.coin_id, int(
                                order.quantity) * int(price), sell_coin, 'add')
                        elif side == 'sell':
                            # credit_to(order.coin_id, int(
                            #     order.quantity) * int(price), buy_coin, 'add')
                            credit_to(order.coin_id, int(
                                order.quantity), buy_coin, 'add')
                        order.delete()
                        print('DONE')

                    elif int(quantity) < int(order.quantity):
                        print('quantity is leser than ORDER')
                        order.quantity -= int(quantity)
                        credit += int(quantity)
                        order.save()
                        if side == 'buy':
                            print('adding to seller: ')
                            credit_to(order.coin_id, int(
                                quantity) * int(price), sell_coin, 'add')
                        elif side == 'sell':
                            print('adding to buyer')
                            # credit_to(order.coin_id, int(
                            #     quantity) * int(price), buy_coin, 'add')
                            credit_to(order.coin_id,
                                      quantity, buy_coin, 'add')
                        print('DONE')
                        quantity = 0

            print('3 done filling...Quantity: ', quantity, 'credit: ', credit)
            if int(quantity) > 0:
                if side == 'buy':
                    print('BUY, still left on quantity making order: ', quantity)
                    make_order(sell_coin, buy_coin, quantity,
                               price, user_id, 'buy')
                    print('done making order on quantity left')
                # retux`rn
                elif side == 'sell':
                    print('SELL, still left on quantity making order: ', quantity)
                    make_order(sell_coin, buy_coin, quantity,
                               price, user_id, 'sell')
                    print('done making order on quantity left')

            elif int(quantity) <= 0:
                print('all orders are filled', quantity)
                print('crediting....')
            # return 'all orders are fill_order'
            if side == 'buy':
                credit_to(user_id, credit, buy_coin, 'add')
                credit_to(user_id, int(credit) *
                          int(price), sell_coin, 'subtract')

            elif side == 'sell':
                credit_to(user_id, credit, buy_coin, 'subtract')
                credit_to(user_id, int(credit) *
                          int(price), sell_coin, 'add')
            # credit_to(user_id, amount, coin, what)

        except:
            pass
            # print('orders are being made', side)
            # if side == 'buy':
            #     make_order(sell_coin, buy_coin, quantity,
            #                price, user_id, 'buy')

            # elif side == 'sell':
            #     make_order(sell_coin, buy_coin, quantity,
            #                price, user_id, 'sell')

    except:
        print('fill_order FAILED')
        return 'fill_order Failed'


def make_order(sell_coin, buy_coin, quantity, price, user_id, side):
    try:
        print('making Order.....')
        from . models import Order
        try:
            print('IM TRYING update order', side)
            if side == 'sell':
                print(side, 'making selling ORDER')
                old_order = Order.objects.get(
                    sell_coin=sell_coin, buy_coin=buy_coin, coin_id=user_id, price=price, sell=True)
                credit_to(user_id, quantity, buy_coin, 'subtract')
                print(side, 'making selling ORDER')

            elif side == 'buy':
                print(side, 'making buying ORDER ')
                old_order = Order.objects.get(
                    sell_coin=sell_coin, buy_coin=buy_coin, coin_id=user_id, price=price, buy=True)
                credit_to(user_id, int(quantity) *
                          int(price), sell_coin, 'subtract')
                print(side, 'making buying ORDER ')

            print('trying to look old orders..', user_id)
            old_order.quantity += int(quantity)
            old_order.save()
            print(' old order updated')
        except:
            new_order = Order()
            new_order.coin_id = user_id
            new_order.quantity = quantity
            new_order.price = price
            new_order.sell_coin = sell_coin
            new_order.buy_coin = buy_coin

            if side == 'buy':
                new_order.buy = True
                print('Order Crediting...')
                credit_to(user_id, int(quantity) *
                          int(price), sell_coin, 'subtract')
            elif side == 'sell':
                new_order.sell = True
                print('Order Crediting...')
                credit_to(user_id, quantity, buy_coin, 'subtract')
            new_order.save()
            print('new order made.......')
        # credit_to(user_id, int(quantity) * int(price), sell_coin, 'subtract')

        # make an order with id to be credited
        # credit_to(user_id, int(quantity) * int(price), 'peso', 'subtract')

    except:
        print('did not make order......')


def load(request):
    if request.method == 'POST':
        user = request.user
        hashed = user.first_name
        load = request.POST.get("load")

        from app_mail import models
        target = models.User.objects.get(username=request.POST.get("target"))
        value = reload(user, hashed, load, target)
        if value == 'hacker':
            return HttpResponse('error')
        return HttpResponseRedirect(reverse("commerce:commerce"))
    return HttpResponseRedirect(reverse("commerce:commerce"))


def reload(user, hashed, load, target):
    # add object that error when less than 0
    if hashed != user.first_name:
        return ('hacker')
    new_hash = hash(str(hashed))
    user.first_name = new_hash
    new_load = int(user.last_name) - int(load)
    # added
    if new_load <= 0:
        return HttpResponse("poor")
        ##
    user.last_name = new_load
    user.save()
    target.first_name = new_hash+1
    target.last_name = int(target.last_name) + int(load)
    target.save()
    # put it on record
    record_it(user.id, target.id, load, new_hash)


def record_it(sender, receiver, amount, hashit):
    from . models import Transaction_History
    new_record = Transaction_History()
    new_record.sender_id = sender
    new_record.receiver_id = receiver
    new_record.amount = amount
    new_record.hashit = str(sender)+str(00)+str(receiver)
    new_record.save()
