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

  const xss = new Array(locations.length).map(() =>
    new Array(locations.length).map(() => new Variable())
  );

  const solver = new Solver();

  for (const xs of xss) {
    for (const x of xs) {
      solver.createConstraint(x, Operator.Ge);
      solver.createConstraint(x, Operator.Le, 1);
    }
  }

  for (const xs of xss) {
    solver.createConstraint(new Expression(...xs), Operator.Eq);
  }

  for (const xs of lodash.zip(...xss)) {
    solver.createConstraint(new Expression(...xs), Operator.Eq);
  }

  const ts = new Array(locations.length).map(() => new Variable());
  const m = 1000 * locations.length;

  for (const t of ts) {
    solver.createConstraint(t, Operator.Ge);
    solver.createConstraint(t, Operator.Le, locations.length - 1);
  }

  for (const [i, t] of ts.entries()) {
    for (const [j, s] of ts.entries()) {
      solver.createConstraint(
        new Expression(t, 1, [-1, m], [m, xss[i][j]]),
        Operator.Le,
        s
      );
    }
  }

  solver.updateVariables();

  return [];
}

// tslint:disable no-console
console.log(execute([]));
