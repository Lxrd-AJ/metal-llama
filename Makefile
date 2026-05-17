.PHONY: all test

all: test

test:
	uv run pytest -v
