#외부library
import random #내부 라이브러리
import qrcode

url = 'https://medicine.yonsei.ac.kr/medicine/index.do'
qrcode_img = qrcode.make(url)
qrcode_img.save('yonsei.png')





