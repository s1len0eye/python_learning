def make_car(manufacturer, name, **others):
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model_name'] = name
    
    for key, value in others.items():
        profile[key] = value
        
    return profile

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
