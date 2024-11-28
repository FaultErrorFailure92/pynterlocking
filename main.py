"""main.py
Setup and Use pyinterlocking.
For now it creates test-elements. Later on it main.py ill hold all the startup methods like introducing the topology and connecting to the user interface.
"""

from model import Track, Point, MainSignal, ShuntingSignal, SignalRepeater, LevelCrossing, Route

def test_interlocking_system():
    # Create elements
    track_1 = Track(id="track_1", name="Track 1", start_point=None, end_point=None)
    track_2 = Track(id="track_2", name="Track 2", start_point=None, end_point=None)
    point_1 = Point(id="point_1", name="Point 1", location=track_1, position="straight")
    point_2 = Point(id="point_2", name="Point 2", location=track_2, position="straight")
    signal_1 = MainSignal(id="signal_1", name="Signal 1", location=track_1, state="stop")
    signal_2 = MainSignal(id="signal_2", name="Signal 2", location=track_2, state="stop")
    shunting_signal_1 = ShuntingSignal(id="shunting_signal_1", name="Shunting Signal 1", location=track_2, state="stop")
    repeater_1 = SignalRepeater(id="repeater_1", name="Repeater 1", signal=signal_1)
    level_crossing_1 = LevelCrossing(id="level_crossing_1", name="Level Crossing 1", location=track_1, status="closed")


    route_101 = Route(route_id=101, start=signal_1, goal=signal_2, routeType="train", tracks=[track_1, track_2])
    print(route_101.route_id)
    print(route_101.start.id)
    print(route_101.goal.id)
    print(route_101.routeType)
    print(route_101.tracks)

    print(Route.list_all_routes())


    # Set next signal for chaining logic
    signal_1.set_next_signal(shunting_signal_1)

    # Example of locking a point
    point_1.lock()

    # Print out some of the elements
    print(track_1)
    print(signal_1)
    print(shunting_signal_1)
    print(repeater_1)
    print(level_crossing_1)

    # Check if point is locked
    print(f"Point 1 locked: {point_1.locked}")

if __name__ == "__main__":
    test_interlocking_system()
