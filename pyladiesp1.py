colours = ["red"]

for i in colours:
    if i == "red":
        colours += ["black"]
    if i == "black":
        colours += ["white"]

print(colours)

# ------------------------------------------------------------#

colours = ["red"]

for i in colours[:]:
    if i == "red":
        colours += ["black"]
    if i == "black":
        colours += ["white"]

    print(colours)
