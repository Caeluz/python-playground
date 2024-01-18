import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the user's home directory
home_path = os.path.expanduser("~")

# Combine home path with the desired directory for Laravel project
laravel_project_directory = os.path.join(home_path, 'Documents', 'GitHub', 'osafph-mcg-cares')

# Combine home path with the desired directory for npm project
npm_project_directory = os.path.join(home_path, 'Documents', 'GitHub', 'osafph-frontend')

# Change the working directory for Laravel project
os.chdir(laravel_project_directory)

# Get the server IP from the environment variables
server_ip = os.getenv("SERVER_IP", "localhost")  # Default to localhost if not specified

# Command to run 'php artisan serve' with the server IP from the environment variables
php_command = f'php artisan serve --host {server_ip} --port 80'

# Run php command in a new command prompt window without /wait
os.system(f"start cmd /c {php_command}")

# Change the working directory for npm project
os.chdir(npm_project_directory)

# Command to run 'npm run serve'
npm_command = "npm run serve"

# Run npm command in another new command prompt window without /wait
os.system(f"start cmd /c {npm_command} && pause")
