import {
  Constraint,
  Expression,
  Operator,
  Solver,
  Strength,
  Variable
} from "kiwi.js";
import * as lodash from "lodash";

import { ILocation, ITrip, IWaypointOutput } from "./domain";

export function execute(trips: ITrip[]): IWaypointOutput[] {
  const locations: ILocation[] = trips.flatMap(
    ({ pickupWaypoint, dropoffWaypoint }) => [
      pickupWaypoint.location,
      dropoffWaypoint.location
    ]
  );

  const X = new Array(locations.length).map(() =>
    new Array(locations.length).map(() => new Variable())
  );

  const solver = new Solver();

  for (const xs of X) {
    for (const x of xs) {
      solver.createConstraint(new Expression([x, x], [-1, x]), Operator.Eq);
    }
  }

  for (const xs of X) {
    solver.createConstraint(new Expression(...xs), Operator.Eq);
  }

  for (const xs of lodash.zip(X)) {
    solver.createConstraint(new Expression(...xs), Operator.Eq);
  }

  solver.updateVariables();

  return [];
}

// tslint:disable no-console
console.log(execute([]));
