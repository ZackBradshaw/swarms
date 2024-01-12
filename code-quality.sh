#!/bin/bash

# Set execute permissions for the script
chmod +x code-quality.sh

# Run code quality checks
black .
flake8 .

# If script requires administrative privileges, run with sudo
if [ "$EUID" -ne 0 ]; then
  sudo ./code-quality.sh
fi
