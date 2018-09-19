C = input('請輸入攝氏溫度:')

if C != '':
	F = (float(C) * (9 / 5)) + 32
	print('華氏溫度=', F)

if C == '':
	print('你尚未輸入攝氏溫度喔!')