#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <input_directory> <output_directory>"
    exit 1
fi

# Assign input and output directories
input_dir="$1"
output_dir="$2"

# Check if the input directory exists
if [ ! -d "$input_dir" ]; then
    echo "Input directory does not exist: $input_dir"
    exit 1
fi

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Loop through all .png files in the input directory
for file in "$input_dir"/*.png; do
    # Get the base name of the file (without extension)
    base_name=$(basename "$file" .png)
    
    # Define the output file path
    output_file="$output_dir/$base_name.webp"
    
    # Convert the .png file to .webp using cwebp
    cwebp "$file" -o "$output_file"
    
    # Check if the conversion was successful
    if [ $? -eq 0 ]; then
        echo "Converted: $file -> $output_file"
    else
        echo "Failed to convert: $file"
    fi
done

echo "Conversion complete!"
