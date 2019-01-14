def restaurant_ratings(filename):
    file = open(filename)
    ratings = {}
    for line in file:
        line = line.rstrip()
        restaurant_info = line.split(':')
        for rating in restaurant_info:
            ratings[restaurant_info[0]] = restaurant_info[1]

    sorted_restaurant_ratings = sorted(ratings.items())
    for restaurant, restaurant_ratings in sorted_restaurant_ratings:
        print(f'{restaurant} is rated at {restaurant_ratings}.')


restaurant_ratings('scores.txt')