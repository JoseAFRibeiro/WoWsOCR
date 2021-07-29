import cv2
import pytesseract as pt
import os

pt.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


class Image:
    text: str

    @staticmethod
    def import_img(image_path: str):
        print("importing image")
        img = cv2.imread(image_path)
        cv2.imshow("image", img)
        cv2.waitKey(0)
        return img

    @staticmethod
    def read_img(img: str):
        text = pt.image_to_string(img, config="-l eng --dpi 700 -c tessedit_write_images=true")
        print(text)
        return text


