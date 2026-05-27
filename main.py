from qhit import *
import qrcode
import os

tbl = {
	(0, 0, 0, 0): '\u2800',
	(0, 0, 0, 1): '\u2597',
	(0, 0, 1, 0): '\u2596',
	(0, 0, 1, 1): '\u2584',
	(0, 1, 0, 0): '\u259D',
	(0, 1, 0, 1): '\u2590',
	(0, 1, 1, 0): '\u259E',
	(0, 1, 1, 1): '\u259F',
	(1, 0, 0, 0): '\u2598',
	(1, 0, 0, 1): '\u259A',
	(1, 0, 1, 0): '\u258C',
	(1, 0, 1, 1): '\u2599',
	(1, 1, 0, 0): '\u2580',
	(1, 1, 0, 1): '\u259C',
	(1, 1, 1, 0): '\u259B',
	(1, 1, 1, 1): '\u2588'
}
data = input('DATA >> ')

mode = 3
qr = qrcode.QRCode(border=3)
qr.add_data(data)
qr.make(fit=True)

img = qrcode.make(data)
img.save("qr.png")

os.system('cls')

qrx = qr.get_matrix()
if mode in [2, 3]:
	for i in qrx:
		if mode == 3:
			x = ''
			for n, j in enumerate(i):
				x += '\u2800' if j else '\u2588'
				try:
					x += {
						(True, True): '\u2800',
						(True, False): '\u2590',
						(False, True): '\u258C',
						(False, False): '\u2588'
					}[(j, i[n+1])]
				except IndexError: pass
			print(x)
		else:
			print(''.join(['\u2800' if j else '\u2588' for j in i]))
elif mode == 0:
	if len(qrx) % 2 != 0:
		qrx.append([True]*len(qrx[-1]))
	for n, i in enumerate(qrx):
		if len(i) % 2 != 0:
			qrx[n].append(True)
	
# input()