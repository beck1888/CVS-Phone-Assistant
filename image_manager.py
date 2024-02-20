import os

image_database = {
    "CVS":"/Users/beckorion/Documents/Python/mini-scripts\:random\:tests/pharmacy/pictures/cvspharmacy_outside.jpeg ",
}

def open(image):
    try:
        image_database[image]
    except:
        print(f"WARNING: No image path found for the shortcut {image}")

    os.system(f"open -a \"Preview\" {image_database[image]}")

def kill():
    os.system("killall Preview")