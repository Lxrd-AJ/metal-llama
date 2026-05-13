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
    def __init__(self, vocabFile: str):
        contents = open(vocabFile).read()