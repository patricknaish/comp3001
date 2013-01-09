from django import template
import re

def to_price(var):
    price = str(var)
    if re.search('0+\.[0-9]*', 'price'):		
        return "0." + price[-2:]
    else:
        return price[:-2] + "." + price[-2:]

register = template.Library()
register.filter("to_price", to_price)
