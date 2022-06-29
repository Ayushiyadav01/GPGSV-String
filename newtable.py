from cProfile import label
from tkinter import *
from  tkinter import ttk
from time import process_time_ns
from turtle import goto
import serial

ser = serial.Serial('COM5', 4800, timeout=0)

ws  = Tk()
ws.title('GPGSV')
ws.geometry('500x250')
ws['bg'] = '#AC99F2'

game_frame = Frame(ws)
game_frame.pack()

my_game = ttk.Treeview(game_frame)

my_game['columns'] = ('Sat_No', 'Elev_Angle', 'Azim_Angle')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("Sat_No",anchor=CENTER, width=150)
my_game.column("Elev_Angle",anchor=CENTER,width=150)
my_game.column("Azim_Angle",anchor=CENTER,width=150)

my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("Sat_No",text="Satellite Number",anchor=CENTER)
my_game.heading("Elev_Angle",text="Elevation Angle",anchor=CENTER)
my_game.heading("Azim_Angle",text="Azimuth Angle",anchor=CENTER)

def data():
    while True :
        data_raw = str(ser.readline())
        data_li = list(data_raw.split(","))
        # print(data_li)
        if (data_li[0]=='b\'$GPGSV'):
            try:
                sat_no1 = data_li[4]
                elev1 = data_li[5]
                azi1 = data_li[6]
            except:
                print("data over1")

            try:
                sat_no2 = data_li[8]
                elev2 = data_li[9]
                azi2 = data_li[10]
            except:
                print("Data over2")

            try:                    
                sat_no3 = data_li[12]
                elev3 = data_li[13]
                azi3 = data_li[14]
            except:
                print("data over3")

            try:
                sat_no4 = data_li[16]
                elev4 = data_li[17]
                azi4 = data_li[18] 
            except:
                print("data over4")

            my_game.insert(parent='',index='end',text='',
            values=(sat_no1,elev1,azi1))
            my_game.insert(parent='',index='end',text='',
            values=(sat_no2,elev2,azi2))
            my_game.insert(parent='',index='end',text='',
            values=(sat_no3,elev3,azi3))
            my_game.insert(parent='',index='end',text='',
            values=(sat_no4,elev4,azi4))
           
            ws.update()
                

my_game.pack()

bu = Button(ws,text=("Start"),command=data)
bu.pack()


ws.mainloop()