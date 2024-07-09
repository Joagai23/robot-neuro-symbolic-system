import cv2 as cv
import os

# Dynamic annotation
def annotate_image(annotation:str):
    if len(annotation) != 12:
        return None
    unit = annotation[0]
    insides = annotation[1]
    color = annotation[2]
    state = annotation[3]
    shape = annotation[4]
    material = annotation[5]
    object = annotation[6]
    finish = annotation[7]
    metal_clips = annotation[8]
    rubber_ring = annotation[9]
    handle = annotation[10]
    closure = annotation[11]
    annotation_def = ''
    
    # Units
    match(unit):
        case 'o':
            annotation_def += 'one '
        case 't':
            annotation_def += 'two '
        case 's':
            annotation_def += 'several '
    # Insides
    match(insides):
        case 'f':
            annotation_def += 'full '
        case 'e':
            annotation_def += 'empty '
    # Color
    match(color):
        case 't':
            annotation_def += 'transparent '
        case 's':
            annotation_def += 'translucent '
        case 'o':
            annotation_def += 'opaque '
    # State
    match(state):
        case 'o':
            annotation_def += 'open '
        case 'c':
            annotation_def += 'closed '
    # Shape
    match(shape):
        case 'c':
            annotation_def += 'cylindrical '
        case 'r':
            annotation_def += 'rectangular '
        case 'o':
            annotation_def += 'oval '
        case 'n':
            annotation_def += 'conical '
        case 'x':
            annotation_def += 'complex-shaped '
    # Material
    match(material):
        case 'p':
            annotation_def += 'plastic '
        case 'g':
            annotation_def += 'glass '
        case 'c':
            annotation_def += 'ceramic '
        case 'm':
            annotation_def += 'metal '
    # Object
    match(object):
        case 'b':
            annotation_def += 'bottle '
        case 'j':
            annotation_def += 'jar '
        case 'v':
            annotation_def += 'vase '
        case 'c':
            annotation_def += 'container '
    # Finish
    annotation_def += 'with a '
    match(finish):
        case 't':
            annotation_def += 'twist '
        case 's':
            annotation_def += 'snap '
        case 'w':
            annotation_def += 'swing-top '
        case 'x':
            annotation_def += 'complex '
    annotation_def += 'finish'
    # Metal clips
    match(metal_clips):
        case 'm':
            annotation_def += ', metal clips'
        case 'n':
            annotation_def = annotation_def
    # Rubber ring
    match(rubber_ring):
        case 'r':
            annotation_def += ', rubber ring'
        case 'n':
            annotation_def = annotation_def
    # Handle
    match(handle):
        case 'h':
            annotation_def += ', handle'
        case 'n':
            annotation_def = annotation_def
    # Closure
    annotation_def += ' and '
    match(closure):
        case 's':
            annotation_def += 'screw '
        case 'h':
            annotation_def += 'handle '
        case 'f':
            annotation_def += 'flip-top '
        case 'g':
            annotation_def += 'grinder '
        case 'c':
            annotation_def += 'crown '
        case 'p':
            annotation_def += 'push-pull '
        case 'k':
            annotation_def += 'cork '
        case 'y':
            annotation_def += 'spray '
        case 'd':
            annotation_def += 'disc-top '
        case 'r':
            annotation_def += 'dropper '
        case 't':
            annotation_def += 'trigger '
        case 'w':
            annotation_def += 'swing-top '
        case 'a':
            annotation_def += 'snap '
        case 'n':
            annotation_def += 'no '
        case 'o':
            annotation_def += 'ropp '
    annotation_def += 'closure'
    
    return annotation_def

# Define directory and annotation file paths
#image_dir = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/Images'
#annotation_file = 'C:/Jorge/Universidad/JU/2/Thesis/Scripts/blip-image-captioning-large/Dataset_Processing/annotations.txt'
testing_dir = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/Testing'
testing_annotation_file = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/testing_annotations.txt'

# Fetch image names into list
indexes = [int(index.split('.')[0]) for index in os.listdir(testing_dir) if os.path.isfile(os.path.join(testing_dir, index))]
indexes.sort()
start_index = 528
finish_index = max(indexes) + 1

# Display the images
for image_index in range(start_index, finish_index):
    try:
        image = str(image_index) + '.jpg'
        # Read image data
        image_color = cv.imread(testing_dir + '/' + image, cv.IMREAD_COLOR)
        (h, w) = image_color.shape[:2]
        new_w = 250
        new_h = int(h * (new_w / float(w)))
        # Display image
        cv.namedWindow(image, cv.WINDOW_NORMAL)
        cv.moveWindow(image, 0, 0)
        cv.imshow(image, image_color)
        #image_color = cv.resize(image_color, (960, 540))
        cv.resizeWindow(image, new_w, new_h)
        cv.waitKey(1500) & 0xFF
        # Read console input from user
        image_description = input()
        annotation = annotate_image(image_description)
        # Open annotation file
        file = open(testing_annotation_file, "a")
        # Save description into annotations text file
        file.write(image + ' - ' + annotation + '\n')
        file.close()
        cv.destroyWindow(image)
    except:
        cv.destroyAllWindows()
        print("Error at image index " + str(image_index))