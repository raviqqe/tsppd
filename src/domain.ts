export type TripId = string;

export interface ILocation {
  latitude: number;
  longitude: number;
}

export enum WaypointType {
  Pickup = 1,
  Dropoff = 2
}

export interface IWaypoint {
  type: WaypointType;
  location: ILocation;
}

export interface ITrip {
  id: TripId;
  pickupWaypoint: IWaypoint;
  dropoffWaypoint: IWaypoint;
}

export interface IWaypointOutput {
  tripId: TripId;
  type: WaypointType;
}

export function distance(location1: ILocation, location2: ILocation): number {
  const dlat = location2.latitude - location1.latitude;
  const dlon = location2.longitude - location1.longitude;
  return Math.sqrt(dlat * dlat + dlon * dlon);
}
