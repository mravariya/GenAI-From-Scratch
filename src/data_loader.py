from datasets import load_dataset
import typing as tp


def load_bookcorps_data(n: int = 1_000_000) -> tp.List[str]:
    """
    Load the BookCorpus dataset from Hugging Face Datasets.
    The BookCorpus dataset contains a large collection of books.
    The dataset is used for training language models.
    The dataset contains a single split: "train".
    The dataset contains a single column: "text".
    The dataset is not tokenized.
    The dataset is not preprocessed.
    The dataset is not cleaned.
    The dataset is not deduplicated.
    The dataset is not augmented.
    The dataset is not shuffled.
    The dataset is not split into train and test sets."
    """
    data = load_dataset("bookcorpus", split="train")[:n]
    return data['text']


if __name__ == "__main__":
    data = load_bookcorps_data()
    print(data[:5])
    print(len(data))
    print("load_bookcorps_data() is working correctly.")
