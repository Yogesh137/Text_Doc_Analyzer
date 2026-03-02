from typing import Dict, List

class WordCounter:

    STOP_WORDS = {
        "the", "and", "is", "at", "which", "on", "a", "an", "as", "are",
        "was", "were", "been", "be", "have", "has", "had", "do", "does",
        "did"
    }

    def __init__(self, text: str):
        self.text = text
        self.word_frequencies = self._process_text()

    def _process_text(self) -> Dict[str, int]:
        words = self.text.split()
        frequency = {}

        for word in words:
            if len(word) < 3:
                continue

            if word in self.STOP_WORDS:
                continue

            frequency[word] = frequency.get(word, 0) + 1

        return frequency

    def get_frequencies(self) -> Dict[str, int]:
        return self.word_frequencies