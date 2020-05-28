init:
    pip install -r requirements.txt

test:
    py.test tests

freeze:
    pip freeze > requirements.txt

.PHONY: init test freeze
