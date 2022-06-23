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

a=100
#Decorator - to Skip a particular test case
#@pytest.mark.skip --- Unconditional
#@pytest.mark.skip("Skipping as this functionality is not working, developer will fix it in new build") --Unconditional with reason

#@pytest.mark.skipif(a>99,reason="Skipping as this functionality is not working, developer will fix it in new build") --Conditional

@pytest.mark.TopPriority
def test_tc_001_Login_Logout_Testing():
    print("This is Smoke Test Case.....")
    print("This is end of my test cases")

#@pytest.mark.skipif(a>98,reason="Skipping as this functionality is not working, developer will fix it in new build") --Conditional
@pytest.mark.Sanity
def test_tc_003_Login_Logout_Invalid_Credentials():
    print("This is Sanity test case 3.....")
    print("This is end of test case")
