import pytesseract
from PIL import Image
import os
import subprocess

# 設定 tesseract 可執行檔路徑，如果你的環境中已經設定 PATH，可以省略這行
pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"

# 擷取屏幕截圖
os.system("screencapture -i tmp.png")

# 讀取截圖並識別文字
text = pytesseract.image_to_string(Image.open("tmp.png"), lang='eng')

# 將文字存到剪貼板中
process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
process.communicate(text.encode('utf-8'))

# 刪除截圖檔案
os.remove("tmp.png")

print("OCR 結果已存入剪貼板！")

