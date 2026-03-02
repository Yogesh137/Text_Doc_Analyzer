from typing import Dict, List, Tuple

class StatisticsReport:

    def __init__(self, word_frequencies: Dict[str, int]):
        self.word_frequencies = word_frequencies
        self.total_word_count = sum(word_frequencies.values())
        self.unique_word_count = len(word_frequencies)

    def average_word_length(self) -> float:
        if self.total_word_count == 0:
            return 0.0

        total_length = sum(
            len(word) * count
            for word, count in self.word_frequencies.items()
        )

        return round(total_length / self.total_word_count, 2)

    def longest_word(self) -> str:
        if not self.word_frequencies:
            return ""

        return max(self.word_frequencies.keys(), key=len)

    def most_frequent_word(self) -> Tuple[str, int]:
        if not self.word_frequencies:
            return ("", 0)

        word = max(self.word_frequencies, key=self.word_frequencies.get)
        return (word, self.word_frequencies[word])

    def getTopNWords(self, n: int) -> List[Tuple[str, int]]:
        return sorted(
            self.word_frequencies.items(),
            key=lambda item: item[1],
            reverse=True
        )[:n]

    def getWordsStartingWith(self, prefix: str) -> List[str]:
        prefix = prefix.lower()

        words = [
            word for word in self.word_frequencies.keys()
            if word.startswith(prefix)
        ]

        return sorted(words)

    def exportReport(self, output_file_path: str) -> None:
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write("Text Analysis Report\n")
            file.write("====================\n\n")
            file.write(f"Total Word Count: {self.total_word_count}\n")
            file.write(f"Unique Word Count: {self.unique_word_count}\n")
            file.write(f"Average Word Length: {self.average_word_length()}\n")
            file.write(f"Longest Word: {self.longest_word()}\n")

            most_word, count = self.most_frequent_word()
            file.write(f"Most Frequent Word: {most_word} ({count})\n\n")

            file.write("Top 10 Words:\n")
            for word, freq in self.getTopNWords(10):
                file.write(f"{word}: {freq}\n")