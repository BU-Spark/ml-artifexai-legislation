import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.cluster import KMeans
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("nlpaueb/legal-bert-base-uncased")
model = AutoModel.from_pretrained("nlpaueb/legal-bert-base-uncased")

def extract_embeddings(texts):
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1) 
    return embeddings.numpy()

# Replace texts with actual data
texts = [
    "This is a contract that defines the terms of service.",
    "The intellectual property rights of the product are owned by the company.",
    "The defendant is charged with a violation of criminal law.",
    "The company’s merger agreement includes terms for acquisitions.",
    "Intellectual property law protects creations of the mind.",
    "The defendant was found guilty in a court of law."
]

embeddings = extract_embeddings(texts)


# Sample KMeans clustering on embedded data
n_clusters = 2  
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(embeddings)

labels = kmeans.labels_

for text, label in zip(texts, labels):
    print(f"Cluster {label}: {text}")

