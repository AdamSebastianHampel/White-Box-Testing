import unittest
from credit_card_validator import credit_card_validator


class Test(unittest.TestCase):

    def test1(self):
        # Verifies if any credit card with no input returns False
        # Picked using Error Guessing Method
        num = ''
        self.assertFalse(credit_card_validator(num))

    def test2(self):
        # Verifies if Visa Card with invalid length (17) returns False
        # Picked using Boundary Value Testing
        num = '41234567890123456'
        self.assertFalse(credit_card_validator(num))

    def test3(self):
        # Verifies if Visa Card with invalid length (15) returns False
        # Picked using Boundary Value Testing
        num = '412345678901234'
        self.assertFalse(credit_card_validator(num))

    def test4(self):
        # Verifies if Visa Card with valid length (16)
        # & invalid check bit returns False
        # Picked using Partition Testing
        num = '4123456789012345'
        self.assertFalse(credit_card_validator(num))

    def test5(self):
        # Verifies if Visa Card with valid length (16)
        # & valid check bit returns True
        # Picked using Partition Testing
        num = '4518270462578606'
        self.assertTrue(credit_card_validator(num))

    def test6(self):
        # Verifies if AmEx Card with invalid length (14) returns False
        # Picked using Boundary Value Testing
        num = '34123456789012'
        self.assertFalse(credit_card_validator(num))

    def test7(self):
        # Verifies if AmEx Card with invalid length (16) returns False
        # Picked using Boundary Value Testing
        num = '3412345678901234'
        self.assertFalse(credit_card_validator(num))

    def test8(self):
        # Verifies if AmEx Card with prefix of 37
        # & invalid length (14) returns False
        # Picked using Partition Testing
        num = '37123456789012'
        self.assertFalse(credit_card_validator(num))

    def test9(self):
        # Verifies if AmEx Card with prefix of 37
        # & invalid length (16) returns False
        # Picked using Partition Testing
        num = '3712345678901234'
        self.assertFalse(credit_card_validator(num))

    def test10(self):
        # Verifies if AmEx Card with prefix of 34
        # & valid length (15) but invalid check bit returns False
        # Picked using Partition Testing
        num = '341234567890123'
        self.assertFalse(credit_card_validator(num))

    def test11(self):
        # Verifies if AmEx Card with prefix of 34
        # & valid length (15) and valid check bit returns True
        # Picked using Partition Testing
        num = '349349527074745'
        self.assertTrue(credit_card_validator(num))

    def test12(self):
        # Verifies if AmEx Card with prefix of 37
        # & valid length (15) but invalid check bit returns False
        # Picked using Partition Testing
        num = '371234567890123'
        self.assertFalse(credit_card_validator(num))

    def test13(self):
        # Verifies if AmEx Card with prefix of 37
        # & valid length (15) and valid check bit returns True
        # Picked using Partition Testing
        num = '370036175255203'
        self.assertTrue(credit_card_validator(num))

    def test14(self):
        # Verifies if MC Card with invalid prefix (50),
        # invalid length (15) and valid check bit returns False
        # Picked using Partition Testing & Boundary Value Testing
        #MC, prefix of 50, length of 15, good CheckSum
        num = '501234567890123'
        self.assertFalse(credit_card_validator(num))

    def test15(self):
        # Verifies if MC Card with valid prefix (51),
        # invalid length (15) and valid check bit returns False
        # Picked using Partition Testing & Boundary Value Testing
        num = '511234567890121'
        self.assertFalse(credit_card_validator(num))

    def test16(self):
        # Verifies if MC Card with valid prefix (55),
        # invalid length (15) and valid check bit returns False
        # Picked using Partition Testing & Boundary Value Testing
        num = '551234567890122'
        self.assertFalse(credit_card_validator(num))

    def test17(self):
        # Verifies if MC Card with invalid prefix (56),
        # invalid length (15) and valid check bit returns False
        # Picked using Partition Testing & Boundary Value Testing
        num = '561234567890120'
        self.assertFalse(credit_card_validator(num))

    def test18(self):
        # Verifies if MC Card with invalid prefix (50),
        # invalid length (17) and valid check bit returns False
        # Picked using Partition Testing & Boundary Value Testing
        num = '50123456789012375'
        self.assertFalse(credit_card_validator(num))

    def test19(self):
        # Verifies if MC Card with valid prefix (51),
        # invalid length (17) and valid check bit returns False
        # Picked using Partition Testing & Boundary Value Testing
        num = '51123456789012142'
        self.assertFalse(credit_card_validator(num))

    def test20(self):
        # Verifies if MC Card with valid prefix (55),
        # invalid length (17) and valid check bit returns False
        # Picked using Partition Testing & Boundary Value Testing
        num = '55123456789012374'
        self.assertFalse(credit_card_validator(num))

    def test21(self):
        # Verifies if MC Card with invalid prefix (56),
        # invalid length (17) and valid check bit returns False
        # Picked using Partition Testing & Boundary Value Testing
        num = '56123456789012141'
        self.assertFalse(credit_card_validator(num))

    def test22(self):
        # Verifies if MC Card with valid prefix (55),
        # valid length (16) and valid check bit returns True
        # Picked using Partition Testing
        num = '5512345678901231'
        self.assertTrue(credit_card_validator(num))

    def test23(self):
        # Verifies if MC Card with valid prefix (55),
        # valid length (16) and invalid check bit returns False
        # Picked using Partition Testing
        num = '5512345678901237'
        self.assertFalse(credit_card_validator(num))

    def test24(self):
        # Verifies if MC Card with valid prefix (51),
        # valid length (16) and valid check bit returns True
        # Picked using Partition Testing
        num = '5112345678901235'
        self.assertTrue(credit_card_validator(num))

    def test25(self):
        # Verifies if MC Card with valid prefix (51),
        # valid length (16) and invalid check bit returns False
        # Picked using Partition Testing
        num = '5112345678901239'
        self.assertFalse(credit_card_validator(num))

    def test26(self):
        # Verifies if MC Card with valid prefix (2221),
        # valid length (16) and valid check bit returns True
        # Picked using Partition Testing
        num = '2221123456789014'
        self.assertTrue(credit_card_validator(num))

    def test27(self):
        # Verifies if MC Card with valid prefix (2221),
        # valid length (16) and invalid check bit returns False
        # Picked using Partition Testing
        num = '2221123456789019'
        self.assertFalse(credit_card_validator(num))

    def test28(self):
        # Verifies if MC Card with valid prefix (2720),
        # valid length (16) and valid check bit returns True
        # Picked using Partition Testing
        num = '2720123456789010'
        self.assertTrue(credit_card_validator(num))

    def test29(self):
        # Verifies if MC Card with valid prefix (2720),
        # valid length (16) and invalid check bit returns False
        # Picked using Partition Testing
        num = '2720123456789016'
        self.assertFalse(credit_card_validator(num))


if __name__ == '__main__':
    unittest.main(verbosity=2)
