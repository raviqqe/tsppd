type TripId = string;

interface ILocation {
  latitude: number;
  longitude: number;
}

enum WaypointType {
  Pickup = 1,
  Dropoff = 2
}

interface IWaypoint {
  type: WaypointType;
  location: ILocation;
}

interface ITrip {
  id: TripId;
  pickupWaypoint: IWaypoint;
  dropoffWaypoint: IWaypoint;
}

interface IWaypointOutput {
  tripId: TripId;
  type: WaypointType;
}

function distance(location1: ILocation, location2: ILocation): number {
  const dlat = location2.latitude - location1.latitude;
  const dlon = location2.longitude - location1.longitude;
  return Math.sqrt(dlat * dlat + dlon * dlon);
}

export function execute(trips: ITrip[]): IWaypointOutput[] {
  return [];
}
