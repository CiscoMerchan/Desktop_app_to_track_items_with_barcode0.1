"""
THE PURPOSE OF THIS PAGE IS TO BE ABLE TO SEACH IN THE DB "SCANNED" AND YIELD THE OUTPUT IN A DATA TABLE
ACCORDING TO THE INPUT TYPED IN THE ENTRIES (AS WELL THE POSSIBILITY TO PRINTED ON PDF).
"""
# import barcode
# from barcode.writer import ImageWriter
# # import pillow
# from datetime import datetime
# from fpdf import FPDF
# import pandas as pd
from tkinter import *
#####---------- This Search page reads the DB from the scanner page -----------------------#####
"""Label Fonts"""
LABEL_TITLE_FONT = ('Arial', 20, "bold")
LABEL_FONT = ('Arial', 15)
INSERT_FONT = ("Arial", 13, 'italic')

"""Colors"""
BUTTON_COLOR = "#5EAAA8"
LETTER_COLOR = "#056676"
BG_COLOR = "#F9F3DF"
ENTRY_FRAME_COLOR = "#A3D2CA"
INSERT_COLOR = "#CCD1E4"


class Search:

    def __init__(self, window):

        self.window = window
        self.window.title("        Search Barcode  ")
        self.window.geometry("1200x650")
        self.window.config(bg=BG_COLOR)





        """------------------PAGE 3 "Search Label------------------------------------------------------"""
    # setting_page.config(bg=BG_COLOR)
    # setting_page_title = Label(search_page, text="Search Label", font=LABEL_TITLE_FONT,
    #                                 bg=BG_COLOR, fg=LETTER_COLOR)
    # setting_page_title.grid(row=1, column=1, padx=5, pady=(15,20), sticky="n")

        """Labels"""
        #by Name

        by_name = Label(self.window, text="By Name:", font=LABEL_FONT, justify="left",
                        fg=LETTER_COLOR, bg=BG_COLOR)
        by_name.grid(row=3, column=0, pady=10)
        #by Order
        by_order = Label(self.window, text="By Order N.:", font=LABEL_FONT, justify="left",
                         fg=LETTER_COLOR, bg=BG_COLOR)
        by_order.grid(row=4, column=0, pady=10)
        #by Barcode
        by_barcode = Label(self.window, text="By Barcode N.:", font=LABEL_FONT, justify="left",
                           fg=LETTER_COLOR, bg=BG_COLOR)
        by_barcode.grid(row=5, column=0, pady=10)
        #by Station
        by_station= Label(self.window, text="By Station:", font=LABEL_FONT, justify="left",
                          fg=LETTER_COLOR, bg=BG_COLOR)
        by_station.grid(row=3, column=2, pady=10)
        #by Date from
        by_datefrom = Label(self.window, text="By Date from :", font=LABEL_FONT, justify="left",
                            fg=LETTER_COLOR, bg=BG_COLOR)
        by_datefrom.grid(row=4, column=2, pady=10)
        #by Date to
        by_dateto = Label(self.window, text="By Date to:", font=LABEL_FONT, justify="left",
                          fg=LETTER_COLOR, bg=BG_COLOR)
        by_dateto.grid(row=4, column=4, pady=10)
        #by Time from
        by_timefrom = Label(self.window, text="By Time from:", font=LABEL_FONT, justify="left",
                            fg=LETTER_COLOR, bg=BG_COLOR)
        by_timefrom.grid(row=5, column=4, pady=10)
        #by Time to
        by_timeto = Label(self.window, text="By Time to:", font=LABEL_FONT, justify="left",
                          fg=LETTER_COLOR, bg=BG_COLOR)
        by_timeto.grid(row=5, column=2, pady=10)

        """Entries"""
        #By Name
        name_search_entry = Entry(self.window, fg="grey", font=LABEL_FONT,
                                  bg="white", highlightthickness=2)
        # name_search_entry.insert(0, "Full name", font=INSERT_FONT, fg=INSERT_COLOR)
        name_search_entry.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        name_search_entry.grid(row=3, column=1)
        #by Order:
        order_search_entry = Entry(self.window, fg="black", font=LABEL_FONT, width=10,
                                   bg="white", highlightthickness=2)
        order_search_entry.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        order_search_entry.grid(row=4, column=1)
        #By Barcode
        barcode_search_entry = Entry(self.window, fg=LETTER_COLOR, font=LABEL_FONT, width=15,
                                     bg="white", highlightthickness=2)
        barcode_search_entry.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        barcode_search_entry.grid(row=5, column=1)
        #By Station:
        station_search_entry = Entry(self.window, fg=LETTER_COLOR, font=LABEL_FONT, width=20,
                                     bg="white", highlightthickness=2)
        station_search_entry.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        station_search_entry.grid(row=3, column=3)
        #By Date from
        datefrom_search_entry = Entry(self.window, fg=LETTER_COLOR, font=LABEL_FONT, width=10,
                                      bg="white", highlightthickness=2)
        datefrom_search_entry.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        datefrom_search_entry.grid(row=4, column=3)
        #By Date to
        dateto_search_entry = Entry(self.window, fg=LETTER_COLOR, font=LABEL_FONT, width=10,
                                    bg="white", highlightthickness=2)
        dateto_search_entry.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        dateto_search_entry.grid(row=4, column=5)
        #by Time from:
        timefrom_search_entry = Entry(self.window, fg=LETTER_COLOR, font=LABEL_FONT, width=10,
                                      bg="white", highlightthickness=2)
        timefrom_search_entry.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        timefrom_search_entry.grid(row=5, column=3, )
        #by Time to:
        timeto_search_entry = Entry(self.window, fg=LETTER_COLOR, font=LABEL_FONT, width=10,
                                    bg="white", highlightthickness=2)
        timeto_search_entry.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        timeto_search_entry.grid(row=5, column=5)

        """Buttons"""
        #Search button
        button_search = Button(self.window, text="Search", font=LABEL_FONT, bg=BUTTON_COLOR, fg=LETTER_COLOR,
                               activebackground="grey")
        button_search.grid(row=3, column=5, pady=10)
        #Clear button
        clear_button_search = Button(self.window, text="Clear", font=LABEL_FONT, bg=BUTTON_COLOR, fg=LETTER_COLOR,
                                     activebackground="grey")
        clear_button_search.grid(sticky="sw")
        #Print button
        print_button_search = Button(self.window, text="Print", font=LABEL_FONT, bg=BUTTON_COLOR, fg=LETTER_COLOR,
                                     activebackground="grey")
        print_button_search.grid(sticky="se")
        # Menu button
        menu_button = Button(self.window, text="🔙Menu", font=LABEL_FONT, bg=BG_COLOR, fg=LETTER_COLOR,
                             activebackground="white", command=lambda: (self.window.destroy()))
        menu_button.grid(row=0, column=0)

def page():
    window = Tk()
    Search(window)
    window.mainloop()


if __name__ == '__main__':
    page()



