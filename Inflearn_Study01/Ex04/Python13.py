###############################
# TITLE : Abstract
# CREATE DATE : 2022-02-25
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from abc import *


class ContentSender(metaclass=ABCMeta):
    title = ""
    name = ""

    # constructor
    def __init__(self, title, name):
        self.title = title
        self.name = name

    @abstractmethod
    def send_message(self, recipient):
        pass

class StudentBase(metaclass=ABCMeta):

    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_school(self):
        pass

class Student(StudentBase):

    # overriding
    def study(self):
        print("I\'m studying right now.")

    # overriding
    def go_school(self):
        print("I\'m going to school.")


class KakaoSender(ContentSender):

    content = ""

    def __init__(self, title, name, content):
        super().__init__(title, name)
        self.content = content

    def send_message(self, recipient):
        print("Title : {}".format(self.title))
        print("Name : {}".format(self.name))
        print("Content : {}". format(self.content))
        print("recipient : {}".format(recipient))


class SmsSender(ContentSender):
    content = ""

    def __init__(self, title, name, content):
        super().__init__(self, title, name)
        self.content = content

    def send_message(self, recipient):
        print("Title : {}".format(self.title))
        print("Name : {}".format(self.name))
        print("Content : {}".format(self.content))
        print("recipient : {}".format(recipient))


if __name__ == "__main__":
    student = Student()
    student.study()
    student.go_school()

    kakao = KakaoSender("Kakao", "Lee", "Hello")
    kakao.send_message("creditor")