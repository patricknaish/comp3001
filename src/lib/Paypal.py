"""
This file defines all the PayPal integration magic that we need to do.

It handles going from Sandbox to Live, along with button generation.

It was originally a PHP module that was ported for use in this application.
"""

class InvalidPaypalOptionException(Exception):
    def __init__(self):
        Exception.__init__("An invalid option was passed to a Paypal function")

class InvalidPaypalItemException(Exception):
    def __init__(self):
        Exception.__init__("An invalid PaypalItem was passed to a button generator")

class PDTFailure(Exception):
    def __init__(self):
        Exception.__init__("The PDT service failed")

"""
Class to represent somebody who has paid for an item on Paypal
"""
class User:
    def __init__(self):
        self.Address_City = ""
        self.Address_Country = ""
        self.Address_Country_Code = ""
        self.Address_Name = ""
        self.Address_State = ""
        self.Address_Confirmed = ""
        self.Address_Street = ""
        self.Address_Zip = ""
        self.First_Name = ""
        self.Last_Name = ""
        self.Business_Name = ""
        self.Email = ""
        self.ID = ""
        self.Status = ""
        self.Phone = ""
        self.Residence_Country = ""

"""
Class to represent an option for a Paypal item
"""
class Option:
    def __init__(self, name, value, display = True):
        self.Name = name
        self.Value = value
        self.Display = display

"""
Class to represent an item that can be bought via Paypal
"""
class Item:
    def __init__(self, code, name, cost, currency = "GBP", options = []):
        self.Code = code
        self.Name = name
        self.Cost = cost
        self.Currency = currency
        self.Options = options

    def addOption(self, option):
        if not isinstance(option, Option):
            raise InvalidPaypalOptionException()
        self.Options.append(option)

    def getOption(self, name):
        for opt in self.Options:
            if opt.Name == name:
                return opt
        return None

    def getOptions(self):
        return self.Options

"""
Class to represent PDT data that comes back from Paypal
"""
class PostbackData:
    def __init__(self):
        self.Sandbox = False
        self.Buyer = None
        self.Items = list()

    def addItem(self, item):
        if not isinstance(item, Item):
            raise InvalidPaypalOptionException()
        self.Items.append(item)

    def getItems(self):
        return self.Items

"""
Class to do the main bulk of the work

This class does interesting things with the above classes to get sanity.
"""
class Paypal:
    def __init__(self):
        self.MerchantID = ""
        self.PDTAuthToken = ""
        self.ButtonType = "LG"
        self.Sandbox = False
        self.Charset = "utf-8"
        self.CheckoutColour = 0
        self.ShippingEnabled = 0
        self.Notes = 0
        self.ReturnURL = ""
        self.ReturnMethod = 0

    def setPDTMode(self, mode):
        if mode == "enabled":
            self.ReturnMethod = 0
        elif mode == "disabled":
            self.ReturnMethod = 1
        elif mode == "enabled_post":
            self.ReturnMethod = 2
        else:
            raise InvalidPaypalOptionException()

    def setShippingMode(self, mode):
        if mode == "enabled":
            self.ShippingEnabled = 0
        elif mode == "disabled":
            self.ShippingEnabled = 1
        elif mode == "required":
            self.ShippingEnabled = 2
        else:
            raise InvalidPaypalOptionException()

    def setNoteField(self, enabled):
        if enabled:
            self.Notes = 0
        else:
            self.Notes = 1

    def setColourScheme(self, scheme):
        if scheme == "black":
            self.CheckoutColour = 1
        elif scheme == "white":
            self.CheckoutColour = 0
        else:
            raise InvalidPaypalOptionException()

    def setButtonType(self, button_type):
        if button_type == "small":
            self.ButtonType = "SM"
        elif button_type == "large":
            self.ButtonType = "LG"
        else:
            raise InvalidPaypalOptionException()

    def buyNowButton(self, item, paypalExtra = list()):
        return self.button("_xclick", item, paypalExtra)

    def addCartButton(self, item, paypalExtra = list()):
        return self.button("_cart", item, paypalExtra)

    def button(self, command, item, paypalExtra = list()):
        if not isinstance(item, Item): raise InvalidPaypalItemException()

        if self.Sandbox:
            ppHost = "sandbox.paypal.com"
        else:
            ppHost = "paypal.com"

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
    ppHost, 
    self.Charset,
    command,
    self.MerchantID,
    self.CheckoutColour,
    self.Notes,
    self.ShippingEnabled,
    self.ReturnURL,
    self.ReturnMethod,
    item.Name,
    item.Code,
    item.Currency,
    item.Cost
    )

        optIndex = 0
        for opt in item.getOptions():
            thisFieldPrices = False
            if opt.Display:
                form_html += """<input type="hidden" name="on%d" value="%s" />""" % (optIndex, opt.Name)
                form_html += """<label for="os%d">%s</label>""" % (optIndex, opt.Name)
                if isinstance(opt.Value, cist):
                    form_html += """<select name="os%d">""" % optIndex
                    for key in opt.Value.keys():
                        val = opt.Value[key]
                        if isinstance(val, dict):
                            item_desc = key
                            if val["Price"] < item.Cost:
                                item_desc += "(- &pound;%.02f)" % (item.Cost - val["Price"])
                            elif val["Price"] > item.Cost:
                                item_desc += "(+ &pound;%.02f)" % (val["Price"] - item.Cost)

                            form_html += """<option value="%s">%s</option>""" % (val["Ref"], item_desc)
                        else:
                            form_html += """<option value="%s">%s</option>""" % (val, key)
                    form_html += "</select>";
                    optValOptIndex = 0
                    for key in opt.Value.keys():
                        val = opt.Value[key]
                        if isinstance(val, dict):
                            thisFieldPrices = True
                            form_html += """<input type="hidden" name="option_select%s" value="%s">
<input type="hidden" name="option_amount%s" value="%s">""" % (optValOptIndex, val["Ref"], optValOptIndex, val["Price"])
                        optValOptIndex += 1
                    if thisFieldPrices: form_html += """<input type="hidden" name="option_index" value="%s">""" % optIndex
                else:
                    form_html += """<input type="text" name="os%s" value="%s" />""" % (optIndex, opt.Value)
            else:
                form_html += """<input type="hidden" name="on%d" value="%s" />
<input type="hidden" name="os%d" value="%s" />""" % (optIndex, opt.Name, optIndex, opt.Value)

        for key in paypalExtra.keys():
            form_html += """<input type="hidden" name="%s" value="%s" />""" % (key, paypalExtra[key])

        if command == "_cart":
            btnID = "cart"
        else:
            btnID = "buynow"

        form_html += """<input type="image" src="https://www.paypal.com/en_GB/i/btn/btn_%s_%s.gif" />
</form>""" % (btnID, self.ButtonType)

        return form_html
