from abc import ABC, abstractmethod

class Tokenizer(ABC):
    @abstractmethod
    def encode(self, text: str) -> list[int]:
        """Encode text into a list of integers."""
        pass

    @abstractmethod
    def decode(self, tokens: list[int]) -> str:
        """Decode a list of integers back into text."""
        pass


class CharacterTokenizer(Tokenizer):
    def __init__(self, contents: str):
        vocab = sorted(set(contents))
        self.__stoi = {c:i for i, c in enumerate(vocab)}
        self.__itos = {i:c for c, i in self.__stoi.items()}

    def encode(self, text: str) -> list[int]:
        return [self.__stoi[c] for c in text]

    def decode(self, tokens: list[int]) -> str:
        return "".join([self.__itos[i] for i in tokens])