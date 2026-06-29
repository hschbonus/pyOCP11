from locust import HttpUser, task, between


class GudlftUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def view_competitions(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task(1)
    def purchase_places(self):
        with self.client.post(
            "/purchasePlaces",
            data={
                "competition": "Winter Classic",
                "club": "Simply Lift",
                "places": "1",
            },
            catch_response=True,
        ) as response:
            if response.status_code in (200, 400):
                response.success()

    @task(1)
    def view_points_board(self):
        self.client.get("/pointsBoard")
