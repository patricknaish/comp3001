"""
Paypal class unit tests
"""

import unittest
import lib

class TestPaypal(unittest.TestCase):
    """
    Class to test the Paypal class
    """
    def setUp(self):
        """
        Setup the Paypal test (this is called each time)
        """
        self.paypal = lib.Paypal()

    def test_PDTMode(self):
        """
        Ensure the PDT mode setting works
        """
        self.paypal.set_pdt_mode("enabled")
        self.assertEqual(self.paypal.return_method, 0)
        self.paypal.set_pdt_mode("disabled")
        self.assertEqual(self.paypal.return_method, 1)
        self.paypal.set_pdt_mode("enabled_post")
        self.assertEqual(self.paypal.return_method, 2)

    def test_ShippingMode(self):
        """
        Ensure the shipping mode setting works
        """
        self.paypal.set_shipping_mode("enabled")
        self.assertEqual(self.paypal.shipping_enabled, 0)
        self.paypal.set_shipping_mode("disabled")
        self.assertEqual(self.paypal.shipping_enabled, 1)
        self.paypal.set_shipping_mode("required")
        self.assertEqual(self.paypal.shipping_enabled, 2)

    def test_NotesField(self):
        """
        Ensure the notes field enable/disable works
        """
        self.paypal.set_notes_field(True)
        self.assertEqual(self.paypal.enable_notes, 0)
        self.paypal.set_notes_field(False)
        self.assertEqual(self.paypal.enable_notes, 1)
 
    def test_setColourScheme(self):
        """
        Ensure the colour scheme setting works
        """
        self.paypal.set_colour_scheme("black")
        self.assertEqual(self.paypal.checkout_colour, 1)
        self.paypal.set_colour_scheme("white")
        self.assertEqual(self.paypal.checkout_colour, 0)

    def test_setButtonType(self):
        """
        Ensure the button type setting works
        """
        self.paypal.set_button_type("small")
        self.assertEqual(self.paypal.button_type, "SM")
        self.paypal.set_button_type("large")
        self.assertEqual(self.paypal.button_type, "LG")
