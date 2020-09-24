#使用import載入，並使用random產生隨機變數
import random
r = random.randint(1, 100)

while True:
	num = input('請猜一個數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了')
		break
	elif num > r:
		print('你猜錯了，你猜得比答案大')
	else:
		print('你猜錯了，你猜得比答案小')	