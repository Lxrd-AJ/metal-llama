import torch
from torch.utils.data import Dataset
from .Tokenizer import CharacterTokenizer

class TinyShakespeareDataset(Dataset):
    def __init__(self, data: str, tokenizer: CharacterTokenizer, blockSize: int = 256):
        self.data = data
        self.blockSize = blockSize
        self.tokens = torch.tensor(tokenizer.encode(self.data), dtype=torch.long)

    def __len__(self) -> int:
        numBlocks = (len(self.tokens) - 1) // self.blockSize
        return numBlocks

    def __getitem__(self, idx) -> tuple[torch.Tensor, torch.Tensor]:
        startIdx = idx * self.blockSize
        X = self.tokens[startIdx : startIdx + self.blockSize]
        Y = self.tokens[startIdx + 1 : (startIdx+1)+self.blockSize]

        return (X, Y)