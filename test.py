import os

from clear_suds_cache import clear_suds_cache
from suds.client import Client

def wsdl_path(number):
    assert number in [1,2], "never heard of test wsdl #%s" % number
    return "file://" + os.path.join(os.path.dirname(__file__), "test-wsdl/test-wsdl-%s.xml" % number)

def number_of_wsdl_cache_items():
    return len(os.listdir("/tmp/suds"))

# not going to use a test framework for this - a few asserts will be good enough

# the tool tries to clear all the caches but these tests only cover the default

#create both if they don't exist already
#no easy way to start with a clean slate without deleting the hole folder and
#affecting unrelated cached
Client(wsdl_path(1))
Client(wsdl_path(2))

initial_file_count = number_of_wsdl_cache_items()

clear_suds_cache(wsdl_path(1))

assert number_of_wsdl_cache_items() < initial_file_count, "should remove files"

file_count_without_cache_1 = number_of_wsdl_cache_items()

clear_suds_cache(wsdl_path(1))

assert number_of_wsdl_cache_items() == file_count_without_cache_1, "no change"

clear_suds_cache(wsdl_path(2))

assert number_of_wsdl_cache_items() < file_count_without_cache_1, "no change"

file_count_with_neither = number_of_wsdl_cache_items()

clear_suds_cache(wsdl_path(2))

assert number_of_wsdl_cache_items() == file_count_with_neither, "no change"

clear_suds_cache(wsdl_path(1))

assert number_of_wsdl_cache_items() == file_count_with_neither, "no change"

Client(wsdl_path(2))

assert number_of_wsdl_cache_items() == file_count_without_cache_1, "2 back in"

Client(wsdl_path(2))

assert number_of_wsdl_cache_items() == file_count_without_cache_1, "no change"

Client(wsdl_path(1))

assert number_of_wsdl_cache_items() == initial_file_count, "both back in"

print "TESTS PASSED - WILL SAY 'Ran 0 tests in 0.000s' BUT IT'S WRONG"