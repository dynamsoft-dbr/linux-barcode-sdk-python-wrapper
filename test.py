import os.path
import dbr

def initLicense(license):
    dbr.initLicense(license)

def decodeFile(fileName):
    dbr.initLicense("t0068MgAAAGvV3VqfqOzkuVGi7x/PFfZUQoUyJOakuduaSEoI2Pc8+kMwjrojxQgE5aJphmhagRmq/S9lppTkM4w3qCQezxk=")
    formats = 0x3FF | 0x2000000 | 0x8000000 | 0x4000000; # 1D, QRCODE, PDF417, DataMatrix
    results = dbr.decodeFile(fileName, formats)
    
    for result in results:
        print("barcode format: " + result[0])
        print("barcode value: " + result[1])

if __name__ == "__main__":
    barcode_image = input("Enter the barcode file: ");
    if not os.path.isfile(barcode_image):
        print "It is not a valid file."
    else:
        decodeFile(barcode_image);