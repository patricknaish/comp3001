from django import template

def to_price(var):
    price = str(var)
    if len(price) == 2:
        return "0." + price[-2:]
    elif len(price) == 1;
        return "0.0"+ price[-2:]
    else:
        return price[:-2] + "." + price[-2:]

register = template.Library()
register.filter("to_price", to_price)