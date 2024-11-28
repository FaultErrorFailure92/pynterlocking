from model import Element

# Generalized Track class
# start_point und end_point zeigen den Beginn und das Ende des Gleises an bzw. referenzieren auf Nachbarn: : 
# "start" zeigt den Nachbarn Richtung Kilometer 0, "end" zeigt den Nachbarn Richtung  der aufsteigenden Kilometrierung
class Track(Element):
    def __init__(self, id, name, start_point, end_point, status='free', isDisturbed=False):
        super().__init__(id, name, isDisturbed)
        self.start_point = start_point  # Reference to a Point object
        self.end_point = end_point  # Reference to a Point object
        self.status = status  # "free", "occupied", "blocked"

# Generalized Point class - erbt von Gleis
# besteht aus 2 Gleisen, die über Positiohn umgeschaltet werden können
class Point(Track):
    def __init__(self, id, name, start_point, end_point, end_point_diverged, position='straight', locked=False, controlled_by=None, isDisturbed=False):
        super().__init__(id, name, start_point, end_point, isDisturbed)
        self.end_point_diverged = end_point_diverged
        self.position = position  # "straight", "diverted"
        self.locked = locked
        self.controlled_by = controlled_by

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False
