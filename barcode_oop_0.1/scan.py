"""
This module is to register a barcode in a csv file either by scanning a barcode (using the computer
               camera) or type in the barcode number. The number will be store in a csv file that can be access in
               "Search Barcode Label".  For this reason is mandatory to fill the 'stage' input case to follow up the
               different stage of the transformation when the user search in "Search Barcode Label"(# At the moment
               the saved barcode is prompted on the console) .
 """
from tkinter import messagebox
from readbarcode import *
import cv2
import pyzbar.pyzbar as pyzbar
import PIL.Image
import barcode
from barcode.writer import ImageWriter
# import pillow
from datetime import datetime
# from fpdf import FPDF
import pandas as pd
from tkinter import *
from datetime import datetime

### ---------------------- The input from this page goes to DB SCANNED AND IS CONNECTED TO THE SEARCH PAGE--------###
"""DB SCANNED"""

"""Label Fonts"""
LABEL_TITLE_FONT = ('Arial', 12, "bold")
LABEL_FONT = ('Arial', 12, "bold")
SMALL_LETTER_BUTTON = ('Arial', 12)
"""Colors"""
BUTTON_COLOR = "#5EAAA8"
LETTER_COLOR = "#056676"
BG_COLOR = "#F9F3DF"
ENTRY_FRAME_COLOR = "#A3D2CA"


class Scan:

    def save(self):
        while True:
            if self.station.get() == "":
                confirmed = messagebox.showerror("Error!", 'You must select a "Station number" ')
                if confirmed:
                    break
            else:
                # return self.station.get()
        # station = self.station_n()

                """DATA FOR THE "DB" """


                """date and time"""
                dt = datetime.now()
                date = f'{dt.strftime("%m")}/{dt.strftime("%d")}/{dt.strftime("%Y")}'
                time = f'{dt.strftime("%I")}:{dt.strftime("%M")}{dt.strftime("%p")}'

                scan_data = {"Station": [f"{self.station.get()}"],
                             "Barcode": [f'{self.manual_e.get()}'],
                             "Date": [f'{date}'],
                             "Time": [f'{time}'],
                             "Observation": [f'{self.observation_e .get()}']
                             }
                print(scan_data)
                df = pd.DataFrame(scan_data)#, columns=(["Station", "Barcode", "Date", "Time", "Observation"]))
                df.to_csv("barcode_input_DataFrame.csv", mode='a', header=False)
            break
    """DEF STATION_N IS A FUNCTION TO GET THE STATION NUMBER SELECTED BY THE USER WHO IS SCANNING THE BARCODELABEL """

    # def station_n(self):
    #     print("station number")
    #     i = 0
        # while True:
        #     if self.station.get() == "":
        #         confirmed = messagebox.showerror("Error!", 'You must select a "Station number" ')
        #         if confirmed:
        #             break
        #     else:
        #         return self.station.get()

    """FUNCTION TO TAKE THE INPUT OF THE LABEL NUMBER FROM THE USER MANUALLY """

    def manual_type_barcode(self):

        dt = datetime.now()
        date = f'{dt.strftime("%m")}/{dt.strftime("%d")}/{dt.strftime("%Y")}'
        time = f'{dt.strftime("%I")}:{dt.strftime("%M")}{dt.strftime("%p")}'
        m_t_b = str(self.manual_e.get())
        confirmation = messagebox.askyesno(title='confirmation', message=f'{m_t_b}')
        if confirmation:
            with open("barcode_result.txt", mode='a') as file:
                file.write(f"mtb{m_t_b} \n")
            # return f'{m_t_b}'
        print(f'{m_t_b}')

        return m_t_b

    """THIS FUNCTION IS TO READ THE BARCODE ONCE THE USER PRESS "SCAN" BUTTON"""

    def scanbarcode(self):
        dt = datetime.now()
        date = f'{dt.strftime("%m")}/{dt.strftime("%d")}/{dt.strftime("%Y")}'
        time = f'{dt.strftime("%I")}:{dt.strftime("%M")}{dt.strftime("%p")}'
        i = 0
        vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while i < 1:
            _, f = vid.read()
            decoded = pyzbar.decode(f)
            for obj in decoded:
                bare = str(obj.data).replace("b", "")
                bar = bare.strip("'")
                print(type(bar))
                confirmation = messagebox.askyesno(title='confirmation', message=f'{bar}')
                if confirmation:
                    self.manual_e.insert(0, f"{bar}")
                    with open("barcode_result.txt", mode='a') as file:
                        file.write(f"{bar} {date} {time}\n")

                    return f'{bar}'
                print(bar)

                i += 1
            cv2.imshow('Barcode/QRCode', f)
            if cv2.waitKey(5) & 0xFF == 27:
                cv2.destroyAllWindows()
                break
            # cv2.release()

    def codebar(self):
        with open('barcode_result.txt', "r") as fp:
            bar_input = fp.readlines()[-1]
            print(bar_input)
            return bar_input

    def __init__(self, window):

        self.barcode_info = None
        self.window = window
        self.window.title("        Barcode Scanner ")
        self.window.geometry("480x450")
        self.window.config(bg=BG_COLOR)
        self.manual_barcode = LabelFrame(self.window, text="Enter barcode manually", bg=BG_COLOR,
                                         highlightbackground=ENTRY_FRAME_COLOR, fg=LETTER_COLOR,
                                         highlightcolor=ENTRY_FRAME_COLOR, padx=50, pady=20)
        self.manual_barcode.grid(row=3, column=1)
        self.observation = LabelFrame(self.window, text='Observation:\n (If necessary, make observation before "save")',
                                      bg=BG_COLOR, highlightbackground=ENTRY_FRAME_COLOR, fg=LETTER_COLOR,
                                      highlightcolor=ENTRY_FRAME_COLOR, padx=50, pady=20)
        self.observation.grid(row=5, column=1)

        # _______________________Scan Barcode Label_________________________________"""

        """Title"""
        # scanner_page.config(bg=BG_COLOR)
        # scanner_page_title = Label(self.window, text="Scan Barcode", font=LABEL_TITLE_FONT,
        #                                 bg=BG_COLOR, fg=LETTER_COLOR)
        # scanner_page_title.grid(row=1, column=1, padx=5, pady=(15,20), sticky="n")

        """Entry of the "Sation number by the user"""
        # LABEL
        station_n_label = Label(self.window, text="Station number:*", font=('Arial', 12), fg=LETTER_COLOR, bg=BG_COLOR)
        station_n_label.grid(row=1, column=1)
        # Station name/number ENTRY
        self.station = Entry(self.window, width=5, bg="white", highlightbackground=ENTRY_FRAME_COLOR,
                             fg='black', highlightcolor=ENTRY_FRAME_COLOR)
        # self.station.insert(0,"")
        self.station.place(x=298, y=5)

        """Observation box"""
        self.observation_e = Entry(self.observation, highlightthickness=2, width=30)
        # self.b = Button(self.observation, text='Save', fg=LETTER_COLOR, font=SMALL_LETTER_BUTTON, bg=BG_COLOR,
        #                 command=lambda: self.manual_type_barcode())
        # self.b.grid(row=3, column=0)
        self.observation_e.grid(row=3, rowspan=2, column=0)
        # LABEL
        # scan_label_page_observation = Label(self.window, font=LABEL_FONT,fg=LETTER_COLOR, bg=BG_COLOR,
        #                                     text='Observation:\n (If necessary, make observation before "save")')
        # scan_label_page_observation.grid(row=4, column=1, pady=10)
        # # ENTRY
        # self.scan_label_entry_observation = Entry(self.window, fg=LETTER_COLOR, font=LABEL_FONT,
        #                                           bg=BG_COLOR, highlightthickness=2)
        # self.scan_label_entry_observation.config(highlightbackground=ENTRY_FRAME_COLOR,
        #                                          highlightcolor=ENTRY_FRAME_COLOR)
        # self.scan_label_entry_observation.grid(row=5, column=1, ipady="50")

        """Buttons"""

        # Activate Scanner button
        scan_button = Button(self.window, text="Scan", font=LABEL_FONT, bg=BUTTON_COLOR, fg=LETTER_COLOR,
                             activebackground="grey", command=lambda: self.scanbarcode())

        scan_button.grid(row=2, column=1, padx=20, pady=20)

        #  IN THIS ENTRY THE SCAN NUMBER IS SHOW OR THE USER CAN TYPE THE BARCODE NUMBER#
        self.manual_e = Entry(self.manual_barcode, highlightthickness=2)

        self.b = Button(self.manual_barcode, text='Save', fg=LETTER_COLOR, font=SMALL_LETTER_BUTTON, bg=BG_COLOR,
                        command=lambda: self.manual_type_barcode())
        self.b.grid(row=4, column=0)
        self.manual_e.grid(row=3, column=0)

        # Save Button
        save_button = Button(self.window, text="Save", font=LABEL_FONT, bg=BUTTON_COLOR, fg=LETTER_COLOR,
                             activebackground="grey", command=lambda: self.save())
        save_button.grid(row=6, column=0, padx=20, pady=20)

        # Clear button
        clear_button = Button(self.window, text="Clear", font=LABEL_FONT, bg=BUTTON_COLOR, fg=LETTER_COLOR,
                              activebackground="grey")
        clear_button.grid(row=6, column=2, padx=20, pady=20)
        # Back button
        menu_button = Button(self.window, text='🔙Menu', font=LABEL_FONT, fg=LETTER_COLOR,
                             activebackground="grey", command=lambda: (self.window.destroy()))
        menu_button.place(x=0, y=0)


def page():
    window = Tk()
    Scan(window)
    window.eval("tk::PlaceWindow . center")
    window.mainloop()


if __name__ == '__main__':
    page()
