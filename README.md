# Travelling Salesman Problem with Pickup and Delivery (TSPPD)

[![Circle CI](https://img.shields.io/circleci/project/github/raviqqe/tsppd.svg?style=flat-square)](https://circleci.com/gh/raviqqe/tsppd)
[![License](https://img.shields.io/github/license/raviqqe/tsppd.svg?style=flat-square)](LICENSE)

The solution for TSPPD with [PuLP][pulp] in Python.

## Description

The TSPPD is formulated as an integer linear programming problem with extra
constraints of pickup and delivery because each passenger needs to be picked up
before being dropped off.
As the underlying ILP solver is [CBC](https://github.com/coin-or/Cbc) used by
[PuLP][pulp], the branch-and-cut method is used for faster solution search.

## Running examples

```
python3 src/main.py
```

## License

[MIT](LICENSE)

[pulp]: https://github.com/coin-or/pulp
