from hello_pipeline import greet


def test_greet_default():
    assert greet() == "Hello, Azure DevOps! This build ran successfully. test"
