from ShoppingBasket import ShoppingBasket
import unittest as ut


class TestCartDetails(ut.TestCase):

    def testAdd(self):
        cart = ShoppingBasket()
        self.assertEqual(cart.order(), 0)

    def testAddToCart(self):
        cart = ShoppingBasket()
        cart.add_to_cart("bread", 1)
        self.assertEqual(cart.order(), 1.49)

    def testAddExtra(self):
        cart = ShoppingBasket()
        cart.add_to_cart("milk", 1)
        self.assertEqual(cart.order(), 0.99)
        cart.add_to_cart("milk", 1)
        self.assertEqual(cart.order(), 1.98)

    def testNegativeCart(self):
        cart = ShoppingBasket()
        with self.assertRaises(ValueError):
            cart.add_to_cart("cheese", -2)

    def testOtherItemInput(self):
        sb = ShoppingBasket()
        with self.assertRaises(ValueError):
            sb.add_to_cart("sanitizer", 1)


ut.main(argv=['ignored'], exit=False)
