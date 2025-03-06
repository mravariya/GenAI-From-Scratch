import typing as tp
from data_loader import load_bookcorps_data

data = load_bookcorps_data()


def find_characters_in_data(data: tp.List[str]) -> tp.List[str]:
    characters = set()
    for sentence in data:
        characters.update(set(sentence))
    return sorted(list(characters))


if __name__ == "__main__":
    characters = find_characters_in_data(data)
    print(characters)
