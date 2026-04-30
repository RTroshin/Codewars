def growing_plant(up_speed, down_speed, desired_height):
    days = 0
    height = 0
    
    for i in range(0, desired_height, up_speed):
        days += 1
        height += up_speed
        
        if height >= desired_height:
            break
        
        height -= down_speed
    else:
        return 1
    
    return days
