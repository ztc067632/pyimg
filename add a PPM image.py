import pyimg
img=pyimg.get.PPM_Image(28,8)
a=[255,0,0]
b=[0,255,0]
c=[0,0,255]
d=[255,255,255]
pxlist=[[a,b,c,a,b,c,a,b,d,d,a,b,c,a,b,c,a,b,d,d,a,b,d,d,d,d,a,b],
        [b,d,d,d,d,d,d,c,d,d,b,d,d,d,d,d,d,c,d,d,b,d,c,d,d,c,d,c],
        [c,d,d,d,d,d,d,a,d,d,c,d,d,d,d,d,d,a,d,d,c,d,d,a,b,d,d,a],
        [a,b,a,c,b,a,c,b,d,d,a,b,a,c,b,a,c,b,d,d,a,d,d,d,d,d,d,b],
        [b,d,d,d,d,d,d,d,d,d,b,d,d,d,d,d,d,d,d,d,b,d,d,d,d,d,d,c],
        [c,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,a],
        [a,d,d,d,d,d,d,d,d,d,a,d,d,d,d,d,d,d,d,d,a,d,d,d,d,d,d,b],
        [b,d,d,d,d,d,d,d,d,d,b,d,d,d,d,d,d,d,d,d,b,d,d,d,d,d,d,c]]
img.all_px(pxlist)
img.preview(400,300,300,80)