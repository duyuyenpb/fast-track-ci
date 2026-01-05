def test_math_logic():
    assert 1 + 1 == 2
    print("Test Passed: Logic is sound!")

def test_string_logic():
    assert "Global" in "Go Global"
    print("Test Passed: Ready to go Global!")


def test_list_operations():
    test_list = [1, 2, 3, 4, 5]
    assert len(test_list) == 5
    assert 3 in test_list
    print("Test Passed: List operations work correctly!")


def test_dictionary_operations():
    test_dict = {"name": "Alice", "age": 30}
    assert test_dict["name"] == "Alice"
    assert test_dict["age"] == 30
    print("Test Passed: Dictionary operations work correctly!")
