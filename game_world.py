world = [[], [], []]  # layers: 0 - background, 1 - midground, 2 - foreground


def add_object(o, depth=0):
    world[depth].append(o)


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return


def clear():
    for layer in world:
        layer.clear()


# Optional helpers used by main.py
def update():
    for layer in world:
        for o in layer:
                o.update()



