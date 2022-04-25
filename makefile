.PHONY: typehint
typehint:
	mypy src/

.PHONY: lint
lint:
	pylint src/