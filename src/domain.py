from collections import namedtuple
from enum import Enum
from typing import List


__all__ = [
    "Location",
    "Trip",
    "trips_to_locations",
    "Waypoint",
    "WaypointType",
    "WaypointOutput",
]


class Location(namedtuple("Location", ["x", "y"])):
    def get_distance(self, location: "Location"):
        return ((self.x - location.x) ** 2 + (self.y - location.y) ** 2) ** 0.5


class WaypointType(Enum):
    PICKUP = 1
    DROPOFF = 2


Waypoint = namedtuple("Waypoint", ["type", "location"])

Trip = namedtuple("Trip", ["id", "pickup_waypoint", "dropoff_waypoint"])

WaypointOutput = namedtuple("WaypointOutput", ["trip_id", "type"])


def trips_to_locations(trips: List[Trip]) -> List[Location]:
    return [location for locations in
            [[trip.pickup_waypoint.location, trip.dropoff_waypoint.location]
             for trip in trips]
            for location in locations]
