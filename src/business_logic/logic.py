def calculate_total_price(items):
    total = sum(item['price'] * item['quantity'] for item in items)
    return total

def apply_discount(total_price, discount):
    if discount < 0 or discount > 1:
        raise ValueError("Discount must be between 0 and 1")
    return total_price * (1 - discount)

def process_order(order):
    total_price = calculate_total_price(order['items'])
    if 'discount' in order:
        total_price = apply_discount(total_price, order['discount'])
    return {
        'order_id': order['id'],
        'total_price': total_price
    }