#!/usr/bin/python
# Simple Python/Tkinter app to run a stopwatch in the right-top corner.
# Control:
# Left click or Enter: Start/Restart.
# Right click or Escape: Pause/Unpause.
# Icon is optional.
# Anton Chivchalov, https://github.com/antorix

import time
import tkinter as tk
class App(tk.Frame):    
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.geometry('130x80+%d+%d' % (self.master.winfo_screenwidth()-130, 0))
        try: self.master.iconbitmap("icon.ico")
        except: pass
        self.master.title("Stopwatch")      
        self.button=tk.Button(self.master, font="{Arial} 14", command=self.run)
        self.button.pack(fill="both", expand=True, padx=3, pady=3)
        self.master.bind("<Return>", self.run)
        self.master.bind("<Escape>", self.pause)
        self.master.bind("<3>", self.pause)
        self.run()
    def run(self, event=None):        
        self.delta=self.freeze=0
        self.frozen=[]        
        self.paused=False
        self.start=time.time()            
        self.refresh()
    def refresh(self):
        if self.paused==False:        
            self.button["relief"]="flat"
            self.cur = time.time()+sum(self.frozen)
            hours, rem = divmod(self.cur-self.start, 3600)
            minutes, seconds = divmod(rem, 60)        
            self.button["text"]="{:0>2}:{:0>2}:{:04.1f}".format(int(hours),int(minutes),seconds)
        else:
            self.button["relief"]="ridge"
            self.delta=(self.cur-self.freeze)            
            self.cur = time.time()
            self.frozen[len(self.frozen)-1]=self.cur-self.start-self.delta           
        self.cycle=self.after(100, self.refresh)
    def pause(self, event=None):
        if self.paused==False:
            self.paused=True
            self.freeze=time.time()
            self.frozen.append(0)
        else:
            self.paused=False        
            self.button["relief"]="flat"
            self.start=time.time()            
App().mainloop()
