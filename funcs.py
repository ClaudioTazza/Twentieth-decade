import random

def foo():
    print "foo"

def bar():
    print "bar"

list_of_funcs = [foo, bar]

f = random.choice(list_of_funcs)
f()
