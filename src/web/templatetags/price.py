from django import template

def to_price(var):
    price = str(var)
    return price[:-2] + "." + price[-2:]

register = template.Library()
register.filter("to_price", to_price)
