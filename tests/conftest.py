import server
import pytest  # type: ignore[import]


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    with server.app.test_client() as client:
        yield client


@pytest.fixture
def clubs():
    return server.loadClubs()


@pytest.fixture
def competitions():
    return server.loadCompetitions()
