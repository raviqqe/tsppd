from enum import Enum
from typing import List, NamedTuple


__all__ = [
    "Location",
    "Trip",
    "trips_to_locations",
    "Waypoint",
    "WaypointType",
    "WaypointOutput",
]


class Location(NamedTuple):
    x: float
    y: float

    def get_distance(self, location: "Location"):
        return ((self.x - location.x) ** 2 + (self.y - location.y) ** 2) ** 0.5


class WaypointType(Enum):
    PICKUP = 1
    DROPOFF = 2


class Waypoint(NamedTuple):
    type: WaypointType
    location: Location


class Trip(NamedTuple):
    id: str
    pickup_waypoint: Waypoint
    dropoff_waypoint: Waypoint


class WaypointOutput(NamedTuple):
    trip_id: str
    type: WaypointType


def trips_to_locations(trips: List[Trip]) -> List[Location]:
    return [
        location
        for locations in [
            [trip.pickup_waypoint.location, trip.dropoff_waypoint.location]
            for trip in trips
        ]
        for location in locations
    ]
