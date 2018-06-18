def print_time(time, msg):
    print(time, msg, sep=': ')

# TODO: add new functions below this line

def handle_new_ingredient(time, sim, ingredient):
    if sim.get_available_chef_count() > 0:
        sim.assign_chef()
        print_time(time, "Starting to prep " + ingredient)
        sim.schedule_event(time + sim.get_prep_time(ingredient), free_chef, ingredient)
    else:
        sim.schedule_event(time + 1, handle_new_ingredient, ingredient)

def free_chef(time, sim, ingredient):
    print_time(time, "Done prepping " + ingredient)
    sim.dismiss_chef()

# TODO: add new functions above this line


def handle_new_order(time, sim, recipe):
    enough_ingredients = True
    # TODO: check if there are enough ingredients
    for ingredient in recipe:
        if sim.get_count(ingredient) <= 0:
            enough_ingredients = False

    if enough_ingredients:
        sim.increment_accepted_order_count()
        print_time(time, 'Accepting order')
        # TODO: schedule events for each ingredient
        count = sim.get_available_chef_count()
        for ingredient in recipe:
            if count > 0:
                sim.schedule_event(time, handle_new_ingredient, ingredient)
                count -= 1
            else:
                sim.schedule_event(time+1, handle_new_ingredient, ingredient)

    else:
        # TODO: handle case where there are not enough ingredients (and delete following line)
        sim.increment_rejected_order_count()
        print_time(time, 'Rejecting order')

def setup_simulation(sim):
    sim.set_available_chef_count(2)
    sim.add_ingredient('burger', 10, 8)
    sim.add_ingredient('lettuce', 8, 2)
    sim.add_ingredient('tomato', 15, 2)
    sim.add_ingredient('bun', 20, 5)
