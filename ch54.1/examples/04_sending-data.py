import os

api_key = os.environ.get("WEATHER_API_KEY")   # read it, never hard-code it
print("key found in the environment:", api_key is not None)
