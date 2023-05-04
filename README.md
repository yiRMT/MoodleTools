# MoodleTools

## Introduction

This project provides tools to login Moodle automatically.
This project is intended for Osaka Metropolitan University's Moodle, but please edit the code accordingly to make use of it!

## Getting Started

In a Python environment with pip, run:
```bash
pip install -r requirements.txt
```

Create `.env` file to import your authentication info.
The format of the `.env` file is the following:
```
OMUID="Your OMUID"
PASSWORD="Your password"
SETUP_KEY="Setup key for the two factor authentication"
```

## License

This project is under MIT license.