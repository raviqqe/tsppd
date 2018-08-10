import random

from domain import Location, Trip, Waypoint, WaypointType
from main import find_path
import examples


def random_location() -> Location:
    return Location(random.random(), random.random())


def test_find_path():
    for trips in [
        *examples.trips,
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
