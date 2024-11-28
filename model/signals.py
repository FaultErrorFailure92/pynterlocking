from model import Element

# Generalized Signal class
# Track referenziert auf das zugehörige Gleis
# state bildet den aktuell gezeigten aspect an
# aspects bildet die Liste aller möglichen Begriffe ab
# next_signal bildet das nächste Signal in der Kette ab
# direction zeigt die Richtung eines Signals: "Home" zeigt in Richtung von Kilometer 0, "Out" in Richtung der aufsteigenden Kilometrierung
class LightSignal(Element):
    def __init__(self, id, name, track, state="stop", aspects=["stop","free","reduced"], direction='home', isDisturbed=False):
        super().__init__(id, name, isDisturbed)
        self.track = track
        self.aspects = aspects
        self.state = state
        self.next_signal = None  
        self.direction = direction

    def set_next_signal(self, next_signal):
        self.next_signal = next_signal

# MainSignal class (inherits from Signal)
# mainSignal_type kann "Entry", "Exit", "Block" oder "Inter" sein
class MainSignal(LightSignal):
    def __init__(self, id, name, location, state="stop", aspects=["stop","free","reduced"], direction='home', mainSignal_type="entry", isDisturbed=False):
        super().__init__(id, name, location, state, direction, mainSignal_type, isDisturbed)
        self.mainSignal_type = mainSignal_type

# ShuntingSignal class (inherits from Signal)
class ShuntingSignal(LightSignal):
    def __init__(self, id, name, location, state="stop", aspects=["stop","free","reduced"], controlled_by=None, isTrainGoal=False, isDisturbed=False):
        super().__init__(id, name, location, state, controlled_by, isDisturbed)
        self.isTrainGoal = isTrainGoal

# Generalized SignalRepeater class
class SignalRepeater(LightSignal):
    def __init__(self, id, name, signal, display_state='stop'):
        super().__init__(id, name)
        self.signal = signal  # Reference to a Signal object
        self.display_state = display_state  # Mirrors the state of the associated signal

    def update_display_state(self):
        self.display_state = self.signal.state


# Generalized distantSignal class
class DistantSignal(LightSignal):
    def __init__(self, id, name, signal, display_state='stop'):
        super().__init__(id, name)
        self.signal = signal  # Reference to a Signal object
        self.display_state = display_state  # Mirrors the state of the associated signal

    def update_display_state(self):
        self.display_state = self.signal.state



# Generalized distantSignal class
class ProtectionSignal(LightSignal):
    def __init__(self, id, name, signal, display_state='stop'):
        super().__init__(id, name)
        self.signal = signal  # Reference to a Signal object
        self.display_state = display_state  # Mirrors the state of the associated signal

    def update_display_state(self):
        self.display_state = self.signal.state
