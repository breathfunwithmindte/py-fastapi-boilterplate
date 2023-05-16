from core.app import create_app
from config import settings

from core.exceptions import NonAuthenticatedException

app = create_app()

# Add routes on primary application level.


@app.get("/test-api")
def test_api ():
    raise NonAuthenticatedException
    return { "Hello": "world" }