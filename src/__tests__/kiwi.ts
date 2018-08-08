import {
  Constraint,
  Expression,
  Operator,
  Solver,
  Strength,
  Variable
} from "kiwi.js";

test("Minimize an objective funciton", () => {
  const solver = new Solver();

  const x = new Variable();

  solver.createConstraint(x, Operator.Le, 100);
  solver.createConstraint(x, Operator.Ge, 0);
  solver.createConstraint(x, Operator.Le, -100, Strength.weak);

  solver.updateVariables();

  expect(x.value()).toBe(0);
});
