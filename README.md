# CS269GroupProject
Detailed description of the dataset and the next step (work in progress) is at: [Google Docs ](https://docs.google.com/document/d/1SsRv5j8TZkH0_qsuulHQcyvrwEd4elUuji0cc_Yu17w/edit?usp=sharing)


# Dataset
Use `python3 clean.py` to generate the csv file from the json raw data for Financial Phrase Bank dataset. In addition, `util.py` and `finbert.py` are also used to clean up raw Financial Phrase Bank dataset and organize them into the correct format that can be feeded into FinBERT or fine-tuned FinBERT model.

1. dataset/ : data in this folder are raw data. 
2. data/ : FPB dataset is splitted into 3 parts (training, validation, and testing). 
3. augmented_dataset: the augmented adversarial examples.
   1. `improved_genetic_algo_augmented.csv` is build by augmenting `semantic_attack_examples.csv` with improved genetic algorithm. FinBERT has about 43% accuracy on this data.
   2. `wordnet_augmented.csv`: this is our first try to augmenting data. But it fails to attack the original model.
4. `semantic_attack_examples.csv` contains the adversarial examples the can fool FinBERT model. FinBERT model has 0% accuracy on this dataset. 


# Setup
1. Create conda environment: `conda env create -f req.txt`
2. Activate conda: `conda activate cs269`
3. Open Jupyter Notebook: `jupyter notebook FinBERT.ipynb`
4. After you finish coding: `conda deactivate` 