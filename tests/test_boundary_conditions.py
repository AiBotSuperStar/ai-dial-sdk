import pytest
from aidial_sdk import DIALApp
from tests.utils.endpoint_test import TestCase, run_endpoint_test

# Define boundary test cases
boundary_testcases = [
    # Test with maximum input size for tokenization
    TestCase(
        app=DIALApp(),
        deployment="test-app",
        endpoint="tokenize",
        request_body={"inputs": ["a" * 10000]},  # Assuming 10,000 is the max size
        response={"outputs": [{"status": "success", "token_count": 10000}]},
    ),
    # Test with minimum input size for tokenization
    TestCase(
        app=DIALApp(),
        deployment="test-app",
        endpoint="tokenize",
        request_body={"inputs": [""]},
        response={"outputs": [{"status": "success", "token_count": 0}]},
    ),
]

@pytest.mark.parametrize("testcase", boundary_testcases)
def test_boundary_conditions(testcase: TestCase):
    run_endpoint_test(testcase)
