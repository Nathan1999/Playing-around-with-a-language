from tkinter import * 


class Application(frame):
  def __init__(self, master):
    Frame.__init__(self, master)
    self.grid()
    self.create_widgets()
  
  def create_widgets(self):
    self.bollocks = Button(self, text = "bollocks")
    self.bolocks.grid()
    
root = Tk()
root.title = "buttons"
root.geometry= ("200x500")

app=Application(root)
root.mainloop()
