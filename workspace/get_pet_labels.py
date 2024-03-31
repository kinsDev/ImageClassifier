#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Kinsley Kaimenyi Gitonga
# DATE CREATED: 10th/11/2023                               
# REVISED DATE: 15th/11/2023
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    # Retrieve the filenames from the specified image directory
    pet_filenames = listdir(image_dir)

    # Iterate through the filenames to convert them to lowercase and exclude system files
    for index in range(len(pet_filenames)):
        # Check if the filename does not start with a dot (.)
        if not pet_filenames[index].startswith("."):
            pet_filenames[index] = pet_filenames[index].lower()

    # Iterate through the filenames to extract and format pet names, excluding system files
    pet_names = []
    for filename in pet_filenames:
        # Check if the filename does not start with a dot (.)
        if not filename.startswith("."):
            split_filename = filename.split("_")
            pet_name = " "
            for name_part in split_filename:
                # Include only alphabetical parts of the filename
                if name_part.isalpha():
                    pet_name += name_part + " "
            pet_names.append(pet_name.strip())

    # Create an empty dictionary named results_dic
    results_dic = dict()

    # Get the list of filenames again
    filename_list = listdir(image_dir)

    # Iterate through the filenames to populate the results_dic dictionary
    for key in range(len(filename_list)):
        if filename_list[key] not in results_dic:
            # Create a list with the pet name and assign it to the filename key
            label_list = [pet_names[key]]
            results_dic[filename_list[key]] = label_list
        else:
            print("Warning: Key =", filename_list[key], "already exists in results_dic with value =", results_dic[filename_list[key]])

    # Print all key-value pairs in the results_dic dictionary
    for key, value in results_dic.items():
        print("Filename =", key, "Pet Label =", value)

    # Replace None with the results_dic dictionary that you created with this function
    return results_dic

