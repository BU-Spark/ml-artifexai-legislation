
import torch
# from transformers import PreTrainedTokenizer, PreTrainedModel
import numpy as np
import pandas as pd

from typing import List, Tuple
import spacy
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sentence_transformers import SentenceTransformer

nlp = spacy.load("en_core_web_sm", disable=["ner", "parser"])
custom_stopwords = set([
    "section", "chapter", "general", "laws", "hereby", "amended", "insert", "enact",
    "enactment", "law", "legislation", "act", "resolve", "order", "committee", "bill",
    "house", "senate", "commonwealth", "public", "private", "regulation", "statute",
    "effective", "provision", "subsection", "notwithstanding", "pursuant", "authorized",
    "office", "duty", "power", "authority", "text", "available", "clerk", "authorized",
    "recess", "investigation", "study", "authorized", "sitting", "office", "provide",
    "shall",  "state", "amend", "official", "edition", 
    "insert", "follow", "paragraph", "clause", "department", "relative",
    "massachusetts", "submit", "", "establish",
        "leave",     # very common, ambiguous
    "sick",      # procedural in employee/sick leave laws
    "employee",  # generic term across labor bills
    "fiscal",    # procedural, not topically defining
    "year",      # always present in budget/timing
    "commission",# too procedural, like “committee”
    "inspection",# structural
    "item",      # budget structure
    "county",    # geographical, not thematic
    "trust"      # legal term, often in estate/tax docs
])

stopwords = ENGLISH_STOP_WORDS.union(custom_stopwords)
stopwords = set(stopwords)
stopwords = stopwords.difference({"fire", "children", "study", "family", "order", "regulation"})

def clean_text(text: str)-> str:
    if pd.isnull(text):
        return np.nan
    doc = nlp(text.lower())
    tokens = [
        token.lemma_ for token in doc
        if token.is_alpha and not token.is_stop and token.lemma_ not in stopwords
    ]
    cleaned = " ".join(tokens)
    if cleaned == "":
        return np.nan
    return " ".join(tokens)

def extract_embeddings(df: pd.DataFrame, text_col_name:str)->Tuple[List, pd.DataFrame]:
    df["cleaned"] = df[text_col_name].apply(clean_text)
    df.cleaned = df.cleaned.fillna('further amend or relative to other act')

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(df.cleaned.values, show_progress_bar=True)

    return embeddings, df
