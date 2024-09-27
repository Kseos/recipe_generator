'''
Recipe application with openAI

Dietery restrictions:
gluten free
vegan
vegetarian
sugar free
dairy free


ingrediants is a list in which you choose what ingrediants to add

entry + button
and a list of boxex with ingrediants above that

'''

import openai
from customtkinter import *

set_appearance_mode('dark')
mode = 'dark'

class App():
    def __init__(self):
        self.root = CTk()
        self.center_window(self.root)
        self.root.title('Your new recipe book')   
        self.root.iconbitmap('images\icon2.ico')

        # create a small window with 'Hello', a tutorial and asking a name

        self.title_label = CTkLabel(self.root, text = 'Recipe book', font = ('georgia', 24))
        self.title_label.pack(padx= 10, pady=(30, 20))

        self.frame = CTkFrame(self.root)
        self.frame.pack(padx = 100, fill = 'x')

        self.dietery_preferences()
        self.type_of_food()
   
        self.create_button() 
        
             
        self.root.mainloop()
        return

    def dietery_preferences(self):
        self.preferences_frame = CTkFrame(self.frame)
        self.preferences_frame.pack(padx = 100, pady = (10, 10), fill = 'both')

        self.preferences_label = CTkLabel(self.preferences_frame, text = 'Dietery preferences', font= ('georgia', 20))
        self.preferences_label.pack(pady = (10, 5))

        self.top_frame = CTkFrame(self.preferences_frame)
        self.top_frame.pack(padx=10,pady=5)
        self.bottom_frame = CTkFrame(self.preferences_frame)
        self.bottom_frame.pack(padx=10,pady=(5,10))

        self.preferences_dairy = CTkCheckBox(self.top_frame, checkbox_width = 20, checkbox_height=20, border_width=1.2,
                                            corner_radius = 6, text = 'Dairy free', font = ('georgia', 16))
        self.preferences_dairy.pack(side=LEFT, padx= (15,13),pady=5)

        self.preferences_vegan = CTkCheckBox(self.top_frame, checkbox_width = 20, checkbox_height=20, border_width=1.2,
                                            corner_radius = 6, text = 'Vegan', font = ('georgia', 16))
        self.preferences_vegan.pack(side=LEFT, padx= (5,15), pady=5)

        self.preferences_gluten = CTkCheckBox(self.bottom_frame, checkbox_width = 20, checkbox_height=20, border_width=1.2,
                                            corner_radius = 6, text = 'Gluten free', font = ('georgia', 16))
        self.preferences_gluten.pack(side=LEFT, padx=(15,5), pady=5)
        
        self.preferences_sugar = CTkCheckBox(self.bottom_frame, checkbox_width = 20, checkbox_height=20, border_width=1.2,
                                            corner_radius = 6, text = 'Sugar free', font = ('georgia', 16))
        self.preferences_sugar.pack(side=LEFT, padx=(5,15), pady=5)


    def type_of_food(self):
        self.type_frame = CTkFrame(self.frame)
        self.type_frame.pack(padx = 100, pady = (10, 10), fill = 'both')

        self.type_label = CTkLabel(self.type_frame, text = 'Type of meal', font= ('georgia', 20))
        self.type_label.pack(pady = (10, 5))

        self.top_frame = CTkFrame(self.type_frame)
        self.top_frame.pack(padx=10,pady=5)
        self.bottom_frame = CTkFrame(self.type_frame)
        self.bottom_frame.pack(padx=10,pady=(5,10))

        self.breakfast = 'Breakfast'
        self.lunch = 'Lunch'
        self.dinner = 'Dinner'
        self.snack = 'Snack'

        self.type_of_food = StringVar(value=self.breakfast)

        self.type_breakfast = CTkRadioButton(self.top_frame, radiobutton_height=16, radiobutton_width=16, border_width_unchecked=1.2, border_width_checked=4,
                                            text = self.breakfast, font = ('georgia', 16), value=self.breakfast, variable = self.type_of_food)
        self.type_breakfast.pack(side=LEFT, padx= (15,5),pady=5)

        self.type_lunch = CTkRadioButton(self.top_frame, radiobutton_width= 16, radiobutton_height=16, border_width_unchecked=1.2, border_width_checked=4,
                                            text = self.lunch, font = ('georgia', 16), value = self.lunch, variable = self.type_of_food)
        self.type_lunch.pack(side=LEFT, padx= (5,15), pady=5)

        self.type_dinner = CTkRadioButton(self.bottom_frame, radiobutton_width= 16, radiobutton_height=16, border_width_unchecked=1.2, border_width_checked=4,
                                            text = self.dinner, font = ('georgia', 16), value = self.dinner, variable = self.type_of_food)
        self.type_dinner.pack(side=LEFT, padx=(15,5), pady=5)
        
        self.type_snack = CTkRadioButton(self.bottom_frame, radiobutton_width= 16, radiobutton_height=16, border_width_unchecked=1.2, border_width_checked=4,
                                            text = self.snack, font = ('georgia', 16), value = self.snack, variable = self.type_of_food)
        self.type_snack.pack(side=LEFT, padx=(5,15), pady=5)

             
    def create_button(self):
        self.button = CTkButton(self.root, text = 'Find recipes', command = self.click_handler,
                           font=('georgia', 16), corner_radius = 9, fg_color='#3E78B2', 
                           hover_color= '#4A525A', text_color='#000000')
        self.button.pack(padx=10,pady=10)
        self.root.bind('<Return>', lambda event: self.click_handler())
    
    def center_window(self, window, width = 750, height = 750):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
    
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        window.geometry('%dx%d+%d+%d' %(width, height, x, y))

    def click_handler(self):
        print('The button was pressed')
               

if __name__ == '__main__':
    App()