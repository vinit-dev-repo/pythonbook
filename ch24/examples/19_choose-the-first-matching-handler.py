try:
    raise ValidationError("bad value")
except AppError:
    print("General app recovery")
except ValidationError:
    print("Specific recovery")
print("After the handlers")
