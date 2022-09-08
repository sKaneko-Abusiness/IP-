#【準備物==================================】
import socket


#【ターミナル文字色強調設定=====================】
RED = '\033[31m'
END = '\033[0m'

#【1,IPアドレスを取得する=====================】
ip = socket.gethostbyname(socket.gethostname())
print("現在接続中のIPアドレスは『"+RED+ip+END+"』になります")


#【2,SSIDを取得する=========================】



#【3,取得情報を画面にポップアップ表示する】
import tkinter as tk

root = tk.Tk()
root.geometry('500x300')

label = tk.Label(root, text='テキスト')
label.pack()

root.mainloop()
