import torch
from data.Datasets import TinyShakespeareDataset
from data.Tokenizer import *

class TinyShakespeareDatasetUnitTests:

    def test_canCreateDatasetWithCorrectLength(self):
        specimen1 = self.createSpecimen(blockSize=64)
        specimen2 = self.createSpecimen(blockSize=128)
        specimen3 = self.createSpecimen(blockSize=256)
        specimen4 = self.createSpecimen(blockSize=512)

        assert len(specimen1) > len(specimen2) > len(specimen3) > len(specimen4)

    def test_canGetItem(self):
        blockSize = 256
        specimen = self.createSpecimen(blockSize)

        (X, Y) = specimen[0]
        assert (X.dtype, Y.dtype) == (torch.long, torch.long)
        assert X.shape == Y.shape
        assert torch.equal(X[1:], Y[:-1])
        assert len(X) == len(Y) == blockSize

    def test_canGetLastItem(self):
        blockSize = 64
        specimen = self.createSpecimen(blockSize)
        numBlocks = len(specimen)
        (X, Y) = specimen[numBlocks-1]
        
        assert torch.equal(X[1:], Y[:-1])
        assert len(X) == len(Y) == blockSize

    def createSpecimen(self, blockSize: int) -> TinyShakespeareDataset:
        txtFile="./data/tinyshakespeare.txt"
        data = open(txtFile).read()
        tokenizer = CharacterTokenizer(contents=data)

        return TinyShakespeareDataset(
            data=data,
            tokenizer=tokenizer,
            blockSize=blockSize
        )