"""First frame of the GUI with three buttons given the choice to the user of:
    -   Create a barcode with customer name and numbers (numbers that correspond to a different arguments )
        the data is store in a csv file.
    -   Scan a barcode with the computer camera or type barcode number to be registered in a csv file.
    -   Search a barcode that has been scanned and stored on the csv file that scan.py registered the data """
import createlabeltest
import scan
import search

"""Label Fonts"""
LABEL_TITLE_FONT = ('Arial', 20, "bold")
LABEL_FONT = ('Arial', 15)

"""Colors"""
BUTTON_COLOR = "#5EAAA8"
LETTER_COLOR = "#056676"
BG_COLOR = "#F9F3DF"
ENTRY_FRAME_COLOR = "#A3D2CA"

class Menu:
    def __init__(self,window):
        self.window=window
        self.window.geometry("300x250")
        self.window.config(bg=createlabeltest.BG_COLOR)
        self.window.title("Menu")
        self.window.eval("tk::PlaceWindow . center")

        """Buttons"""
        ### --- Create barcode label button ---###
        create_button = createlabeltest.Button(self.window, text="Create Barcode Label",
                                               font=createlabeltest.LABEL_FONT, bg=createlabeltest.BUTTON_COLOR,
                                               fg=createlabeltest.LETTER_COLOR, cursor="hand2", activebackground="blue",
                                               command=self.go_to_createlabel)
        create_button.grid(row=3, column=1, sticky="w", padx=(50, 50), pady=(10,10))
        ### --- Scan barcode label button ---###
        scan_button = createlabeltest.Button(self.window, text="Scan Barcode label", font=createlabeltest.LABEL_FONT, bg=createlabeltest.BUTTON_COLOR,
                                             fg=createlabeltest.LETTER_COLOR, command=self.go_to_scan)
        scan_button.grid(row=4, column=1, sticky="we", padx=(50, 50), pady=10)
        ### --- Search barcode label button ---###
        search_button = createlabeltest.Button(self.window, text="Search Barcode Label", font=createlabeltest.LABEL_FONT, bg=createlabeltest.BUTTON_COLOR,
                                               borderwidth=2, fg=createlabeltest.LETTER_COLOR, command=self.go_to_search)
        search_button.grid(row=5, column=1, sticky="e", padx=(50, 50), pady=10)

    def go_to_createlabel(self):
        win = createlabeltest.Toplevel()
        createlabeltest.CreateLabel(win)
        # self.window.destroy()

    def go_to_scan(self):
        win = scan.Toplevel()
        scan.Scan(win)

    def go_to_search(self):
        win = search.Toplevel()
        search.Search(win)
def page():
    window = createlabeltest.Tk()
    Menu(window)
    window.mainloop()

if __name__ == '__main__':
    page()