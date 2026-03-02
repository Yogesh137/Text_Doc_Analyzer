import re

class TextReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_and_normalize(self) -> str:
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                text = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")

        # Convert to lowercase
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", "", text)

        return text