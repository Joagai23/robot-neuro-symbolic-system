import os
import pickle as pkl

dir_name = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/LabPics Medical/Test'
new_dir = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/Images'
cup_file = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/cup_images'
osdd_dir = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/OSDD/Images'
glass_bottles = 'C:/Jorge/Universidad/JU/2/Thesis/Scripts/Jar-Knowledge-Base/code/fetching/glassBottles'
glass_jars = 'C:/Jorge/Universidad/JU/2/Thesis/Scripts/Jar-Knowledge-Base/code/fetching/glassJars'
plastic_bottles = 'C:/Jorge/Universidad/JU/2/Thesis/Scripts/Jar-Knowledge-Base/code/fetching/plasticBottles'
plastic_jars = 'C:/Jorge/Universidad/JU/2/Thesis/Scripts/Jar-Knowledge-Base/code/fetching/plasticJars'
testing_jars = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/Testing'

def get_max_value(directory):
    indexes = [int(index.split('.')[0]) for index in os.listdir(directory) if os.path.isfile(os.path.join(directory, index))]
    max_value = max(indexes) + 1
    return max_value

def add_images(original_directory, new_directory):
    names = [name for name in os.listdir(original_directory) if os.path.isdir(os.path.join(original_directory, name))]
    max_value = get_max_value(original_directory)
    for i, folder in enumerate(names):
        index_value = i + max_value
        file_path = original_directory + '/' + folder + '/Image.jpg'
        destination = new_directory + '/' + str(index_value) + '.jpg'
        os.rename(file_path, destination)

def reset_index(directory):
    indexes = [index for index in os.listdir(directory) if os.path.isfile(os.path.join(directory, index))]
    indexes.sort()
    for i, file_name in enumerate(indexes, start=1):
        file_path = directory + '/' + str(file_name)
        new_name = directory + '/' + str(i) + '.jpg'
        os.rename(file_path, new_name)

def move_images_to_main(main_directory, images_to_move_directory):
    names = [name for name in os.listdir(images_to_move_directory) if os.path.isfile(os.path.join(images_to_move_directory, name))]
    max_index = get_max_value(main_directory)
    for i, file_name in enumerate(names, start = max_index):
        file_path = images_to_move_directory + '/' + file_name
        new_name = main_directory + '/' + str(i) + '.jpg'
        os.rename(file_path, new_name)

reset_index(testing_jars)