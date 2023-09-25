from forward_decl import *

import unittest
 
# Define class to test the program
class TestBasicFunctionality(unittest.TestCase):

    def test_local_fwref(self):

        var2 = FwDecl()
        var1 = OpaqueFwRef("var2")
        var2 = "Hello"

        self.assertIsNotNone(
            var1.get_ref(),
            "get_ref doesn't find the assigned object"
        )
        self.assertIs(
            var1.get_ref(),
            var2,
            "get_ref doesn't find the correct object"
        )

    def test_class_fwref(self):

        MyClass = FwDecl()

        class MyClass:
            clsReference = OpaqueFwRef("MyClass")
            clsVar = "Hello"

        self.assertIsNotNone(
            MyClass.clsReference.get_ref(),
            "get_ref doesn't find the assigned object"
        )
        self.assertIs(
            MyClass.clsReference.get_ref().clsVar,
            MyClass.clsVar,
            "get_ref doesn't find the correct object"
        )

if __name__ == '__main__':
    unittest.main()