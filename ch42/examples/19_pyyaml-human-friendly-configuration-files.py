import yaml   # python -m pip install PyYAML==6.0.3

text = "name: Amy\nage: 28\nscores:\n  - 90\n  - 85\n"
data = yaml.safe_load(text)
print(data)
