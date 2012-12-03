"""
This file defines all the PayPal integration magic that we need to do.

It handles going from Sandbox to Live, along with button generation.

It was originally a PHP module that was ported for use in this application.
"""


class InvalidPaypalOptionException(Exception):
    """
    Exception thrown when an invalid option is passed to a Paypal library 
    function.
    """
    def __init__(self):
        Exception.__init__("An invalid option was passed to a Paypal function")


class InvalidPaypalItemException(Exception):
    """
    Exception thrown when an invalid item is passed to a button generator.
    """
    def __init__(self):
        Exception.__init__("An invalid PaypalItem was passed to a button " + 
                            "generator")


class PDTFailure(Exception):
    """
    Exception thrown when/if the Payment Data Transfer service fails.
    """
    def __init__(self):
        Exception.__init__("The PDT service failed")

class User:
    """
    Class to represent somebody who has paid for an item on Paypal
    """
    def __init__(self):
        self.address_city = ""
        self.address_country = ""
        self.address_country_code = ""
        self.address_name = ""
        self.address_state = ""
        self.address_confirmed = ""
        self.address_street = ""
        self.address_zip = ""
        self.first_name = ""
        self.last_name = ""
        self.business_name = ""
        self.email = ""
        self.user_id = ""
        self.status = ""
        self.phone = ""
        self.residence_country = ""


class Option:
    """
    Class to represent an option for a Paypal item
    """
    def __init__(self, name, value, display = True):
        self.name = name
        self.value = value
        self.display = display


class Item:
    """
    Class to represent an item that can be bought via Paypal
    """
    def __init__(self, code, name, cost, currency = "GBP", options = list()):
        self.code = code
        self.name = name
        self.cost = cost
        self.currency = currency
        self.options = options

    def add_option(self, option):
        """
        Add an option to the item.
        """
        if not isinstance(option, Option):
            raise InvalidPaypalOptionException()
        self.options.append(option)

    def get_option(self, name):
        """
        Fetch an option from this item by its name
        """
        for opt in self.options:
            if opt.name == name:
                return opt
        return None

    def get_options(self):
        """
        Fetch all of the options for this item.
        """
        return self.options


class PostbackData:
    """
    Class to represent PDT data that comes back from Paypal
    """
    def __init__(self):
        self.sandbox = False
        self.buyer = None
        self.items = list()

    def add_item(self, item):
        """
        Add an item that was bought and posted back to us.
        """
        if not isinstance(item, Item):
            raise InvalidPaypalOptionException()
        self.items.append(item)

    def get_items(self):
        """
        Get the list of items that were posted back to us
        """
        return self.items


class Paypal:
    """
    Class to do the main bulk of the work

    This class does interesting things with the above classes to get sanity.
    """
    def __init__(self):
        self.merchant_id = ""
        self.pdt_auth_token = ""
        self.button_type = "LG"
        self.sandbox = False
        self.charset = "utf-8"
        self.checkout_colour = 0
        self.shipping_enabled = 0
        self.enable_notes = 0
        self.return_url = ""
        self.return_method = 0

    def set_pdt_mode(self, mode):
        """
        Set the Payment Data Transfer mode.
        One of:
            enabled - PDT data is sent via GET
            disabled - No PDT data is sent
            enabled_post - PDT data is sent via POST
        """
        if mode == "enabled":
            self.return_method = 0
        elif mode == "disabled":
            self.return_method = 1
        elif mode == "enabled_post":
            self.return_method = 2
        else:
            raise InvalidPaypalOptionException()

    def set_shipping_mode(self, mode):
        """
        Set the shipping mode.
        One of:
            Enabled - Shipping data is optional
            Disabled - Shipping data is not requested
            Required - Shipping data is required
        """
        if mode == "enabled":
            self.shipping_enabled = 0
        elif mode == "disabled":
            self.shipping_enabled = 1
        elif mode == "required":
            self.shipping_enabled = 2
        else:
            raise InvalidPaypalOptionException()

    def set_notes_field(self, enabled):
        """
        Enabled or disable the additional notes field.
        """
        if enabled:
            self.enable_notes = 0
        else:
            self.enable_notes = 1

    def set_colour_scheme(self, scheme):
        """
        Change the colour scheme of the paypal checkout
        Supported colour schemes:
            white
            black
        """
        if scheme == "black":
            self.checkout_colour = 1
        elif scheme == "white":
            self.checkout_colour = 0
        else:
            raise InvalidPaypalOptionException()

    def set_button_type(self, button_type):
        """
        Set the button size
        Valid sizes:
            small
            large
        """
        if button_type == "small":
            self.button_type = "SM"
        elif button_type == "large":
            self.button_type = "LG"
        else:
            raise InvalidPaypalOptionException()

    def buy_now_button(self, item, paypal_extra = list()):
        """
        Generate a "Buy Now" button for an item.
        """
        return self.button("_xclick", item, paypal_extra)

    def add_cart_button(self, item, paypal_extra = list()):
        """
        Generate an "Add to cart" button.
        """
        return self.button("_cart", item, paypal_extra)

    def button(self, command, item, paypal_extra = None):
        """
        Generate a button for a Paypal web form
        """
        if paypal_extra == None:
            paypal_extra = dict()

        if not isinstance(item, Item):
            raise InvalidPaypalItemException()

        if self.sandbox:
            pp_host = "sandbox.paypal.com"
        else:
            pp_host = "paypal.com"

        form_html = """<FORM action="https://%s/cgi-bin/webscr" method="post">
            <input type="hidden" name="charset" value="%s">
            <input type="hidden" name="cmd" value="%s" />
            <input type="hidden" name="business" value="%s" />
            <input type="hidden" name="cs" value="%s" />
            <input type="hidden" name="no_note" value="%s" />
            <input type="hidden" name="no_shipping" value="%s" />
            <input type="hidden" name="return" value="%s" />
            <input type="hidden" name="rm" value="%s" />
            <input type="hidden" name="item_name" value="%s" />
            <input type="hidden" name="item_number" value="%s" />
            <input type="hidden" name="currency_code" value="%s" />
            <input type="hidden" name="amount" value="%s" />""" % (
            pp_host,
            self.charset,
            command,
            self.merchant_id,
            self.checkout_colour,
            self.enable_notes,
            self.shipping_enabled,
            self.return_url,
            self.return_method,
            item.Name,
            item.Code,
            item.Currency,
            item.Cost
        )

        opt_index = 0
        for opt in item.getOptions():
            this_field_prices = False
            if opt.Display:
                form_html += ("""<input type="hidden" name="on%d" """
                                """ "value="%s" />""") % (opt_index, opt.Name)
                form_html += """<label for="os%d">%s</label>""" % \
                                (opt_index, opt.Name)
                if isinstance(opt.value, dict):
                    form_html += """<select name="os%d">""" % opt_index
                    for key in opt.value.keys():
                        val = opt.value[key]
                        if isinstance(val, dict):
                            item_desc = key
                            if val["Price"] < item.cost:
                                item_desc += "(- &pound;%.02f)" % \
                                    (item.Cost - val["Price"])
                            elif val["Price"] > item.cost:
                                item_desc += "(+ &pound;%.02f)" % \
                                    (val["Price"] - item.cost)

                            form_html += """<option value="%s">%s</option>"""% \
                                (val["Ref"], item_desc)
                        else:
                            form_html += """<option value="%s">%s</option>"""% \
                                (val, key)
                    form_html += "</select>"
                    opt_val_opt_index = 0
                    for key in opt.value.keys():
                        val = opt.Value[key]
                        if isinstance(val, dict):
                            this_field_prices = True
                            form_html += ("""<input type="hidden" """
                                """name="option_select%s" """
                                """value="%s">"""
                                """<input type="hidden" """
                                """name="option_amount%s" value="%s">""") % \
                                (opt_val_opt_index,
                                    val["Ref"],
                                    opt_val_opt_index,
                                    val["Price"]
                                )
                        opt_val_opt_index += 1
                    if this_field_prices: 
                        form_html += ("""<input type="hidden" """
                            """name="option_index" value="%s">""") % opt_index
                else:
                    form_html += ("""<input type="text" name="os%s" """
                        """value="%s" />""") % (opt_index, opt.value)
            else:
                form_html += ("""<input type="hidden" name="on%d" """
                    """value="%s" />"""
                    """<input type="hidden" name="os%d" value="%s" />""") % \
                    (opt_index,
                    opt.name,
                    opt_index,
                    opt.value)

        for key in paypal_extra.keys():
            form_html += """<input type="hidden" name="%s" value="%s" />""" % \
                (key, paypal_extra[key])

        if command == "_cart":
            btnid = "cart"
        else:
            btnid = "buynow"

        form_html += """<input type="image" """ + \
            """src="https://www.paypal.com/en_GB/i/btn/btn_%s_%s.gif" />
            </form>""" % (btnid, self.button_type)

        return form_html
