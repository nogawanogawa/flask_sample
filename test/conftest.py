import os

import pytest
from microservice import create_app

@pytest.fixture
def app():

    # create the app with common test config
    app = create_app({
        'TESTING': True
    })

    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

