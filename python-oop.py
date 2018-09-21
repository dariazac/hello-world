# Object Oriented Programming


class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_id(self):
        print "My real name is {}".format(self.name)


class Hero(Person):
    def __init__(self, name, h_name):
        super(Hero, self).__init__(name)
        self.h_name = h_name

    def reveal_id(self):
        super(Hero, self).reveal_id()
        print "...And I am {}".format(self.h_name)


wade = Hero("wade wilson", 'Deadpool')
wade.reveal_id()
