import urllib3.request, time, os

print("Clown Browser v0.1\n")

def dir_gen():
  clown_folder = os.path.dirname(os.path.realpath(__file__))
  path = os.path.join(clown_folder, "webcache")
  if os.path.isdir(path) == False:
    os.mkdir(path)
  else:
    pass

dir_gen()

def url():

  clown_folder = os.path.dirname(os.path.realpath(__file__))

  url_input = input("What website do you want to go to?: ")

  if url_input.startswith("https://") == True:
    print("\nPassed Check #1: Is a valid URL, of type: " + "HTTPS (Hypertext Transfer Protocol Secure)")
  elif url_input.startswith("http://") == True:
    print("Passed Check #1: Is a valid URL, of type: " + "HTTP (Hypertext Transfer Protocol (INSECURE))")
  else:
    print("\nFailed Check #1: Is not a valid URL, of type HTTPS or HTTPS")
    print("\nExiting")
    for i in range(3, 0, -1):
      time.sleep(1)
      print(i)
    exit()

  start = time.process_time()
  http = urllib3.PoolManager()
  r = http.request('GET', url_input)
  print("Website returned code: " + str(r.status))
  
  path = os.path.join(clown_folder, "webcache", url_input.split("//")[1])
  if os.path.isdir(path) == False:
    os.mkdir(path)
  else:
    pass
  
  print("Downloaded '" + url_input + "' from the internet in " + str(time.process_time() - start) + " seconds.")
  
  index_input = input("Continue to index.html? (y, n): ")

  if index_input == "y":
    print("Downloading index.html...")
    index_load_time = time.process_time()
    
    print("Downloaded 'index.html' from the internet in " + str(time.process_time() - start) + " seconds.")

url()
