# File Name: zilog.py
# Student Name: Cam Shinker,  Ryan Jacob
# email: shinkecj@mail.uc.edu,   Jacobry@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/27/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Create a data viz using this AI data

# Brief Description of what this module does: Learning about how to work with different data types.
# Citations: https://pythonexamples.org/python-pillow-show-display-image/

# Anything else that's relevant:

from PIL import Image

def show_logo(image):
    """
    @param image str: The file path for your image
    """
    my_image = Image.open(image)
    my_image.show()



