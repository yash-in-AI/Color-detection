# Color Detection Project

This project is a simple Python program that detects the color of a point in an image.

## What it does
- Open an image
- Let the user click on the image
- Read the RGB values of that pixel
- Match the color with a list of known colors
- Show the result on the screen

## Requirements
Install these packages:

pip install opencv-python numpy pandas

## Run the program
Use this command:

python color_detection.py --image your_image.jpg

Example:

python color_detection.py --image colorpic.jpg

## How it works
1. Load the image.
2. Click on the image.
3. Read the pixel color.
4. Compare it with the CSV data.
5. Display the result.

## Files
- color_detection.py
- colors.csv
- colorpic.jpg

## Notes
- Press Esc to close the window.
- Click on the image to detect a color.
