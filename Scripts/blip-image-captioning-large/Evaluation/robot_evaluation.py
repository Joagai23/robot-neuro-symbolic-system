from aac_metrics.functional import spider, bleu_1, bleu_4
import pandas as pd

# Run in admin mode (Gets 5 machine translation and image captioning metrics)
def main():
    try:    
        # Read df
        true_value_df = pd.read_csv('robot_true_captions.csv')
        evaluation_df = pd.read_csv('robot_evaluation_captions_22.csv')

        true_value_captions = true_value_df['true_caption'].values
        evaluation_captions = evaluation_df['evaluation_caption'].values

        # Iterate and group captions
        chunk_size = 9
        init_value = 0
        candidates = []
        mult_references = []

        # i -> 0 - 49
        for i in range(init_value, int(len(evaluation_captions) / chunk_size)):
            current_range = int(i * chunk_size)
            true_caption = true_value_captions[i]
            evaluation_caption = evaluation_captions[current_range:current_range + chunk_size]
            candidates.append(true_caption)
            mult_references.append(evaluation_caption.tolist())

        blue_1_scores, _ = bleu_1(candidates=candidates, mult_references=mult_references)
        blue_4_scores, _ = bleu_4(candidates=candidates, mult_references=mult_references)
        #cider_d_scores, _ = cider_d(candidates=candidates, mult_references=mult_references)
        #spice_scores, _ = spice(candidates=candidates, mult_references=mult_references)
        spider_scores, _ = spider(candidates=candidates, mult_references=mult_references, java_path='C:/Program Files/Java/jre-1.8/bin/java')

        print(blue_1_scores, blue_4_scores, spider_scores)
    except PermissionError as e:
        print(e.strerror)

if __name__ == "__main__":
    #_get_java_version('C:\\Jorge\\Universidad\\JU\\2\\Thesis\\Scripts\\blip-image-captioning-large\\jdk1.8.0_202')
    main()