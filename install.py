import subprocess

def install(pip_binary):
  pip_install_command = pip_binary + " install -r requirements.txt"
  subprocess.run(pip_install_command)
  print("Installed dependencies using {pip_binary}\n\nRun Clown Browser CLI using the command: python cmd.py\nRun Clown Browser GUI using the command: python main.py")

# Ask user if they want to use a custom pip binary, and if so, which one
pip_binary = input("What pip binary would you like to use? e.g pip3. (Leave blank for default: pip) ")

# Determine pip binary to use and pass it into install()
if pip_binary == "":
  print("Using default pip binary, 'pip'")
  pip_binary = "pip"
  install(pip_binary)
else:
  print(f"Using custom pip binary, '{pip_binary}'")
  install(pip_binary)
