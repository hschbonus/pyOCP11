import server


# Test si après réservation, les places sont bien déduites du nombre de places disponibles dans la compétition
def test_should_deduct_places_after_booking(client):
    initial_places = int(server.competitions[2]['numberOfPlaces'])
    client.post('/purchasePlaces', data={'competition': server.competitions[2]['name'],
                                         'club': "Simply Lift",
                                         'places': 5})
    assert int(server.competitions[2]['numberOfPlaces']) == initial_places - 5


# Test si login puis réservation puis logout fonctionne correctement
def test_should_login_book_and_logout(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    client.post('/purchasePlaces', data={'competition': server.competitions[2]['name'],
                                         'club': "Simply Lift",
                                         'places': 5})
    response = client.get('/logout')
    assert response.status_code == 302
    assert response.location == "/"
