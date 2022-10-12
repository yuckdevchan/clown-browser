import requests

print("Clown Browser v0.1")

url_input = input("What website do you want to go to?: ")

r = requests.get(url_input, allow_redirects=True)
print("Downloaded '" + url_input + "' from the internet")
