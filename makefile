build-HelloWorldFunction:
	cp src/lambda_function.py src/layers/command.py src/layers/data.py src/layers/execution_environment.py src/__init__.py $(ARTIFACTS_DIR)