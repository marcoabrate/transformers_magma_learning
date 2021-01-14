import re

# General configurations

get_cpts = lambda df, bid:\
    sorted(list(set(df.loc[bid].index.get_level_values(0).tolist())),
    key=lambda x: int(re.search(r'\d+', x).group()))

get_bullets = lambda df, bid, cpt: df.loc[bid, cpt].bullets[0]

REPLACE_ABBR = False            # set to True to replace abbreviations

SPECIAL_CHAR_FILE = '/content/drive/My Drive/MAGMA: Summarization/special_char_file.txt'

REMOVE_PAR = False              # set to True to remove text between parentheses

SEED = 42                       # random seed, set for reproducibility

MODEL_MAX_LEN = 1019            # maximum input length fro BART and PEGASUS

BULLETS_MIN_LEN = 50
BULLETS_MED_LEN = 180           # gold summaries median length
BULLETS_MAX_LEN = 350

ONE_BULLET_MIN_LEN = 10
ONE_BULLET_MED_LEN = 30
ONE_BULLET_MAX_LEN = 150

LENGTH_PENALTY = 1
NUM_BEAMS = 4
NO_REPEAT_NGRAM_SIZE = 5

MAX_RATIO = 0.25                 # maximum text ratio

ROUGE_TYPES = ['rouge1', 'rouge2', 'rougeL']

# assign the bullets based on this ROUGE type (1, 2, or L)
ROUGE_TYPE_RECALL = 'rougeL_recall'

# Datasets path
DATASET_PATH =  '/content/drive/My Drive/MAGMA: Summarization/datasets/'
