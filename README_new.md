# Color Detection Project

This project is a simple Python application that helps you identify the color of any point in an image.

## What this project does

- Opens an image file
- Lets you click on the image
- Reads the RGB values of the clicked pixel
- Finds the closest matching color name
- Shows the result on the screen
- Stores the detected color information in colors.csv

## Requirements

You need Python and these libraries installed:

- OpenCV
- NumPy
- pandas

Install them with:

pip install opencv-python numpy pandas

## How to run

Run the script from the project folder:

python color_detection.py --image your_image.jpg

For example:

python color_detection.py --image colorpic.jpg

## How the program works

1. The program loads the selected image.
2. It waits for a mouse click.
3. It reads the pixel color at the clicked position.
4. It compares that color with the stored list of known colors.
5. It displays the color name and RGB values.

## Project files

- color_detection.py — main program
- colors.csv — stores color information
- colorpic.jpg — sample image used for testing

## How to use

- Click on the image to detect a color
- Press Esc to close the window

## Notes

This project is a good example of basic image processing and color matching in Python.