import requests, time, os

print("Clown Browser v0.1")

def url():
  url_input = input("What website do you want to go to?: ")

  if url_input.startswith("https://") == True:
    print("Passed Check #1: Is a valid URL, of type: " + "HTTPS (Hypertext Transfer Protocol Secure)")
  elif url_input.startswith("http://") == True:
    print("Passed Check #1: Is a valid URL, of type: " + "HTTP (Hypertext Transfer Protocol (INSECURE))")
  else:
    print("Failed Check #1: Is not a valid URL, of type HTTPS or HTTPS")
    print("Exiting")
    for i in range(3, 0, -1):
      time.sleep(1)
      print(i)
    exit()

  start = time.process_time()
  r = requests.get(url_input, allow_redirects=True)
  
  print("Downloaded '" + url_input + "' from the internet in " + str(time.process_time() - start) + " seconds.")

url()
