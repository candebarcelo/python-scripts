import sys
import os  # or pathlib
import re
from PIL import Image

# run from terminal and state /img_folder (where the pics are) and /new_folder (where the new pics will go)


def converter(img_folder, new_folder):
    path = os.path.join('C:', 'Users', 'candelaria.barcelo', 'OneDrive - Accenture', 'Cande',
                        'Python', 'img_processing', new_folder)  # os.path.join joins the path
    # with / or \ for Mac or Windows
    # os.path.exists checks if the path exists and returns T/F
    if not os.path.exists('./' + new_folder):
        os.makedirs(new_folder)  # os.makedirs makes a new folder
        print("the new directory has been created!")

    # os.listdir returns a list of all files in that folder
    for item in os.listdir(img_folder):
        img_path = os.path.join(img_folder, item)
        img = Image.open(img_path)
        # removes .format from file name
        img_filename = re.match(r"^([A-Za-z0-9]+)\.", item).group(1)
        # so it's not hi.jpg.png
        print(img_filename)
        new_img_path = os.path.join(new_folder, img_filename)
        # save to new folder by saying folder path + name + format
        img.save(new_img_path + '.png', 'png')

    print('done! :)')


converter(sys.argv[1], sys.argv[2])
