import pytest


def test_method1():
	return 2

def test_method2():
	assert test_method1() == 2
	
def test_fun(mocker):
	mocker.patch('test_sample1.test_method1' , return_value = 3)
	assert test_method1() == 3

