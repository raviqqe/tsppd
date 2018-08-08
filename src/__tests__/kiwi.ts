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

  solver.createConstraint(x, Operator.Le, new Expression(100));
  solver.createConstraint(x, Operator.Ge, new Expression(0));
  solver.createConstraint(x, Operator.Le, new Expression(-100), Strength.weak);

  solver.updateVariables();

  expect(x.value()).toBe(0);
});
