from class_files import match, image, TextExtractor
from os import listdir
from os.path import isfile, join
from pathlib import Path


class Main:


    @staticmethod
    def main():
        img_list = Main.get_files()

        match_list = {}

        for i in range(len(img_list)):
            cv_image = image.Image.import_img(img_list[i][0])
            img_text = image.Image.read_img(cv_image)
            parsed_text = int(TextExtractor.Text_Extractor.text_parser(img_text))

            obj = match.Match()
            obj.base_income = parsed_text
            dict_element = {i: obj}
            match_list.update(dict_element)


    @staticmethod
    def get_files():

        img_dir = "C:\\Users\\José\\PycharmProjects\\WoWsOCR"
        img_list = []
        for i in listdir(img_dir):
            if i.__contains__("jpg"):
                if i.__contains__("win"):
                    img_list.append([i, 1])
                elif i.__contains__("defeat"):
                    img_list.append([i, 0])

        return img_list


if __name__ == '__main__':
    Main.main()
