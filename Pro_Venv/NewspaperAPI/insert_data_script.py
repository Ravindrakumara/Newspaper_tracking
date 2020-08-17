from.models import Consumer_order,Daily_Cart

def transfer_daily_data():
    new_daily_cart = Daily_Cart()
    new_daily_cart.ac_no = Consumer_order.ac_no()
    new_daily_cart.newspaper = Consumer_order.newspaper()
    new_daily_cart.added_date = Consumer_order.added_date()
    new_daily_cart.save()
    print(callable ("saving...\n" + new_daily_cart))
