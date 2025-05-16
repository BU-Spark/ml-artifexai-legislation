
import torch
from transformers import PreTrainedTokenizer, PreTrainedModel
import numpy as np

from typing import List

def extract_embeddings(
    texts,
    tokenizer,
    model,
    batch_size: int = 64
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
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()
    
    all_embeddings = []

    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        inputs = tokenizer(batch, padding=True, truncation=True, return_tensors="pt").to(device)

        with torch.no_grad():
            outputs = model(**inputs)
            batch_embeddings = outputs.last_hidden_state.mean(dim=1).cpu().numpy()

        all_embeddings.append(batch_embeddings)

    return np.vstack(all_embeddings)


# EXAMPLE USAGE
# tokenizer = AutoTokenizer.from_pretrained("nlpaueb/legal-bert-base-uncased")
# model = AutoModel.from_pretrained("nlpaueb/legal-bert-base-uncased")

# embeddings = extract_embeddings(list(df['clean_text']), 
#                                     tokenizer, 
#                                     model)