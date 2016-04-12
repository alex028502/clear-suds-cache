# this is for setting up for development and testing

.PHONY: install test clear

install: virtualenv
	$</bin/python setup.py install
test: install
	virtualenv/bin/python setup.py test # test that things get deleted
	# ok the library works

	# now let's just make sure the exe runs without error
	virtualenv/bin/clear-suds-cache http://example.com
	# at least we know it runs - and probably works because we tested the
	# command that it wraps up
virtualenv:
	virtualenv $@
	echo "*" > $@/.gitignore
clean:
	rm -rf virtualenv
	rm -rf *.egg-info
	rm -rf build
