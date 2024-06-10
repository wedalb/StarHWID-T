import subprocess

filepath = "./test-script.bat"
p = subprocess.Popen(filepath, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = p.communicate()
print(p.returncode)  # is 0 if success
