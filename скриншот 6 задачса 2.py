my_car = {'first_one': 'we can do it'}
def biggest_dict(**kwargs):
    my_car.update(**kwargs)
biggest_dict(name='никита', age=13, weight=190, eyes_color='red')
print(my_car)
