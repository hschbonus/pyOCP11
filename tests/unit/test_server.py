import server


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


# B4 Test si l'app permet de réserver des places d'une compétition passée
def test_should_not_book_past_competition(client):
    response = client.post('/purchasePlaces', data={'competition': "Spring Festival",
                                                    'club': "Simply Lift",
                                                    'places': 5})
    data = response.data.decode()
    assert 'Great-booking complete!' not in data


# B5 Test si l'app met à jour les points du club après réservation
def test_should_update_club_points_after_booking(client):
    theorical_points = int(server.clubs[0]['points']) - 5
    client.post('/purchasePlaces', data={'competition': "Winter Classic",
                                         'club': "Simply Lift",
                                         'places': 5})
    assert int(server.clubs[0]['points']) == theorical_points


# B6 Test si l'app ne permet pas de réserver plus de places que disponible dans la compétition
def test_should_not_book_more_than_available_places(client):
    response = client.post('/purchasePlaces', data={'competition': "Winter Classic",
                                                    'club': "She Lifts",
                                                    'places': 7})
    data = response.data.decode()
    assert 'Great-booking complete!' not in data
