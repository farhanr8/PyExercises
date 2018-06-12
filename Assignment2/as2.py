def print_time(time, msg):
    print(time, msg, sep=': ')

# TODO: add new functions below this line
# TODO: add new functions above this line

def handle_new_order(time, sim, recipe):
    enough_ingredients = True
    # TODO: check if there are enough ingredients
    if enough_ingredients:
        sim.increment_accepted_order_count()
        print_time(time, 'Accepting order')
        # TODO: schedule events for each ingredient
    else:
        # TODO: handle case where there are not enough ingredients (and delete following line)
        pass

def setup_simulation(sim):
    sim.set_available_chef_count(2)
    sim.add_ingredient('burger', 10, 8)
    sim.add_ingredient('lettuce', 8, 2)
    sim.add_ingredient('tomato', 15, 2)
    sim.add_ingredient('bun', 20, 5)