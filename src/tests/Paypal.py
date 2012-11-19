
import unittest
import lib


class TestPaypal(unittest.TestCase):
	def setUp(self):
		self.paypal = lib.Paypal()

	def test_PDTMode(self):
		self.paypal.setPDTMode("enabled")
		self.assertEqual(self.paypal.ReturnMethod, 0)
		self.paypal.setPDTMode("disabled")
		self.assertEqual(self.paypal.ReturnMethod, 1)
		self.paypal.setPDTMode("enabled")
		self.assertEqual(self.paypal.ReturnMethod, 2)

	def test_ShippingMode(self):
		self.paypal.setShippingMode("enabled")
		self.assertEqual(self.paypal.ReturnMethod, 0)
		self.paypal.setShippingMode("disabled")
		self.assertEqual(self.paypal.ReturnMethod, 1)
		self.paypal.setShippingMode("required")
		self.assertEqual(self.paypal.ReturnMethod, 2)

	def test_NoteField(self):
		self.paypal.setNoteField(True)
		self.assertEqual(self.paypal.Notes, 0)
		self.paypal.setNoteField(False)
		self.assertEqual(self.paypal.Notes, 1)
		
	def test_setColourScheme(self):
		self.paypal.setColourScheme("black")
		self.assertEqual(self.paypal.CheckoutColour, 1)
		self.paypal.setColourScheme("white")
		self.assertEqual(self.paypal.CheckoutColour, 0)

	def test_setButtonType(self):
		self.paypal.setButtonType("small")
		self.assertEqual(self.paypal.ButtonType, "SM")
		self.paypal.setButtonType("large")
		self.assertEqual(self.paypal.ButtonType, "LG")
