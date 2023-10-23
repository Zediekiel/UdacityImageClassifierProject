#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Ian McCandliss
# DATE CREATED: 10/15/23                                 
# REVISED DATE: 10/20/23
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


# TODO 2: Define get_pet_labels funtion below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 

#"""
#    Creates a dictionary of pet labels (results_dic) based upon the filenames 
#    of the image files. These pet image labels are used to check the accuracy 
#    of the labels that are returned by the classifier function, since the 
#    filenames of the images contain the true identity of the pet in the image.
#    Be sure to format the pet labels so that they are in all lower case letters
#    and with leading and trailing whitespace characters stripped from them.
#    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
#    Parameters:
#     image_dir - The (full) path to the folder of images that are to be
#                 classified by the classifier function (string)
#    Returns:
#      results_dic - Dictionary with 'key' as image filename and 'value' as a 
#      List. The list contains for following item:
#         index 0 = pet image label (string)
#    """
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    in_files = listdir(image_dir)        
    results_dic = dict()
    for file in in_files:
        if file[0] != '.':
            pet_label = ""
           # TODO: 2a. BELOW REPLACE pass with CODE that will process each 
           #          filename in the in_files list to extract the dog breed 
           #          name from the filename. Recall that each filename can be
           #          accessed by in_files[idx]. Be certain to place the 
           #          extracted dog breed name in the variable pet_label 
           #          that's created as an empty string ABOVE            
## Sets string to lower case letters
            low_pet_file = file.lower()
## Splits lower case string by _ to break into words 
            word_list_pet_file = low_pet_file.split("_")
## Create pet_name starting as empty string

## Loops to check if word in pet name is only
## alphabetic characters - if true append word
## to pet_name separated by trailing space 
#Note: Join method suggested as part of previous exam submission
            pet_label = ' '.join(word.strip() for word in word_list_pet_file if word.isalpha())
## Prints resulting pet_name
            if pet_label not in results_dic:
                results_dic[file] = [pet_label]
            else:
                print('Warning, duplicate file exists in directory',in_files[file])
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
