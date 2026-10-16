import itertools

dice_faces = [1, 2, 3, 4, 5, 6]
two_dice_rolls = list(itertools.product(dice_faces, repeat=2))
print(len(two_dice_rolls))
print(two_dice_rolls[:5])
