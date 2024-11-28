# interlocking_system.py

# Element Klasse, Basis für alle anderen Elemente
# ID ist Unique und soll irgendwann auch berechnet werden
# Name ist der Bezeichner eines Elements
# isDisturbed zeigt an, ob ein Element gestört ist. Wenn ein Element gestört ist, kann keine Fahrstraße etc. gestellt werden.
# station zeigt die zugehörigkeit zum entsprechenden bahnhof, wird derzeit defaultmässig gesetzt, damit der Testcode nicht dauernd geändert werden muss
class Element:
    def __init__(self, id, name, station="MB", isDisturbed=False):
        self.id = id
        self.name = name
        self.station = station
        self.isDisturbed = isDisturbed

    def __repr__(self):
        return f"{self.__class__.__name__}(id='{self.id}', name='{self.name}')"

# Generalized LevelCrossing class
# da ist noch nicht viel getan - geben tut es sie halt :D
class LevelCrossing(Element):
    def __init__(self, id, name, location, status='closed', controlled_by=None):
        super().__init__(id, name)
        self.location = location  # Reference to a Track object
        self.status = status  # "closed", "open"
        self.controlled_by = controlled_by

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'closed'


