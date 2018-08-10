from domain import Location, Trip, Waypoint, WaypointType
from main import find_path


def test_find_path():
    for trips in [
            [
                Trip("my_trip",
                     Waypoint(WaypointType.PICKUP, Location(0, 0)),
                     Waypoint(WaypointType.DROPOFF, Location(1, 0))),
                Trip("your_trip",
                     Waypoint(WaypointType.PICKUP, Location(0, 1)),
                     Waypoint(WaypointType.DROPOFF, Location(1, 1))),
            ],
            [
                Trip("my_trip",
                     Waypoint(WaypointType.PICKUP, Location(0, 0)),
                     Waypoint(WaypointType.DROPOFF, Location(1, 0))),
                Trip("your_trip",
                     Waypoint(WaypointType.PICKUP, Location(0, 1)),
                     Waypoint(WaypointType.DROPOFF, Location(1, 1))),
                Trip("good_trip",
                     Waypoint(WaypointType.PICKUP, Location(0.5, 2)),
                     Waypoint(WaypointType.DROPOFF, Location(1, 3))),
            ],
    ]:
        waypoint_outputs = find_path(trips)

        assert len(waypoint_outputs) == 2 * len(trips)

        for index, pickup_output in enumerate(waypoint_outputs):
            if pickup_output.type == WaypointType.PICKUP:
                dropoff_outputs = [
                    waypoint_output
                    for waypoint_output in waypoint_outputs[index+1:]
                    if waypoint_output.trip_id == pickup_output.trip_id]

                assert len(dropoff_outputs) == 1
                assert dropoff_outputs[0].type == WaypointType.DROPOFF
