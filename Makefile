SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run mypy pytest_modified_env tests/*.py
	poetry run flake8 .

.PHONY: unit
unit:
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: lint package unit

