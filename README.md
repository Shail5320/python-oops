# Python Refresher — OOP Internals

Working Python implementations of core OOP mechanics — operator overloading, encapsulation, static behavior — written to be read and rebuilt, not just run.

## Why

Most day-to-day Python doesn't force you to think about *why* `__eq__` exists or what a dunder method is actually doing under the hood — you just use the language. This repo is the opposite exercise: strip the abstraction back down and reimplement it deliberately, so the mental model behind the syntax is solid, not assumed.

It's a periodic pass, not a first pass.

## Contents

| File | Covers |
|---|---|
| `01_intro.py` | Functional vs. OOP style, and the structural case for OOP |
| `02_classes.py` | Class/object model, constructors, `self`, instance state |
| `03_methods.py` | Instance methods, defining behavior on objects |
| `04_dunder_methods.py` | Operator overloading — `__str__`, `__eq__`, and friends |
| `05_complex_numbers_project.py` | A full `Complex` number class tying together constructors, dunder methods, and arithmetic (`__add__`, `__mul__`, `__truediv__`) into one working type |
| `06_static_property.py` | Static vs. instance properties, class-level state |

## Structure

```
oops/
├── 01_intro.py
├── 02_classes.py
├── 03_methods.py
├── 04_dunder_methods.py
├── 05_complex_numbers_project.py
└── 06_static_property.py
```

## Running

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>/oops
python3 05_complex_numbers_project.py
```

No external dependencies — standard library only.

## Notes

- `05_complex_numbers_project.py` is the centerpiece so far — a compact way to exercise most of Python's dunder-method surface (`__str__`, `__add__`, `__mul__`, `__truediv__`, `__eq__`) in one working class instead of in isolation.
- Static vs. instance property behavior in `06_static_property.py` is worked through deliberately, not just used in passing.
