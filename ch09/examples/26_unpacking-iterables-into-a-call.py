def describe_pet(name, animal):
    print(name, "is a", animal)

pet_info = {"name": "Rex", "animal": "dog"}
describe_pet(**pet_info)
