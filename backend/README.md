# Django

## Migrations

To run python commands on Windows, prefix the file name with "py" and it works fine. _However_ since we want to run migration commands within the docker container, we're actually operating on unix (I think?) so we should use "python3" instead of "py".
...Except we're still executing all on Windows, and thus have to prefix docker-compose with "winpty"

Full commands, assuming running docker container

```
winpty docker-compose exec backend python3 manage.py makemigrations
winpty docker-compose exec backend python3 manage.py migrate
winpty docker-compose exec backend python3 manage.py createsuperuser
```

> Remember to rebuild the docker container after running "migrate"

**Note: Guides tell to use _docker-compose run..._ but "run" creates a new container and we want to execute the command in _the same_ container, hence "exec" instead of "run"**
