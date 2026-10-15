# lifecycle_import.py
import lifecycle_model as model
import lifecycle_model as again

print("same cached module:", model is again)
print("own fields:", model.Parcel.declared_fields, model.Child.declared_fields)
print("nested name:", model.Parcel.Note.__qualname__)
print("direct bases:", [base.__name__ for base in model.Child.__bases__])
print("direct children:", [cls.__name__ for cls in model.Parcel.__subclasses__()])
print("MRO:", [cls.__name__ for cls in model.Child.__mro__])
print(model.Child.mro() == list(model.Child.__mro__))
