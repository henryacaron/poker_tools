from PIL import Image, ImageGrab 
import numpy as np
import cv2
import sys
sys.path.insert(1, './model')
import svm_model


from win32api import GetSystemMetrics
sys.path.append('C:\\Program Files\\Tesseract-OCR\\tesseract.exe')
import pytesseract
from matplotlib import pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\Tesseract-OCR\\tesseract'
# import time, math
from pprint import pprint

def num_cards():
    scr_w = GetSystemMetrics(0)
    scr_h = GetSystemMetrics(1)
    # printscreen = np.array(Image.open("./images/full.png")) 
    printscreen = np.array(ImageGrab.grab(bbox = (scr_w/2, 0, scr_w, scr_h)))
    return len(get_cards(printscreen))
    
def find_cards(estimator):
    scr_w = GetSystemMetrics(0)
    scr_h = GetSystemMetrics(1)
    # printscreen = np.array(Image.open("./images/full.png")) 
    printscreen = np.array(ImageGrab.grab(bbox = (scr_w/2, 0, scr_w, scr_h)))

    gray = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
    color_cards = get_cards(printscreen)
    bw_cards = get_cards(thresh)
    card_list = list()
    for i in range(len(color_cards)):
        bw_card = get_rank(bw_cards[i])
        if np.mean(bw_card) > 10:
            # rank = input("rank?")            
            rank = svm_model.predict(estimator,bw_card)
            card_list.append(to_string(rank[0]) + get_suit(color_cards[i]))
    print(card_list)
    return card_list
    
    # while(True):
    #     printscreen = ImageGrab.grab(bbox = (scr_w/2, 0, scr_w, scr_h)) 
    #     gray = cv2.cvtColor(np.array(printscreen), cv2.COLOR_BGR2GRAY)
    #     ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    
    #     cv2.imshow('window', thresh)
    #     if cv2.waitKey(25) & 0xFF == ord('q'):
    #         cv2.destroyAllWindows()
    #         break

def to_string(rank):
    if rank == 10:
        return 'T'
    if rank == 11:
        return 'J'
    if rank == 12:
        return 'Q'
    if rank == 13:
        return 'K'
    if rank == 14:
        return 'A'
    else: return str(rank)
def get_suit(card):
    boundaries = [
    	["h", [200, 0, 0], [240, 20, 20]], #hearts
    	["s", [0, 0, 0], [20, 20, 20]], #spades
    	["c", [0, 137, 45], [20, 167, 65]], #diamonds
    	["d", [0, 125, 195], [20, 155, 235]] #clubs
    ]
    suit = None
    pixel = card[32, 15]
    for i in range(len(boundaries)):
        bang = 0
        for j in range(0,3):
            if pixel[j] >= boundaries[i][1][j] and pixel[j] <= boundaries[i][2][j]:
                bang+=1
        if bang == 3: 
            suit = boundaries[i][0]
            break
    return suit
    
def get_rank(image):
    return image[:18, :].flatten()

def get_cards(image):
    card = list()
    
    card.append(image[452:496, 307:337])
    card.append(image[452:496, 342:372])
    
    dim = (30,44)

    card.append(cv2.resize(image[344:408, 208:252], dim, interpolation = cv2.INTER_AREA))
    card.append(cv2.resize(image[344:408, 263:307], dim, interpolation = cv2.INTER_AREA))
    card.append(cv2.resize(image[344:408, 318:362], dim, interpolation = cv2.INTER_AREA))
    card.append(cv2.resize(image[344:408, 373:417], dim, interpolation = cv2.INTER_AREA))
    card.append(cv2.resize(image[344:408, 428:472], dim, interpolation = cv2.INTER_AREA))
    return card

def get_pot(image): 
    image = image[288:340, 281:401]
    string = pytesseract.image_to_string(image).split()
    return int(string[2])

    cv2.waitKey(0)
if __name__ == "__main__":
    find_cards()