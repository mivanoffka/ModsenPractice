from django.test import TestCase, Client


class Test(TestCase):
    client = Client()

    def test_200_code(self):
        response = self.client.get("/weather_for_now/40/40")
        open_weather_code = int(str(response.content).split(" ")[0].replace("b'", ""))
        self.assertEqual(open_weather_code, 200)

    def test_400_code(self):
        response = self.client.get("/weather_for_now/40000/40000000")
        open_weather_code = int(str(response.content).split(" ")[0].replace("b'", ""))
        self.assertEqual(open_weather_code, 400)

    def test_401_code(self):
        response = self.client.get("/custom/data|3.0|onecall?lat=40&lon=40&appid=0123456789")
        open_weather_code = int(str(response.content).split(" ")[0].replace("b'", ""))
        self.assertEqual(open_weather_code, 401)

    def test_403_code(self):
        response = self.client.get("/forbidden/")
        open_weather_code = int(str(response.content).split(" ")[0].replace("b'", ""))
        self.assertEqual(open_weather_code, 403)

    def test_404_code(self):
        response = self.client.get("/custom/hello")
        open_weather_code = int(str(response.content).split(" ")[0].replace("b'", ""))
        self.assertEqual(open_weather_code, 404)
