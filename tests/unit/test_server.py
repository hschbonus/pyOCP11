def test_should_status_code_not_500(client):
    response = client.post('/showSummary', data={'email': 'test@example.com'})
    assert response.status_code != 500
