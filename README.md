# test_rabbit_broker_no_mock
Minimal reproducible example

## Prepare

Create and activate virtual environment. Install requirements

```pip install -r requirements.txt```

## Reproducing the problem

```pytest tests.py::test_handle```

The `SubscriberNotFound` not expected.