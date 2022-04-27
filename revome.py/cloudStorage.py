from os import access
import dropbox

class TransferData:
        def __init__(self,accesToken):
            self.accessToken=accesToken

        def uploadFile(self,fileFrom,fileTo):
            dpx=dropbox.Dropbox(self.accessToken)
            ef = open(fileFrom,'rb')
            dpx.files_upload(ef.read(),fileTo)

accessToken="sl.BGAW5zKk3D0928HsCGf5Eybl3qf8Ano1EBovylCpZrY-A-tdBQ0AAHHUX0gPW3NoneJc25sgSjVK5Q5lzTCHOW2i4d9x4cgwpyIFGXKr1Kp_qeuEkN9Pgg_9x0pVXiaAyuAlrEU"
transferData=TransferData(accessToken)
filefrom = input("enter the files to transfer")
fileto = input("enter the path to upload")
transferData.uploadFile(filefrom,fileto)
print ("file has been moved")

