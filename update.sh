#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Find all outdated packages and write to a file
pip list --outdated --format=columns > outdated_packages.txt

# Initialize a line counter
line_counter=0

# Read the outdated packages file and update each package
while IFS= read -r line; do
    # Increment the line counter
    line_counter=$((line_counter + 1))
    
    # Skip the first two lines
    if [ "$line_counter" -le 2 ]; then
        continue
    fi
    
    # Extract the package name from the line (format: Package Version Latest Type)
    package=$(echo "$line" | awk '{print $1}')
    echo "Updating $package"
    pip install --upgrade "$package"
done < outdated_packages.txt

# Clean up the outdated packages file
rm outdated_packages.txt
pip freeze --local > requirements.txt
# Deactivate the virtual environment
deactivate

echo "All packages have been updated."
