import subprocess

def install_prequisites():
    try:
        subprocess.check_call(["pip", "install", "selenium"])
        subprocess.check_call(["pip", "install", "webdriver-manager"])
        subprocess.check_call(["pip", "install", "python-dotenv"])
    except Exception as e:
        print(f"Error installing prerequisites: {e}")

if __name__ == "__main__":
    install_prequisites()