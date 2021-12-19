from hello import add_one, subtract_one

def setup_function(function):
    print("Running Setup: %s" % function.__name__)
    function.x = 10


def teardown_function(function):
    print("Running Teardown: %s" % function.__name__)
    del function.x

### Run to see failed test
# def test_hello_add_one():
#     assert add_one(test_hello_add_one.x) == 12

def test_add_one():
    
    assert add_one(test_add_one.x) == 11


def test_subtract_one():
    
    assert subtract_one(test_subtract_one.x) == 9



