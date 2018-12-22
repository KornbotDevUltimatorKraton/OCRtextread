try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pyttsx 
import regex # Regular Expression
import gtts 
engine = pyttsx.init()
# If you don't have tesseract executable in your PATH, include the following:

# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open('hundred.png')))
engine.say(pytesseract.image_to_string(Image.open('hundred.png')))
engine.runAndWait() 
