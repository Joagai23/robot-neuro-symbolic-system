#annotation_file = 'C:/Jorge/Universidad/JU/2/Thesis/Scripts/blip-image-captioning-large/Dataset_Processing/annotations.txt'
#dataset_file = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/Images/annotations/metadata.csv'
testing_annotation_file = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/testing_annotations.txt'
testing_dataset = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/testing_annotations.csv'

text_file = open(testing_annotation_file, "r")
csv_file = open(testing_dataset, "a")
for line in text_file.readlines():
    csv_line = line.replace(", ", " ")
    csv_line = csv_line.replace(" - ", ",")
    csv_file.write(csv_line)

text_file.close()
csv_file.close()