from typing import List

from domain import Location, Trip, Waypoint, WaypointType

trips: List[List[Trip]] = [
    [
        Trip(
            "my_trip",
            Waypoint(WaypointType.PICKUP, Location(0, 0)),
            Waypoint(WaypointType.DROPOFF, Location(1, 0)),
        ),
        Trip(
            "your_trip",
            Waypoint(WaypointType.PICKUP, Location(0, 1)),
            Waypoint(WaypointType.DROPOFF, Location(1, 1)),
        ),
    ],
    [
        Trip(
            "my_trip",
            Waypoint(WaypointType.PICKUP, Location(0, 0)),
            Waypoint(WaypointType.DROPOFF, Location(1, 0)),
        ),
        Trip(
            "your_trip",
            Waypoint(WaypointType.PICKUP, Location(0, 1)),
            Waypoint(WaypointType.DROPOFF, Location(1, 1)),
        ),
        Trip(
            "good_trip",
            Waypoint(WaypointType.PICKUP, Location(0.5, 2)),
            Waypoint(WaypointType.DROPOFF, Location(1, 3)),
        ),
    ],
    [
        Trip(
            "a",
            Waypoint(WaypointType.PICKUP, Location(0, 0)),
            Waypoint(WaypointType.DROPOFF, Location(1, 0)),
        ),
        Trip(
            "b",
            Waypoint(WaypointType.PICKUP, Location(0, 1)),
            Waypoint(WaypointType.DROPOFF, Location(0, 2)),
        ),
        Trip(
            "c",
            Waypoint(WaypointType.PICKUP, Location(1, 2)),
            Waypoint(WaypointType.DROPOFF, Location(2, 0)),
        ),
        Trip(
            "d",
            Waypoint(WaypointType.PICKUP, Location(2, 2)),
            Waypoint(WaypointType.DROPOFF, Location(2, 1)),
        ),
    ],
]
