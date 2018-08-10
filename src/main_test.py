import random

from domain import Location, Trip, Waypoint, WaypointType
from main import find_path


def random_location() -> Location:
    return Location(random.random(), random.random())


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
                 Waypoint(WaypointType.PICKUP,
                          Location(0, 0)),
                 Waypoint(WaypointType.DROPOFF, Location(1, 0))),
            Trip("your_trip",
                 Waypoint(WaypointType.PICKUP,
                          Location(0, 1)),
                 Waypoint(WaypointType.DROPOFF, Location(1, 1))),
            Trip("good_trip",
                 Waypoint(WaypointType.PICKUP,
                          Location(0.5, 2)),
                 Waypoint(WaypointType.DROPOFF, Location(1, 3))),
        ],
        [
            Trip("a",
                 Waypoint(WaypointType.PICKUP, Location(0, 0)),
                 Waypoint(WaypointType.DROPOFF, Location(1, 0))),
            Trip("b",
                 Waypoint(WaypointType.PICKUP, Location(0, 1)),
                 Waypoint(WaypointType.DROPOFF, Location(0, 2))),
            Trip("c",
                 Waypoint(WaypointType.PICKUP, Location(1, 2)),
                 Waypoint(WaypointType.DROPOFF, Location(2, 0))),
            Trip("d",
                 Waypoint(WaypointType.PICKUP, Location(2, 2)),
                 Waypoint(WaypointType.DROPOFF, Location(2, 1))),
        ],
        *[
            [
                Trip(str(i),
                     Waypoint(WaypointType.PICKUP, random_location()),
                     Waypoint(WaypointType.DROPOFF, random_location()))
                for i in range(random.randint(1, 8))
            ]
            for _ in range(10)
        ]
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
