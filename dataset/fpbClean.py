import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Sentiment analyzer')
parser.add_argument('--data_path', type=str, help='Path to the text file.')

args = parser.parse_args()
data = pd.read_csv(args.data_path, sep='.@', names=['text','label'], encoding='iso-8859-1')
data.to_csv('dataset/FPB100.csv')

# train, test = train_test_split(data, test_size=0.2, random_state=0)
# train, valid = train_test_split(train, test_size=0.1, random_state=0)

# train.to_csv('data/sentiment_data/train.csv',sep='\t')
# test.to_csv('data/sentiment_data/test.csv',sep='\t')
# valid.to_csv('data/sentiment_data/validation.csv',sep='\t')