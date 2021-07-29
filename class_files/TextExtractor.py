from class_files import match
import re

class Text_Extractor( ):
    """Extracts credit earnings from the match screenshot"""

    @staticmethod
    def text_parser(text: str):
        base_income = re.search("Total:(.+?)%", text).group(1)
        base_income = re.sub(r"\s", "", base_income)
        return base_income