import requests


class PlanetBot:
    def __init__(self, planetName):
        self.planetName = planetName

    def getPlanetBaseInfo(self):
        r = requests.get(
            f"https://api.le-systeme-solaire.net/rest/bodies/{self.planetName}")
        data = r.json()
        return data

    def getPlanetDensity(self):
        r = requests.get(
            f"https://api.le-systeme-solaire.net/rest/bodies/{self.planetName}")
        data = r.json()
        print(data["density"])
        return data["density"]

    def isPlanet(self):
        r = requests.get(
            f"https://api.le-systeme-solaire.net/rest/bodies/{self.planetName}")
        data = r.json()
        print(data["isPlanet"])
        return data["isPlanet"]

    def getMoons(self):
        r = requests.get(
            f"https://api.le-systeme-solaire.net/rest/bodies/{self.planetName}")
        data = r.json()
        if (data["moons"] is None):
            return "This planet has no moons!"
        elif (len(data["moons"]) <= 5):
            return data["moons"]
        elif (len(data["moons"]) > 5):
            moons = []
            i = [0, 1, 2, 3, 4]
            for x in i:
                moons.append(data["moons"][x])
            return moons

    def getMoonCount(self):
        r = requests.get(
            f"https://api.le-systeme-solaire.net/rest/bodies/{self.planetName}")
        data = r.json()
        if data["moons"] is not None:
            return str(len(data["moons"]))
        else:
            return "no"
# bot = PlanetBot(planetName="Earth")
# bot.getMoons()
