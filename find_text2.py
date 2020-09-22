import cv2 
import pytesseract 

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

img = cv2.imread('E:/Summer Proj/Covid_Tracker/Code/My_Map.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18)) 
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 

print(rect_kernel)

_, contours, hierarchy,=cv2.findContours(dilation,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


im2 = img.copy() 

file = open("E:/Summer Proj/Covid_Tracker/Code/recognized.txt", "w+") 
file.write("") 
file.close() 
s=[]

for cnt in contours: 
 x, y, w, h = cv2.boundingRect(cnt) 
 rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2) 
 cropped = im2[y:y + h, x:x + w] 
 file = open("recognized.txt", "a") 
 text = pytesseract.image_to_string(cropped) 
 s.append([x,y,text])
 file.write(text) 
 file.write("\n") 
 file.close()

print(s)

#OP s=[[1265, 1927, 'LITERALLY.’'], [1070, 1927, 'HANDS.'], [858, 1927, 'IN YOUR'], [800, 1927, ''], [436, 1927, '‘YOUR SAFETY'], [1408, 1653, 'AN'], [719, 1633, 'KL'], [818, 1618, 'TN'], [308, 1588, 'LK'], [962, 1573, 'PY'], [1462, 1447, 'DEATHS:'], [860, 1402, 'AP'], [1491, 1377, 'XX'], [1322, 1377, 'CURED'], [646, 1367, 'KA'], [468, 1345, 'GA'], [1319, 1305, 'CTIVE CAS\n\nES:'], [1346, 1224, 'TOTAL CASES:'], [863, 1183, 'TS'], [595, 1084, 'MH'], [1166, 1030, 'OD'], [1049, 982, 'CT'], [1555, 893, 'TR'], [1720, 884, 'MZ'], [1333, 866, 'WB'], [787, 859, 'MP'], [1180, 833, 'JH'], [457, 824, 'GJ'], [1444, 764, 'ML'], [1801, 743, 'MN'], [1240, 710, 'BR'], [1792, 668, 'NL'], [1513, 668, 'AS'], [1021, 651, 'UP'], [534, 637, 'RJ'], [823, 529, 'DL'], [666, 529, 'HR'], [1382, 461, 'SK'], [190, 434, 'CH'], [282, 425, 'XX'], [863, 417, 'UT'], [1762, 369, 'AR'], [676, 353, 'PB'], [1269, 318, 'STATEWISE'], [777, 266, 'HP'], [1425, 232, ''], [1338, 232, ''], [1112, 232, ''], [651, 167, 'JK'], [800, 143, 'LA'], [63, 65, ''], [1765, 41, 'updates'], [1620, 41, 'latest'], [936, 41, 'follow @covid_ai_tracker for']]
