from text_reader import TextReader
from word_counter import WordCounter
from statistics_report import StatisticsReport


def main():
    reader = TextReader("sample.txt")
    normalized_text = reader.read_and_normalize()

    counter = WordCounter(normalized_text)
    frequencies = counter.get_frequencies()

    report = StatisticsReport(frequencies)

    print("Total Words:", report.total_word_count)
    print("Unique Words:", report.unique_word_count)
    print("Average Word Length:", report.average_word_length())
    print("Longest Word:", report.longest_word())
    print("Most Frequent Word:", report.most_frequent_word())
    print("\nTop 5 Words:", report.getTopNWords(5))
    print("\nWords starting with 'de':", report.getWordsStartingWith("de"))

    report.exportReport("analysis_output.txt")


if __name__ == "__main__":
    main()