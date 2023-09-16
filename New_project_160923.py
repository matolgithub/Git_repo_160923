import requests
import pywhatkit


class GlobalTest:
    def __init__(self, phone_number="+79175955650", e_mail="matolpydev@gmail.com", mail_pswd="csszpkcslndaiita",
                 subject="Simple subject of the letter", message="Hello, testing message from the junior developer!",
                 mail_receiver=["volodchenko1972@yandex.ru", "matolpydev@gmail.com", "89175955650@mail.ru",
                                "volodchenko@list.ru"]):
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.mail_pswd = mail_pswd
        self.subject = subject
        self.message = message
        self.mail_receiver = mail_receiver

    def test_1(self):
        num = 1
        for item in self.mail_receiver:
            if self.e_mail == item:
                print("The message sent to itself!")
            else:
                print(f"{num}: Well, done! The message will sent to {item} from {self.e_mail}.")
            pywhatkit.send_mail(self.e_mail, self.mail_pswd, self.subject, self.message, item)
            num += 1

    def test_2(self):
        # pywhatkit.whats.sendwhatmsg(self.phone_number, self.message, time_hour=19, time_min=47)
        # pywhatkit.sendwhats_image(self.phone_number, "333.jpg")
        pywhatkit.sendwhats_image(self.phone_number, "https://img1.fonwall.ru/o/az/kot-yumor-sherst.jpg")


if __name__ == "__main__":
    # global_test_obj = GlobalTest()
    # global_test_obj.test_1()
    global_test_obj = GlobalTest()
    global_test_obj.test_2()
