#!/usr/bin/python3
import sys,os
import cv2
import yaml

fpath = sys.argv[1]
fname, fext = os.path.splitext(fpath)
assert '.yaml'==fext, 'file extension must be yaml'

with open(fpath) as f:
    m = yaml.load(f, Loader=yaml.FullLoader)

mapimg = m['image']
mapres = m['resolution']
orig_x,orig_y,_ = m['origin']

im = cv2.imread(mapimg)

points = []

def click(event, x, y, flags, param):
	global points
	if event == cv2.EVENT_LBUTTONUP:
		points.append((x, y))

cv2.imshow('map', im)
cv2.setMouseCallback("map", click)
k = cv2.waitKey(0)
with open(fname+'.txt', 'w') as f:
    f.write('\n'.join([str(p[0]*mapres + orig_x)+','+str(-p[1]*mapres - orig_y) for p in points]))