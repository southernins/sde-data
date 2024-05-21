# sde-data
 Stock Dev Environment for Data engineering work


## Execute apps

    docker compose run --rm spark <app_name>.py


## Execute Tests

    docker compose run --rm pytest


this will execute any tests found inteh /apps/test folders. Test filenames must start with test_ or end with _test 

 - test_example_example.py
 - example_widget_test.py