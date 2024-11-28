from model import *
from signals import *
from tracks import *

# Fahrstraßenlogik
# Das Einstellen einer Fahrstraße durchläuft mehrere Schritte
# Eingabe - done
# Zulässigkeitsprüfung
# Fahrstraßeneinstellung
# Fahrstraßenfestlegung
# Signalfreischaltung
# Freistellvorgang
class Route:
    # Klassenvariable für alle Routen
    all_routes = []
    def __init__(self, route_id: int, start: LightSignal, goal: LightSignal, routeType='train', tracks=None):
        self.route_id = route_id
        if all(isinstance(track, Track) for track in tracks):
            self.start = start
            self.goal = goal    
            self.routeType= routeType
            self.tracks = tracks if tracks is not None else []
            # Automatisch zur Klassenvariable hinzufügen
            Route.all_routes.append(self)
        else:
            raise ValueError("Alle Elemente in 'tracks' müssen Instanzen der Klasse 'Track' sein.")

    def __repr__(self):
        track_names = [track.name for track in self.tracks]
        return f"Route(id={self.route_id}, tracks={track_names})"
    
    # Mastermethode zum Einstellen der Fahrstraße
    @classmethod
    def setRoute(start, goal):
        route_type = Route.checkSignals(start, goal)
        matching_routes = Route.findRoutes(start, goal, route_type)

    
    #####################################################################################
    # Eingabe
    # Startsignal & Zielsignal muss angegeben werden
    # Startsignal muss Haupt- oder Schutz-Signal sein
    # Zielsignal muss Haupt- oder Schutz- Signal, oder Verschubsignal mit Zugziel sein
    # Regel- und/oder Umwegfahrstraße muss projektiert sein
    #####################################################################################

    
    # Stelle fest, ob die Signale geeignet für eine Fahrstraße sind, gibt den Fahrstraßentyp "train", "shunting" oder None zurück
    @classmethod
    def checkSignals (start, goal):
        print("Fahrstraßeneingabe")
        if (isinstance(goal, MainSignal, ProtectionSignal, ShuntingSignal) and isinstance(start, MainSignal, ProtectionSignal)):
            print("Fahrstraßenlogik für {start.id} nach {goal.id}: {goal.id} darf TRAIN-Fahrstraße sein")
            route_type = "train"
            return route_type
        if (isinstance(goal, ShuntingSignal) and goal.isTrainGoal and isinstance(start, MainSignal, ProtectionSignal)):
            print("Fahrstraßenlogik für {start.id} nach {goal.id}: {goal.id} darf TRAIN-Fahrstraße sein")
            route_type = "train"
            return route_type
        if (isinstance(goal, ShuntingSignal) and isinstance(start, ShuntingSignal)):
            print("Fahrstraßenlogik für {start.id} nach {goal.id}: {goal.id} darf SHUNTING-Straße sein")
            route_type = "shunting"
            return route_type
        return

    @classmethod
    def list_all_routes(cls):
        print("Alle gespeicherten Routen:")
        for route in cls.all_routes:
            print(route)
  
    @classmethod  
    def findRoutes(cls, start, goal, route_type):
        matching_routes = [
        route for route in cls.all_routes if route.start == start and route.goal == goal and route.route_type == route_type]
        if matching_routes:
            print(f"Gefundene Routen von {start} nach {goal}:")
            for route in matching_routes:
                print(route)
            
            return matching_routes
        else:
            print(f"Keine Routen von {start} nach {goal} gefunden.")
            raise()
        

 