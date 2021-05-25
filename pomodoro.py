import tkinter as tk
from tkinter import StringVar, Text, font
import time
from tkinter.constants import FALSE, TRUE

HEIGHT = 400
WIDTH = 400
WORK = 1500
REST = 300
LONG_REST = 900


class Countdown():
  '''Frame that contains the elements for a Pomodoro timer (label with the time remaining per session, start button, pause button, reset button, and an entry for the user to input what task they are performing'''
  def __init__(self):
      self.counter = 4
      self.sec_left = 0
      self.isWork = TRUE
      self.continue_count = FALSE
      self.create_widgets()
      self.display_widgets()
      
  def create_widgets(self):
    self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    self.background_img = tk.PhotoImage(file='time.png')
    self.background_label = tk.Label(root, image=self.background_img)
    self.frame = tk.Frame(root, bg='#ffffff', bd=5)
    v = StringVar(root, value='Set task name')
    self.entry = tk.Entry(self.frame, font=('Verdana', 15), textvariable=v, justify='center')
    self.count_label = tk.Label(root, text='Count Until Long Break!',justify='center', font=('Verdana', 15))
    self.my_label = tk.Label(root, text='Press start', font=('Verdana', 30))
    self.button1 = tk.Button(root, text='▶', font=('Verdana', 20), command=lambda: self.start())
    self.button2 = tk.Button(root, text='⏸', font=('Verdana', 20), command=lambda: self.stop_timer())
    self.button3 = tk.Button(root, text='Reset', font=('Verdana', 20), command=lambda: self.reset_timer())
    
  def display_widgets(self):
    self.canvas.pack()
    self.background_label.place(relwidth=1, relheight=1)
    self.frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')
    self.entry.place(relwidth=1, relheight=1)
    self.count_label.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.05)
    self.my_label.place(relwidth=0.8, relheight=0.35, relx=0.1, rely=0.35)
    self.button1.place(relwidth=0.3, relheight=0.1, relx=0.05, rely=0.8)
    self.button2.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.8)
    self.button3.place(relwidth=0.3, relheight=0.1, relx=0.65, rely=0.8)
    
  def countdown(self):
    min, sec = divmod(self.sec_left, 60)
    timer = '{:02d}:{:02d}'.format(min, sec)
    self.my_label['text'] = timer
    if self.sec_left and self.continue_count:
      self.sec_left -= 1
      self.continue_count = root.after(1000, self.countdown)
    elif self.sec_left == 0:
      if self.isWork and self.counter != 0:
        self.counter -= 1
      elif not self.isWork and self.counter == 0:
        self.counter = 4
      self.isWork = not self.isWork
      self.start()

  def start(self):
    self.count_label['text'] = 'Count Until Long Break: ' + str(self.counter)
    if self.isWork and self.sec_left == 0 :
      self.sec_left = WORK
    elif not self.isWork and self.counter == 0 and self.sec_left == 0:
      self.sec_left = LONG_REST
    elif not self.isWork and self.sec_left == 0:
      self.sec_left = REST
    self.start_timer()

  def start_timer(self):
    self.stop_timer()
    self.continue_count = TRUE
    self.countdown()

  def stop_timer(self):
    if self.continue_count:
      root.after_cancel(self.continue_count)
      self.continue_count = FALSE
    
  def reset_timer(self):
    self.counter = 4
    self.isWork = TRUE
    self.sec_left = 0
    self.start()

#########################

if __name__ == '__main__':
  root = tk.Tk()
  countdown = Countdown()
  root.mainloop()
