import cv2
import pyzbar.pyzbar as pyzbar
from tkinter import messagebox


# class Bar:
#     def read_barcodes(self,frame):
#         barcodes = pyzbar.decode(frame)
#         for barcode in barcodes:
#             x, y, w, h = barcode.rect
#             # 1
#             barcode_info = barcode.data.decode('utf-8')
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#             # 2
#             font = cv2.FONT_HERSHEY_DUPLEX
#             cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
#             # 3
#             with open("barcode_result.txt", mode='a') as file:
#                 file.write(f"Recognized Barcode: {barcode_info}\n")
#                 messagebox.askyesno(title='confirmation', message=barcode_info)
#         return frame
#
#     def main(self):
#         # 1
#         camera = cv2.VideoCapture(0)
#         ret, frame = camera.read()
#         # 2
#         while ret:
#             ret, frame = camera.read()
#             frame = self.read_barcodes(frame)
#             cv2.imshow('Barcode/QR code reader', frame)
#
#             if cv2.waitKey(1) & 0xFF == 27:
#                 break
#         # 3
#         camera.release()
#         cv2.destroyAllWindows()
#
#     # 4
#     if __name__ == '__main__':
#         main()
#         read_barcodes()

def scanQR():
    i = 0
    vid = cv2.VideoCapture(0)
    while i < 2:
        _, f = vid.read()
        decoded = pyzbar.decode(f)
        for obj in decoded:
            print(f'{obj.data}')
            i += 1
        cv2.imshow('Barcode/QRCode', f)
        cv2.waitKey(5)
        cv2.destroyAllWindows
