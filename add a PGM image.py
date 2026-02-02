import pyimg
a=0
b=100
c=255
img=pyimg.get.PGM_Image(28,8)
pxlist=[[a,b,a,b,a,b,a,b,c,c,c,b,a,b,a,b,a,c,c,c,a,b,c,c,c,c,a,b],
        [b,c,c,c,c,c,c,a,c,c,b,c,c,c,c,c,c,a,c,c,b,c,a,c,c,b,c,a],
        [a,c,c,c,c,c,c,b,c,c,a,c,c,c,c,c,c,c,c,c,a,c,c,b,a,c,c,b],
        [b,a,b,a,b,a,b,a,c,c,b,c,c,c,c,c,c,c,c,c,b,c,c,c,c,c,c,a],
        [a,c,c,c,c,c,c,c,c,c,a,c,c,c,a,b,a,c,c,c,a,c,c,c,c,c,c,b],
        [b,c,c,c,c,c,c,c,c,c,b,c,c,c,c,c,c,a,c,c,b,c,c,c,c,c,c,a],
        [a,c,c,c,c,c,c,c,c,c,a,c,c,c,c,c,c,b,c,c,a,c,c,c,c,c,c,b],
        [b,c,c,c,c,c,c,c,c,c,c,a,b,a,b,a,b,c,c,c,b,c,c,c,c,c,c,a]]
img.all_px(pxlist)
img.preview(400,300,300,80)