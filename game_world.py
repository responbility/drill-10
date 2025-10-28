world = []


define add_object(o):
      world.objects.append(o)

      def add_object(o):
          world.append(o)

        def update_world():
            for layer in world:
            for o in world:
                o.update()


     def render():
         for layer in world:
         for o in world:
             o.draw()

     def remove_object(o):
         for layer in world:
             if o in layer:
                    world.remove(o)
                    layer.remove(o)
                    return

