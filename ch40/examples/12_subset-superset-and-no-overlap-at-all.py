required_permissions = {"read", "write"}
user_permissions = {"read", "write", "delete"}

print(required_permissions.issubset(user_permissions))     # has everything required?
print(user_permissions.issuperset(required_permissions))   # same question, other way round

article_tags = {"python", "tutorial"}
video_tags = {"cooking", "recipe"}
print(article_tags.isdisjoint(video_tags))                 # completely unrelated?
