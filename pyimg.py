import tkinter as tk
import os
try:
    from PIL import Image,ImageTk
except ImportError:
    try:
        print('Installing the dependency library, please wait.')
        os.system('pip install pillow')
        from PIL import Image, ImageTk
    except ImportError:
        raise Exception('The installation of Pillow dependency library failed. Please manually install Pillow dependency library.')
class get:
    class PBM_Image:
        def __init__(self,width,height):
            self.xpxnum=1
            self.ypxnum=1
            self.Width=abs(width)
            self.Height=abs(height)
            self.Image=f'P1\n{str(self.Width)} {str(self.Height)}\n'
        def ImageValue(self):
            return self.Image
        def add_px(self,value):
            if value==0 or value==1:
                if self.xpxnum<self.Width and self.ypxnum<=self.Height:
                    self.xpxnum+=1
                    self.Image+=str(value)+' '
                elif self.ypxnum<=self.Height:
                    self.xpxnum=1
                    self.ypxnum+=1
                    self.Image+=str(value)+'\n'
        def all_px(self,value):
            for y in value:
                for x in y:
                    self.add_px(x)
        def save(self,filename):
            FileName=filename
            if not FileName.endswith('.pbm'):
                FileName+='.pbm'
            with open(FileName,'w') as f:
                f.write(self.Image)
        def clean(self):
            self.xpxnum=1
            self.ypxnum=1
            self.Image=f'P1\n{self.Width} {self.Height}\n'
        def preview(self,windowwidth,windowheight,imgwidth,imgheight):
            window=tk.Tk()
            window.title('PBM Preview')
            window.geometry(f'{windowwidth}x{windowheight}')
            window.resizable(False,False)
            with open('preview.pbm','w') as f:
                f.write(self.Image)
            try:
                pil_img=Image.open('preview.pbm')
                pil_img=pil_img.resize((imgwidth,imgheight),0)
                tk_img=ImageTk.PhotoImage(pil_img)
                label_img=tk.Label(window,image=tk_img)
                label_img.place(x=windowwidth/2-imgwidth/2,y=windowheight/2-imgheight/2)
                window.mainloop()
            finally:
                os.remove('preview.pbm')
    class PGM_Image:
        def __init__(self,width,height,maxvalue=255):
            self.xpxnum=1
            self.ypxnum=1
            self.Width=abs(width)
            self.Height=abs(height)
            self.MaxValue=maxvalue
            self.Image=f'P2\n{self.Width} {self.Height}\n{self.MaxValue}\n'
        def ImageValue(self):
            return self.Image
        def add_px(self,value):
            if value<=self.MaxValue:
                if self.xpxnum<self.Width and self.ypxnum<=self.Height:
                    self.xpxnum+=1
                    self.Image+=str(value)+' '
                elif self.ypxnum<=self.Height:
                    self.xpxnum=1
                    self.ypxnum+=1
                    self.Image+=str(value)+'\n'
        def all_px(self,value):
            for y in value:
                for x in y:
                    self.add_px(x)
        def clean(self):
            self.xpxnum=1
            self.ypxnum=1
            self.Image=f'P2\n{self.Width} {self.Height}\n{self.MaxValue}\n'
        def save(self,filename):
            FileName=filename
            if not FileName.endswith('.pgm'):
                FileName+='.pgm'
            with open(FileName,'w') as f:
                f.write(self.Image)
        def preview(self,windowwidth,windowheight,imgwidth,imgheight):
            window=tk.Tk()
            window.title('PGM Preview')
            window.geometry(f'{windowwidth}x{windowheight}')
            window.resizable(False,False)
            with open('preview.pgm','w') as f:
                f.write(self.Image)
            try:
                pil_img=Image.open('preview.pgm')
                pil_img=pil_img.resize((imgwidth,imgheight),0)
                tk_img=ImageTk.PhotoImage(pil_img)
                label_img=tk.Label(window,image=tk_img)
                label_img.place(x=windowwidth/2-imgwidth/2,y=windowheight/2-imgheight/2)
                window.mainloop()
            finally:
                os.remove('preview.pgm')
    class PPM_Image:
        def __init__(self,width,height,maxvalue=255):
            self.xpxnum=1
            self.ypxnum=1
            self.Width=abs(width)
            self.Height=abs(height)
            self.MaxValue=maxvalue
            self.Image=f'P3\n{self.Width} {self.Height}\n{self.MaxValue}\n'
        def ImageValue(self):
            return self.Image
        def add_px(self,value):
            if value<=self.MaxValue:
                if self.xpxnum<self.Width and self.ypxnum<=self.Height:
                    self.xpxnum+=1
                    self.Image+=str(value[0])+' '
                    self.Image+=str(value[1])+' '
                    self.Image+=str(value[2])+' '
                elif self.ypxnum<=self.Height:
                    self.xpxnum=1
                    self.ypxnum+=1
                    self.Image+=str(value[0])+' '
                    self.Image+=str(value[1])+' '
                    self.Image+=str(value[2])+'\n'
        def all_px(self,value):
            for y in value:
                for x in y:
                    self.add_px(x)
        def clean(self):
            self.xpxnum=1
            self.ypxnum=1
            self.Image=f'P3\n{self.Width} {self.Height}\n{self.MaxValue}\n'
        def save(self,filename):
            FileName=filename
            if not FileName.endswith('.ppm'):
                FileName+='.ppm'
            with open(FileName,'w') as f:
                f.write(self.Image)
        def preview(self,windowwidth,windowheight,imgwidth,imgheight):
            window=tk.Tk()
            window.title('PPM Preview')
            window.geometry(f'{windowwidth}x{windowheight}')
            window.resizable(False,False)
            with open('preview.ppm','w') as f:
                f.write(self.Image)
            try:
                pil_img=Image.open('preview.ppm')
                pil_img=pil_img.resize((imgwidth,imgheight),0)
                tk_img=ImageTk.PhotoImage(pil_img)
                label_img=tk.Label(window,image=tk_img)
                label_img.place(x=windowwidth/2-imgwidth/2,y=windowheight/2-imgheight/2)
                window.mainloop()
            finally:
                os.remove('preview.ppm')