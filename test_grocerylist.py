#Testing the Grocery List
#test_grocerlylist.py
# In this assignment you are going to add exception handling and unit tests to your existing Grocery App application. 

# - Are there places in your app where you need to handle exceptions? 

# - What are different unit tests you are going to implement for your Grocery App application 

# - How can you create separate your different classes into separate modules? 

import unittest

from grocerylist import *

class GroceryTests(unittest.TestCase)

    def setUp(self):
        print("Testing the sum of the list")
        self.??? - ???()
        print("SETUP")

    def test_display_sum():
        print("Test to display sum of prices")
        result = self.???.display_full()


    def tearDown(self):
        print("TEARDOWN")

unittest.main()
