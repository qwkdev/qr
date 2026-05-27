#!/usr/bin/env python3

import qrcode
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('data')
parser.add_argument('--small', action='store_true')
args = parser.parse_args()

qr = qrcode.QRCode(border=3)
qr.add_data(args.data)
qr.make(fit=True)

if args.small:
	qr.print_ascii(invert=True)
else:
	qrx = qr.get_matrix()
	for i in qrx:
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