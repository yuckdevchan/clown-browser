import requests
import time

print("Clown Browser v0.1")

def url():
  url_input = input("What website do you want to go to?: ")
  
  start = time.process_time()
  r = requests.get(url_input, allow_redirects=True)
  
  print("Downloaded '" + url_input + "' from the internet in" + time.process_time() - start)
