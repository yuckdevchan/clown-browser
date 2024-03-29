import urllib3.request, time, os, wget
from comedious.funny import webcache_folder, app_version

print(f"Clown Browser {app_version}\n")

def dir_gen():
  clown_folder = os.path.dirname(os.path.realpath(__file__))
  path = os.path.join(clown_folder, webcache_folder)
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
    print("Passed Check #1: Is a valid URL, of type: " + "HTTP (Hypertext Transfer Protocol (INSECURE - Unencrypted Connection.))")
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
  
  path = os.path.join(clown_folder, webcache_folder, url_input.split("//")[1])
  if os.path.isdir(path) == False:
    os.mkdir(path)
  else:
    pass
  
  print("Connected to '" + url_input + "' through the internet in " + str(time.process_time() - start) + " seconds.")
  
  index_input = input("Continue to index.html? (y, n): ")

  if index_input == "y":
    print("Downloading index.html...")
    index_load_time = time.process_time()
    website_index = url_input + "/index.html"
    index_file = wget.download(website_index, out=path)
    
    print(f"Downloaded 'index.html' from the {url_input} in " + str(time.process_time() - start) + " seconds.")

url()
