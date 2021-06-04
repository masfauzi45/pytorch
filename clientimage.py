import requests


resp = requests.post("https://tugasfauzi.herokuapp.com/",
                     files={'file': open('dog.png', 'rb')})
print(resp.text)
