from tkinter import *
import speedtest


def getSpeed() :
    sp = speedtest.Speedtest()
    sp.get_servers()
    download_speed = str(round(sp.download()/(10**6),3)) + "Mbps"
    upload_speed = str(round(sp.upload()/(10**6),3)) + "Mbps"
    lab_download.config(text = download_speed)
    lab_upload.config(text = upload_speed)





sp = Tk()
sp.title('Internet Speed')
sp.geometry('500x650')
sp.config(bg = 'Black')
#Title
lab = Label(sp,text = 'Internet Speed Test',font=('Arial',30,'bold'),bg = 'Black',fg = 'white')
lab.place(x = 60, y = 50, height = 50, width = 380)
#Downloading Speed
lab = Label(sp,text = 'Download Speed',font=('Arial',25,'bold'),bg = 'Black',fg = 'white')
lab.place(x = 60, y = 150, height = 50, width = 380)
lab_download = Label(sp,text = 'Internet Speed Test',font=('Arial',18,'bold'))
lab_download.place(x = 60, y = 225,height=30,width=380)
#Uploading Speed
lab = Label(sp,text = 'Upload Speed',font=('Arial',25,'bold'),bg = 'Black',fg = 'white')
lab.place(x = 60, y = 300, height = 50, width = 380)
lab_upload = Label(sp,text = 'Internet Speed Test',font=('Arial',18,'bold'))
lab_upload.place(x = 60, y = 375, height = 30, width = 380)
#button for current speed
button = Button(sp,text = 'Check Speed',font = ('Arial',20,'bold'),relief=RAISED,bg='red',command=getSpeed)
button.place(x = 60, y = 500,height=50,width=380)


sp.mainloop()
