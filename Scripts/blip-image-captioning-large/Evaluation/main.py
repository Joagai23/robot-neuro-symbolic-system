import subprocess
from nltk.translate.bleu_score import sentence_bleu
from aac_metrics.functional import cider_d, spice, spider, bleu, bleu_1, bleu_4
import pandas as pd

def main():
    try:    
        # Read df
        evaluation_file = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/evaluation_file.csv'
        df = pd.read_csv(evaluation_file)

        captions = df['caption']
        evaluations = df['evaluation']

        sentences_evaluate = []
        targets = []

        # 4-gram cumulative BLEU
        for caption, evaluation in zip(captions, evaluations):
            # remove commas
            caption = str(caption).replace(", ", " ")
            evaluation = str(evaluation).replace(", ", " ")
            sentences_evaluate.append(evaluation)
            targets.append([caption])
        #corpus_scores, sents_scores = bleu_1(mult_references=targets, candidates=sentences_evaluate)
        corpus_scores, sents_scores = spider(mult_references=targets, candidates=sentences_evaluate, java_path='C:/Program Files/Java/jre-1.8/bin/java')
        print(corpus_scores, sents_scores)
    except PermissionError as e:
        print(e.strerror)

if __name__ == "__main__":
    #_get_java_version('C:\\Jorge\\Universidad\\JU\\2\\Thesis\\Scripts\\blip-image-captioning-large\\jdk1.8.0_202')
    main()