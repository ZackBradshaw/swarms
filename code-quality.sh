#!/bin/bash

run_code_quality_checks() {
    # Format the code using black
    black .

    # Check for linting errors using flake8
    flake8 .

    # Perform static type checking using mypy
    mypy .

    # Execute all the tests using pytest
    pytest
}

run_code_quality_checks

# If the script requires administrative privileges, use sudo
# sudo ./code-quality.sh
