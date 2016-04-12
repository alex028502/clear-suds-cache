from setuptools import setup

setup_args = {}
setup_args["name"] = 'clear_suds_cache'
setup_args["description"] = 'clear suds cache for a single wsdl'
setup_args["version"] = "0.0"
setup_args["install_requires"] = ['suds-jurko']
setup_args["test_suite"] = "test"
setup_args["scripts"] = ['bin/clear-suds-cache']
setup_args["packages"] = ['clear_suds_cache']
setup(**setup_args)
