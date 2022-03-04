###############################
# TITLE : OOP Object-Oriented Programming constructor
# CREATE DATE : 2022-02-16
# CREATOR : J
# MODIFIER : J
# MODIFY DATE : 2022-02-17
# VERSION : 1.0.0
###############################

"""
class element
 -member variable(filed, attribute)
 -member method
 -constructor
"""

class language:

    lan_name = ""
    lan_version = 0.0
    lan_type = ""

    def __init__(self, names, versions, ptype):
        self.lan_name = names
        self.lan_version = versions
        self.lan_type = ptype

    def __str__(self):
        print("name : {} " .format(self.lan_name))
        print("version : {}".format(self.lan_version))
        print("type : {}".format(self.lan_type))


if __name__ == "__main__":
    lan1 = language
    lan1.lan_type = "Interpreter"
    lan1.lan_version = 1.9
    lan1.lan_name = "JAVA"

    lan1.__str__(lan1)
    lan1.__init__(lan1, "JAVA", 1.8, "Compiler")
    print("="*20)
    lan1.__str__(lan1)