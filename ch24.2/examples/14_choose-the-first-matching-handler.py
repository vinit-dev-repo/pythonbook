try:
    raise ValidationError("bad value")
except ValidationError:
    print("Specific recovery")
except AppError:
    print("General app recovery")
print("After the handlers")
