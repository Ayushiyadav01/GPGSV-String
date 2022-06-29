from tkinter import *
from  tkinter import ttk


ws  = Tk()
ws.title('GPGSV')
ws.geometry('500x250')
ws['bg'] = '#AC99F2'

game_frame = Frame(ws)
game_frame.pack()

my_game = ttk.Treeview(game_frame)

my_game['columns'] = ('player_id', 'player_name', 'player_Rank')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("player_id",anchor=CENTER, width=150)
my_game.column("player_name",anchor=CENTER,width=150)
my_game.column("player_Rank",anchor=CENTER,width=150)

my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("player_id",text="Satellite Number",anchor=CENTER)
my_game.heading("player_name",text="Elevation Angle",anchor=CENTER)
my_game.heading("player_Rank",text="Azimuth Angle",anchor=CENTER)

my_game.insert(parent='',index='end',iid=0,text='',
values=('1','Ninja','101'))
my_game.insert(parent='',index='end',iid=1,text='',
values=('2','Ranger','102'))
my_game.insert(parent='',index='end',iid=2,text='',
values=('3','Deamon','103'))
my_game.insert(parent='',index='end',iid=3,text='',
values=('4','Dragon','104'))
my_game.insert(parent='',index='end',iid=4,text='',
values=('5','CrissCross','105'))
my_game.insert(parent='',index='end',iid=5,text='',
values=('6','ZaqueriBlack','106'))

my_game.pack()

ws.mainloop()