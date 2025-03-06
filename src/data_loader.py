from datasets import load_dataset


def load_bookcorps_data(n=1_000_000):
    data = load_dataset("bookcorpus", split="train")[:n]
    return data['text']


if __name__ == "__main__":
    data = load_bookcorps_data()
    print(data[:5])  # Print the first 5 text samples
