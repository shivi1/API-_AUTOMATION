import pytest
#  Test Case code must be written inside a method
#  Method name must be started with test
#  Print statement output display on console   -s
#  Verbose mode -  display test cases name with status(Result)    -v
#  Execute Specific test case -k
#  -m <<Tag Name>> example -m Sanity is used to test specific test case collection
#  -m <<"not Tag Name">> example -m "not TopPriority" is used to skip the test specific test case collection
#  Execute test cases with or condition example -m "TopPriority or Regression"
#  Execute test cases with and condition example -m "Smoke and Regression"
#  --disable-pytest-warnings to filter warnings example pytest -s -v --disable-pytest-warning -m "Smoke and  Regression" AutomationCases


@pytest.mark.Sanity
def test_tc_002_Registration_Testing():
    print("This is Sanity Test Case.....")
    print("This is end of my test cases")
