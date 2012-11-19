all:
	echo "Nothing to be done - this is python!"

test:
	-python -m unittest tests.Course tests.University tests.Paypal
	-find -name \*.py -exec ../tools/pep8.py {} \+
