import pyotp
import os
from dotenv import load_dotenv

# Import .env file
load_dotenv()


def otp():
    setup_key = os.getenv("SETUP_KEY")
    totp = pyotp.TOTP(setup_key)
    return totp.now()
