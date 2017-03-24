test:
	python3 -m unittest
	coverage run test_rpn.py

.PHONY: test
