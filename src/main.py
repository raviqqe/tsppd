from pprint import pprint
from typing import List
import numpy
import pulp

from domain import Trip, trips_to_locations, WaypointOutput, WaypointType
import examples


def find_path(trips: List[Trip]) -> List[WaypointOutput]:
    locations = trips_to_locations(trips)

    n = len(locations)

    problem = pulp.LpProblem("TSPPD")

    xss = [[pulp.LpVariable(f"x({i},{j})", cat="Binary") if i != j else None
            for j in range(n)] for i in range(n)]

    ts = [pulp.LpVariable(f"t({i})", cat="Integer", lowBound=1, upBound=n)
          for i in range(n)]

    objective = pulp.lpSum(
        locations[i].get_distance(locations[j]) * xss[i][j]
        for i in range(n) for j in range(n) if i != j)

    problem += objective

    for i in range(n):
        problem += pulp.lpSum(xss[i][j] for j in range(n) if i != j) == 1
        problem += pulp.lpSum(xss[j][i] for j in range(n) if i != j) == 1

        # A weak constraint to remove partial circuits
        # http://web.tuat.ac.jp/~miya/fujie_ORSJ.pdf
        for j in range(n):
            if j not in (0, i):
                problem += ts[i] - ts[j] + (n-1) * xss[i][j] <= n - 2

    for i in range(0, n, 2):
        problem += ts[i] + 1 <= ts[i+1]

    status = pulp.LpStatus[problem.solve()]

    print(f"Status: {status}")
    print("Objective: {}".format(objective.value()))

    if status != "Optimal":
        raise RuntimeError("no solution found")

    ways = numpy.array(
        [[x.value() if x is not None else 0 for x in xs] for xs in xss]) > 0.5

    indices = [0]

    while True:
        index = numpy.argwhere(ways[indices[-1], :])[0][0]

        if index == 0:
            break

        indices.append(index)

    return [WaypointOutput(trips[index//2].id, WaypointType.PICKUP)
            if index % 2 == 0 else
            WaypointOutput(trips[index//2].id, WaypointType.DROPOFF)
            for index in indices]


def main():
    for trips in examples.trips:
        pprint(find_path(trips))


if __name__ == '__main__':
    main()
