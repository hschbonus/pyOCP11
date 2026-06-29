import server
import pytest  # type: ignore[import]


@pytest.fixture
def client():
    server.clubs = server.loadClubs()
    server.competitions = server.loadCompetitions()
    server.app.config['TESTING'] = True
    with server.app.test_client() as client:
        yield client


@pytest.fixture
def clubs():
    return server.loadClubs()


@pytest.fixture
def competitions():
    return server.loadCompetitions()


@pytest.fixture(scope="session")
def app():
    server.app.config['TESTING'] = True
    return server.app
