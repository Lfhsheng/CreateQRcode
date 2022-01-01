import qrcode
from tkinter import *
import tkinter.messagebox as messagebox
window = Tk()
window.title('生成二维码 By 泠风寒声')
width = 300
heigh = 150
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
window.resizable(0, 0)
qr = qrcode.QRCode(version=1,error_correction =
    qrcode.constants.ERROR_CORRECT_M,
    box_size=10, border=4,)
def generate():
    img = qrcode.make(data = data)
    img.show()
def closeWindow():
    askback = messagebox.askyesno('提示', '真的要关闭这个程序吗？')
    if askback == True:
        window.destroy()
ft = ('等线Light', 10)
data = Entry(window, font = ft)
data.place(width = 150, heigh = 25, x = 75, y = 0)
button = Button(window, text = '生成二维码', font = ft,
                command = generate, height = 5, width = 10)
button.place(x = 100, y = 40)
Label(window,text = 'By 泠风寒声', fg = 'red', font = ft).place(x = 225, y = 120)
window.protocol('WM_DELETE_WINDOW', closeWindow)
window.mainloop()