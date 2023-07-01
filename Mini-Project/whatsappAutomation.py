import pywhatkit as wthelp

print("Let's automate message/image sending on whatsapp !!")
print("Make sure that your QR code is scanned on whatsapp web so that script can send message/image from your behalf")

class automateWhatsapp:

    def __init__(self):

        """
        Takes a contact list to whom the sender wants to 
        send messages/images.  

        """      
        flag = True
        self.contact_list = []
        print('Enter contact number: ')