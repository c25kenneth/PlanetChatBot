import spacy
import requests
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from api import PlanetBot

jupiter = PlanetBot("Jupiter")
mercury = PlanetBot("Mercury")
venus = PlanetBot("Venus")
earth = PlanetBot("Earth")
mars = PlanetBot("Mars")
saturn = PlanetBot("Saturn")
neptune = PlanetBot("Neptune")
uranus = PlanetBot("Uranus")

chatbot = ChatBot("PlanetBot", storage_adapter='chatterbot.storage.SQLStorageAdapter', logic_adapter=[
    'chatterbot.logic.MathematicalEvaluation',
    'chatterbot.logic.TimeLogicAdapter',
    'chatterbot.logic.BestMatch', {
        'import_path': 'chatterbot.logic.BestMatch',
        "default_response": "I am sorry, I don't understand",
        "maximum_security_threshold": 0.90
    }
],
    database_uri="sqlite:///database.sqlite3"
)
trainer = ListTrainer(chatbot=chatbot)

trainer.train([
    "Hi there!",
    "Hello, how may I help you?",
])
trainer.train([
    "Bye",
    "Bye! Let me know if I can help you with anything else!",
])

# planet base info
trainer.train([
    "Give me info on Jupiter",
    "Here is some base info! On Jupiter: \n" + str(jupiter.getPlanetBaseInfo())
])

trainer.train([
    "Give me info on Mars",
    "Here is some base info! On Mars: \n" + str(mars.getPlanetBaseInfo())
])

trainer.train([
    "Give me info on Venus",
    "Here is some base info! On Venus: \n" + str(venus.getPlanetBaseInfo())
])

trainer.train([
    "Give me info on Earth",
    "Here is some base info! On Earth: \n" + str(earth.getPlanetBaseInfo())
])

trainer.train([
    "Give me info on Mercury",
    "Here is some base info! On Mercury: \n" + str(mercury.getPlanetBaseInfo())
])

trainer.train([
    "Give me info on Saturn",
    "Here is some base info! On Saturn: \n" + str(saturn.getPlanetBaseInfo())
])

trainer.train([
    "Give me info on Neptune",
    "Here is some base info! On Neptune: \n" + str(neptune.getPlanetBaseInfo())
])

trainer.train([
    "Give me info on Uranus",
    "Here is some base info! On Uranus: \n" + str(uranus.getPlanetBaseInfo())
])

# Jupiter info
trainer.train([
    "What is Jupiter's mass",
    "Jupiter has a mass of \n" +
    str(jupiter.getPlanetBaseInfo()["mass"]["massValue"]) + " to the power of " + str(
        jupiter.getPlanetBaseInfo()["mass"]["massExponent"])
])

trainer.train([
    "How many moons does Jupiter have",
    "Jupiter has " + str(len(jupiter.getPlanetBaseInfo()["moons"])) + " moons."
])

trainer.train([
    "Give me some data on Jupiter's moons",
    "Here are some of Jupiter's moons: \n" + str(jupiter.getMoons())
])

trainer.train([
    "What is the density on Jupiter",
    "Jupiter has a density of " +
    str(jupiter.getPlanetBaseInfo()["density"]) + "."
])

trainer.train([
    "What is the gravitational constant on Jupiter",
    "Jupiter has a gravitational constant of " +
    str(jupiter.getPlanetBaseInfo()["gravity"]) + "."
])

# Mercury info
trainer.train([
    "What is Mercury's mass",
    "Mercury has a mass of \n" +
    str(mercury.getPlanetBaseInfo()["mass"]["massValue"]) + " to the power of " + str(
        mercury.getPlanetBaseInfo()["mass"]["massExponent"])
])

trainer.train([
    "How many moons does Mercury have",
    "Mercury has " + mercury.getMoonCount() + " moons."
])

trainer.train([
    "Give me some data on Mercury's moons",
    "Here are some of Mercury's moons: \n" + str(mercury.getMoons())
])

trainer.train([
    "What is the density on Mercury",
    "Mercury has a density of " +
    str(mercury.getPlanetBaseInfo()["density"]) + "."
])

trainer.train([
    "What is the gravitational constant on Mercury",
    "Mercury has a gravitational constant of " +
    str(mercury.getPlanetBaseInfo()["gravity"]) + "."
])

# venus info
trainer.train([
    "What is Venus' mass",
    "Venus has a mass of \n" +
    str(venus.getPlanetBaseInfo()["mass"]["massValue"]) + " to the power of " + str(
        venus.getPlanetBaseInfo()["mass"]["massExponent"])
])

trainer.train([
    "How many moons does Venus have",
    "Venus has " + venus.getMoonCount() + " moons."
])

trainer.train([
    "Give me some data on Venus' moons",
    "Here are some of Venus' moons: \n" + str(venus.getMoons())
])

trainer.train([
    "What is the density on Venus",
    "Venus has a density of " +
    str(venus.getPlanetBaseInfo()["density"]) + "."
])

trainer.train([
    "What is the gravitational constant on Venus",
    "Venus has a gravitational constant of " +
    str(venus.getPlanetBaseInfo()["gravity"]) + "."
])

# earth info
trainer.train([
    "What is Earth's mass",
    "Earth has a mass of \n" +
    str(earth.getPlanetBaseInfo()["mass"]["massValue"]) + " to the power of " + str(
        earth.getPlanetBaseInfo()["mass"]["massExponent"])
])

trainer.train([
    "How many moons does Earth have",
    "Earth has " + earth.getMoonCount() + " moons."
])

trainer.train([
    "Give me some data on Earth's moons",
    "Here are some of Earth's moons: \n" + str(earth.getMoons())
])

trainer.train([
    "What is the density on Earth",
    "Earth has a density of " +
    str(earth.getPlanetBaseInfo()["density"]) + "."
])

trainer.train([
    "What is the gravitational constant on Earth",
    "Earth has a gravitational constant of " +
    str(earth.getPlanetBaseInfo()["gravity"]) + "."
])
# mars info
trainer.train([
    "What is Mars' mass",
    "Mars has a mass of \n" +
    str(mars.getPlanetBaseInfo()["mass"]["massValue"]) + " to the power of " + str(
        mars.getPlanetBaseInfo()["mass"]["massExponent"])
])

trainer.train([
    "How many moons does Mars have",
    "Mars has " + mars.getMoonCount() + " moons."
])

trainer.train([
    "Give me some data on Mars' moons",
    "Here are some of Mars' moons: \n" + str(mars.getMoons())
])

trainer.train([
    "What is the density on Mars",
    "Mars has a density of " +
    str(mars.getPlanetBaseInfo()["density"]) + "."
])

trainer.train([
    "What is the gravitational constant on Mars",
    "Mars has a gravitational constant of " +
    str(mars.getPlanetBaseInfo()["gravity"]) + "."
])

# saturn info
trainer.train([
    "What is Saturn's mass",
    "Saturn has a mass of \n" +
    str(saturn.getPlanetBaseInfo()["mass"]["massValue"]) + " to the power of " + str(
        saturn.getPlanetBaseInfo()["mass"]["massExponent"])
])

trainer.train([
    "How many moons does Saturn have",
    "Saturn has " + str(len(saturn.getPlanetBaseInfo()["moons"])) + " moons."
])

trainer.train([
    "Give me some data on Saturn's moons",
    "Here are some of Saturn's moons: \n" + str(saturn.getMoons())
])

trainer.train([
    "What is the density on Saturn",
    "Saturn has a density of " +
    str(saturn.getPlanetBaseInfo()["density"]) + "."
])

trainer.train([
    "What is the gravitational constant on Saturn",
    "Saturn has a gravitational constant of " +
    str(saturn.getPlanetBaseInfo()["gravity"]) + "."
])

# neptune info
trainer.train([
    "What is Neptune's mass",
    "Neptune has a mass of \n" +
    str(neptune.getPlanetBaseInfo()["mass"]["massValue"]) + " to the power of " + str(
        neptune.getPlanetBaseInfo()["mass"]["massExponent"])
])

trainer.train([
    "How many moons does Neptune have",
    "Neptune has " + str(len(neptune.getPlanetBaseInfo()["moons"])) + " moons."
])

trainer.train([
    "Give me some data on Neptune's moons",
    "Here are some of Neptune's moons: \n" + str(neptune.getMoons())
])

trainer.train([
    "What is the density on Neptune",
    "Neptune has a density of " +
    str(neptune.getPlanetBaseInfo()["density"]) + "."
])

trainer.train([
    "What is the gravitational constant on Neptune",
    "Neptune has a gravitational constant of " +
    str(neptune.getPlanetBaseInfo()["gravity"]) + "."
])

# uranus info
trainer.train([
    "What is Uranus' mass",
    "Uranus has a mass of \n" +
    str(uranus.getPlanetBaseInfo()["mass"]["massValue"]) + " to the power of " + str(
        uranus.getPlanetBaseInfo()["mass"]["massExponent"])
])

trainer.train([
    "How many moons does Uranus have",
    "Uranus has " + uranus.getMoonCount() + " moons."
])

trainer.train([
    "Give me some data on Uranus' moons",
    "Here are some of Uranus' moons: \n" + str(uranus.getMoons())
])

trainer.train([
    "What is the density on Uranus",
    "Uranus has a density of " +
    str(uranus.getPlanetBaseInfo()["density"]) + "."
])

trainer.train([
    "What is the gravitational constant on Uranus",
    "Uranus has a gravitational constant of " +
    str(uranus.getPlanetBaseInfo()["gravity"]) + "."
])
# print("Hi! I am the PlanetBot, a chatbot that is able to answer questions about a variety of planets in our solar system.")
# while True:
#     request = input("You" + ': ')
#     response = chatbot.get_response(request)
#     print('Bot:', response)
