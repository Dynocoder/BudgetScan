import requests
import json


def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'isTable': True,
               'scale': True,
               'OCREngine': 2
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'isTable': True,
               'scale': True,
               'OCREngine': 5
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()
# test_url = ocr_space_url(url='http://i.imgur.com/31d5L5y.jpg')


# Use examples:
# def receiptScan(filepath):

filename = "test\test1.jpg"

# Pass the file to the ocr function, which returns a json object containing the parsed text.
test_file = ocr_space_file(filename=filepath, api_key='K87071661088957')

# Converting the returned strigified json object to workable json.
converted = json.loads(test_file)

# Testing outputs
print(converted)
with open("result.json", "w") as resultFile:
    resultFile.write(test_file)

# the actual scanned text is placed inside the 'parsedresults' property of the json object.
parsedText = converted['ParsedResults'][0]['ParsedText']

print(parsedText)

# Separating the whole text into lines as separated by '\n' in the response.
parsedTextArray = parsedText.split('\n')

print(parsedTextArray)

# Looping through the array of lines.
for line in parsedTextArray:
    # Looking for the text "TOTAL" in the lines.
    if line.startswith("TOTAL"):
        # Splitting the lines by '\t' (tab)
        price = line.split('\t')
        print(line)
        print(price)
        # return price[1]

