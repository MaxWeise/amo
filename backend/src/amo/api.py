"""Define the API Endpoints for the server."""

from typing import Any

import flask

app = flask.Flask(__name__)


# Weapons endpoint
@app.get("/weapons")
def get_weapons() -> list[dict[str, Any]]:
    """Get all the weapons in the database.

    Returns:
        list[dict[str, Any]]: The list of weapon objects as json dicts.
    """
    pass


@app.post("/weapons")
def post_weapons() -> list[dict[str, Any]]:
    """Post json objects to the endpoint.

    Returns:
        list[dict[str, Any]]: The list of weapon objects as json dicts.
    """
    pass
