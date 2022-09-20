"""
This module is a form to create a barcode label with customer name and the number of the barcode are: invoice number,
position of the item in the invoice, type of article, number of items and an observation case as an option. If any
 case of the form is empty (except 'Observation') and the user clicks on 'save' button the user will see an "Error
 Message" asking the user to fill the missing field. Once everything is in order the data will be saved in a csv file
 ( **is on progress to make this module with the possibility of print a label with the barcode** ).
 """
# import pillow
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import cv2 as cv
import PIL.Image
import pandas as pd
from barcode import Code128
from barcode.writer import ImageWriter

#import setting

"""Label Fonts"""
LABEL_TITLE_FONT = ('Arial', 20, "bold")
LABEL_FONT = ('Arial', 15)

"""Colors"""
BUTTON_COLOR = "#5EAAA8"
LETTER_COLOR = "#056676"
BG_COLOR = "#F9F3DF"
ENTRY_FRAME_COLOR = "#A3D2CA"


class CreateLabel:

    def create_label(self):
        client = self.client.get().title()
        order = self.order.get()
        item = self.item.get()
        material = self.material.get()
        n_of_item = self.n_of_item.get()
        observation = self.observation.get()
        print(type(order + item + n_of_item))
        """"Verification on not empty data before "create_label" """
        if client == '':
            messagebox.showinfo("Error!", 'You must entry a "Customer Name" ')
        elif order == "":
            messagebox.showinfo("Error!", 'You must entry a "Invoice number" ')
        elif item == "":
            messagebox.showinfo("Error!", 'You must entry a "Position in the invoice" ')
        elif material == "":
            messagebox.showinfo("Error!", 'You must entry a "Type" ')
        elif n_of_item == "":
            messagebox.showinfo("Error!", 'You must entry a "Number ot Items"')

        else:
            """date and time"""
            dt = datetime.now()
            date_time = (f'{dt.strftime("%m")}/{dt.strftime("%d")}/{dt.strftime("%Y")}. '
                         f'{dt.strftime("%I")}:{dt.strftime("%M")}{dt.strftime("%p")}')
    #
            """creation of the barcode"""

            numb= f'{order}{item}{n_of_item}'
            # if len(numb) <12:
            #     numb =
            code = Code128(numb, writer=ImageWriter())
            code.save("barcode_image")
            ###????
            print("barcode")
            """"Confirmation Box to confirm with the user is the data is correct and proceed to save the data in the DB """
            ### Yes == True, No ==False
            message = (
                f'Customer Name: {client}\nInvoice Number: {order}\nPosition in the invoice: {item}\nType: {material}\nNumber of items: {n_of_item}')

            confirmation = messagebox.askyesno(title='confirmation',
                                               message=message)

            if confirmation:
##@@@@@@@@@@@@@@@@@@@@@@@@@@@ To fix @@@@@@@@@@@@@@@@@@#
                """sticky_label() if a function to show to the user an image of the barcode once 
the data entered has been confirmed """
                # def sticky_label():
                #     fp = open("barcode_image.png", 'rb' ) #"rb"
                #     img = PIL.Image.open(fp)
                #     withtext = img.save(fp) + (numb)
                #     withtext.show()
                #
                # messagebox.showinfo(title="Barcode", message=sticky_label())
                # with open("venv/barcode_files", "a") as file:
                #     save_barcode = file.write(f'{sticky_label()} + {client}-{numb}')
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###
                """Data Table with all the information of the sticker plus Status,Date and time"""
                # with open("data.csv", "a") as data:
                #     file = data.write(f'{client} {order + item}-{material}-{n_of_item} {numb} {observation}\n')

                scan_data = {"Customer Name": [f'{client}'],
                             "Order number": [f'{order}'],
                             "Item number": [f'{item}'],
                             "Type": [f'{material}'],
                             "Number of items": [f'{n_of_item}'],
                             "Barcode": [f'{numb}'],
                             "Date/Time": [f'{date_time}'],
                             "Observation": [f'{observation}']
                             }
                df = pd.DataFrame(scan_data,
                                  columns=["Customer Name", "Order number", "Item number", "Type", "Number of items",
                                           "Barcode", "Date/Time", "Observation"])
                df = pd.DataFrame(scan_data)
                df.to_csv("label_DataFrame.csv", mode='a', header=True)
                ###???
                print(df)


    def __init__(self, window):

        self.window = window
        self.window.geometry("480x500")
        self.window.config(bg=BG_COLOR)
        self.window.title("Create Label and Barcode")

        """
        TKINTER CODE:
        """

        # create_label_page.config(bg=BG_COLOR)
        # create_label_page_title = Label(self.window, text="Label Creation", font=LABEL_TITLE_FONT,
        #                                 bg=BG_COLOR, fg=LETTER_COLOR)
        # create_label_page_title.grid(padx=5, sticky="n")

        """Labels"""#--------------- LABELS-------------#
        """Customer Name"""
        create_label_page_label_cname = Label(self.window, text="Customer Name:", font=LABEL_FONT,
                                              fg=LETTER_COLOR, bg=BG_COLOR)
        create_label_page_label_cname.grid(row=4, column=0, pady=10)
        """Invoice Number"""
        create_label_page_invoice_n = Label(self.window, text="Invoice number:", font=LABEL_FONT,
                                            fg=LETTER_COLOR, bg=BG_COLOR)
        create_label_page_invoice_n.grid(row=5, column=0, pady=10)
        """Position in Invoice"""
        create_label_page_position_in_invoice = Label(self.window, text="Position in the invoice:",
                                                      font=LABEL_FONT, fg=LETTER_COLOR, bg=BG_COLOR)
        create_label_page_position_in_invoice.grid(row=6, column=0, pady=10)
        """Type"""
        create_label_page_type = Label(self.window, text="Type:", font=LABEL_FONT, justify="left",
                                       fg=LETTER_COLOR, bg=BG_COLOR)
        create_label_page_type.grid(row=7, column=0, pady=10)
        """Number of the Item"""
        create_label_page_n_item = Label(self.window, text="Number of Items:", font=LABEL_FONT, justify="left",
                                         fg=LETTER_COLOR, bg=BG_COLOR)
        create_label_page_n_item.grid(row=8, column=0, pady=10)
        """Observation box"""
        create_label_page_observation = Label(self.window, text="Observation:", font=LABEL_FONT,
                                              fg=LETTER_COLOR, bg=BG_COLOR)
        create_label_page_observation.grid(row=9, column=0, pady=10)

        """Entries of the label"""#--------------------#
        """Customer Name"""
        self.client = Entry(self.window, fg=LETTER_COLOR, font=LABEL_FONT, bg=BG_COLOR, highlightthickness=2)
        self.client.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        self.client.grid(ipadx=20, row=4, column=1)
        """Invoice Number"""
        self.order = Entry(self.window, fg=LETTER_COLOR, font=LABEL_FONT, bg=BG_COLOR, highlightthickness=2)
        self.order.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        self.order.grid(row=5, column=1)
        """Position in Invoice"""
        self.item = Entry(self.window, fg=LETTER_COLOR,font=LABEL_FONT, bg=BG_COLOR, highlightthickness=2)
        self.item.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        self.item.grid(row=6, column=1)
        """Type"""
        self.material = Entry(self.window, fg=LETTER_COLOR, font=LABEL_FONT, bg=BG_COLOR, highlightthickness=2)
        self.material.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        self.material.grid(row=7, column=1)
        """Number of the Item"""
        self.n_of_item = Entry(self.window, fg=LETTER_COLOR, font=LABEL_FONT, bg=BG_COLOR, highlightthickness=2)
        self.n_of_item.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        self.n_of_item.grid(row=8, column=1)
        """Observation box"""
        self.observation = Entry(self.window, fg=LETTER_COLOR, font=LABEL_FONT, bg=BG_COLOR, highlightthickness=2)
        self.observation.config(highlightbackground=ENTRY_FRAME_COLOR, highlightcolor=ENTRY_FRAME_COLOR)
        self.observation.grid(row=9, column=1, ipady="50")

        """-------Buttons------"""
        save_button = Button(self.window, text="Save", font=LABEL_FONT, bg=BUTTON_COLOR, fg=LETTER_COLOR,
                             command=lambda: self.create_label())
        save_button.grid(row=11, sticky="w", padx=20)

        print_button = Button(self.window, text="Print", font=LABEL_FONT, bg=BUTTON_COLOR, fg=LETTER_COLOR)
        print_button.grid(row=11, sticky="e", padx=20)

        back_button = Button(self.window, text="🔙Menu", font=LABEL_FONT, bg=BG_COLOR, fg=LETTER_COLOR,
                             borderwidth=0, command=lambda: (self.window.destroy()))#self.back,
        back_button.grid(row=12, sticky="e", padx=20)


def page():
    window = Tk()
    CreateLabel(window)
    window.eval("tk::PlaceWindow . center")
    window.mainloop()


if __name__ == '__main__':
    page()

