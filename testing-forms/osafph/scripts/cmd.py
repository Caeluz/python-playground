import os
import subprocess

# Get the user's home directory
home_path = os.path.expanduser("~")

# Combine home path with the desired directory
target_directory = os.path.join(home_path, 'Documents', 'GitHub', 'osafph-mcg-cares')

# Change the working directory
os.chdir(target_directory)

# Command to run 'php artisan serve'
php_command = 'php artisan serve --host 1.1.1.1 --port 80'

# Open cmd and execute the command
process = subprocess.Popen(php_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Get the output and errors
output, errors = process.communicate()

# Print the output and errors
print("Output:", output)
print("Errors:", errors)
