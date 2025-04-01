
import torch
from transformers import PreTrainedTokenizer, PreTrainedModel
import numpy as np

from typing import List

def extract_embeddings(
    texts: List[str],
    tokenizer: PreTrainedTokenizer,
    model: PreTrainedModel,
    batch_size: int = 16
) -> np.ndarray:
    """
    Generate dense vector embeddings for a list of texts using a Hugging Face transformer model.

    Args:
        texts (List[str]): List of input texts to embed.
        tokenizer (PreTrainedTokenizer): Tokenizer corresponding to the transformer model.
        model (PreTrainedModel): Pretrained transformer model (e.g., Legal-BERT).
        batch_size (int): Number of texts to process in each batch (default: 16).

    Returns:
        np.ndarray: 2D array of shape (num_texts, embedding_dim) containing text embeddings.
    """
    all_embeddings = []
    model.eval()
    
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        inputs = tokenizer(batch, padding=True, truncation=True, return_tensors="pt")
        
        with torch.no_grad():
            outputs = model(**inputs)
            batch_embeddings = outputs.last_hidden_state.mean(dim=1)  # [batch_size, hidden_dim]
        
        all_embeddings.append(batch_embeddings.numpy())

    return np.vstack(all_embeddings)
