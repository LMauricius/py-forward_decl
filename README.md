# py-forward_decl
A simple module for supporting forward references

# What are those?
Forward references are references to objects that haven't been assigned yet.
The reference is declared as just a name of the variable that has been forward declared.
Forward declaration is a concept in many programming languages that declares the existance of a variable or a function before its value has been defined.

# Why tho?
In 99% of cases when you would think of using forward references there is a better way to do it in Python.
This is for the other 1%.
Like when you need to reference a class from deep within an expression inside a class variable inside that class' definition.
Also useful for recursive parser production rules that are defined using Python's semantics.

# Installation
Install it using pip:
```
pip install forward-decl
```

# Usage

Basic example:
```python
var2 = FwDecl()

var1 = OpaqueFwRef("var2")
var2 = "Hello"

print(var1.get_ref()) # prints 'Hello'
```

A more useful case:
```python
MyClass = FwDecl()

class MyClass:
    clsReference = OpaqueFwRef("MyClass")
    clsVar = "Hello"

print(MyClass.clsReference.get_ref().clsVar) # prints 'Hello'
```