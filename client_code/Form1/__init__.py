from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_1_click(self, **event_args):
    global p
    p=anvil.server.call('predict_next_word1',self.text_area.text,self.limit_text.text)
    self.rich_text_1.clear()
    self.rich_text_1.content=p
    
  

