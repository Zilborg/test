from . import app


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def test_hello_world():
    result = app.hello_world()
    expected_result = 'Hello, World!'

    assert expected_result == result
