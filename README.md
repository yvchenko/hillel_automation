Welcome! This repository contains automated tests.

To run all of the tests use the following command:
> pytest

If you only need to run BDD tests that are made for API, use the following command:
> pytest -m "bdd and api"

If you only need to run BDD tests that are made for UI, use the following command:
> pytest -m "bdd and ui"

You can also run all the API tests:
> pytest -m api

Or all the UI tests:
> pytest -m ui

Or only BDD tests:
> pytest -m bdd

Hope that's useful!
