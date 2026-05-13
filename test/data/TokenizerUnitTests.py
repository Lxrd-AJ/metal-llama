from data.Tokenizer import CharacterTokenizer


class CharacterTokenizerTests:
    shakeFile = "./data/datasets/tinyshakespeare.txt"

    specimen = CharacterTokenizer(vocabFile=shakeFile)

    def test_canEncodeDecode(self):
        words = [
            "Hello",
            "'em! They say!",
            "tribunes for the people,--",
            "Senators, &C:",
            "Now stops thy spring; my sea sha$l suck them dry,"
        ]

        for word in words:
            encoded = self.specimen.encode(word)
            assert self.specimen.decode(encoded) == word