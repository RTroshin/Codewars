def growing_plant(up_speed, down_speed, desired_height):
    days = 0
    height = 0
    
    while height < desired_height:
        days += 1
        height += up_speed
        height -= down_speed
    
    return days
