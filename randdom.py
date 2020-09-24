#使用import載入，並使用random產生隨機變數
import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 # = count + 1
	num = input('請猜一個數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('你猜錯了，你猜得比答案大')
	else:
		print('你猜錯了，你猜得比答案小')
	print('這是你猜的第', count, '次')	