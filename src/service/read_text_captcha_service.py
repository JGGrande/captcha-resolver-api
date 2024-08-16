import cv2
import re
import numpy as np
from pytesseract import pytesseract
from typing import Union

def _is_only_spaces_on_text(text: str) -> bool:
    only_spaces_pattern = re.compile(r'^\s*$')

    result = re.match(only_spaces_pattern, text)

    return bool(result)

def read_text_captcha_image_service(image_bytes: bytes) -> Union[str, None]: 
    np_arr = np.frombuffer(image_bytes, np.uint8)

    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    gry = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    (h, w) = gry.shape[:2]

    gry = cv2.resize(gry, (w*2, h*2))

    cls = cv2.morphologyEx(gry, cv2.MORPH_CLOSE, None)

    thr = cv2.threshold(cls, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(thr)

    if _is_only_spaces_on_text(text): return None

    return text