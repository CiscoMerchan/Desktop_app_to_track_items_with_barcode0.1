#Desktop app to track items with a barcode
Tkinter GUI to create, read/register and search barcodes (barcode are store in csv file) 

This a personal project, the idea is to follow a product that need to be transformed  and to be able to follow a 
production sequence it by give an identity to te product and then register each transformation step by assigning a 
number/name to each stage, this way the user is able to search on which step is the product. 

  This desktop app contain 4 main modules:
  * menu.py: Is the first frame once the user open the app. contains three buttons. Create Barcode Label,  
              Scan Barcode Label, Search Barcode Label.
  * createlabeltest.py: This module is a form to create a barcode label with customer name and the number 
              of the barcode are: invoice number, position of the item in the invoice, type of article, 
              number of items and an observation case as an option. If any case of the form is empty 
              (except 'Observation') and the user clicks on 'save' button the user will see an "Error Message" 
              asking the user to fill the missing field. Once everything is in order the data will be saved 
              in a csv file. The barcode is visible in "barcode_image.png" ( **Is on progress to make this module 
              with the possibility of print a label with the barcode** ).
  * scan.py: This module is to register a barcode in a csv file either by scanning a barcode (using the computer 
               camera) or type in the barcode number. The number will be store in a csv file that can be access in
               "Search Barcode Label".  For this reason is mandatory to fill the 'stage' input case to follow up the
               different stage of the transformation when the user search in "Search Barcode Label"(**the result are 
               visible in "barcode_result.txt"**).
    
  * search.py: This module is to visualise the barcodes that has been recorded in "Scan Barcode Label" by and/or:
                Name, station, order number, barcode number, date , time.(**NOTE: At the moment is uncompleted. There is
                only the entry fields**) 

  - In requirements.txt you can see all the libraries used for the app
  