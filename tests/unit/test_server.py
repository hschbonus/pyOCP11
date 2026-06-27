# B1 Test si l'app crash pas avec un mauvais email
def test_should_status_code_not_500(client):
    response = client.post('/showSummary', data={'email': 'test@example.com'})
    assert response.status_code != 500


# B2 Test si l'app ne permet pas de réserver plus de places que disponible
def test_should_not_book_without_enough_points(client):
    response = client.post('/purchasePlaces', data={'competition': "Spring Festival",
                                                    'club': "Simply Lift",
                                                    'places': 15})
    data = response.data.decode()
    assert 'Great-booking complete!' not in data


# B3 Test si l'app ne permet pas de réserver plus de 12 places
def test_should_not_book_more_than_12_places(client):
    response = client.post('/purchasePlaces', data={'competition': "Fall Classic",
                                                    'club': "Simply Lift",
                                                    'places': 13})
    data = response.data.decode()
    assert 'Great-booking complete!' not in data
