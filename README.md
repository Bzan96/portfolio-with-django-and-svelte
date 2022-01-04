## Debugging

### Superuser creation skipped due to not running in a TTY

**Problem**: _Superuser creation skipped due to not running in a TTY. You can run manage.py createsuperuser in your project to create one manually._

**Solution**: Prefix _python_ with _winpty_ on Windows, eg. winpty python manage.py createsuperuser
