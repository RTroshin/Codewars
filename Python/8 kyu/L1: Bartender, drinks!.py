def get_drink_by_profession(param):
    return {"jabroni": "Patron Tequila",\
            "school counselor": "Anything with Alcohol",\
            "programmer": "Hipster Craft Beer",\
            "bike gang member": "Moonshine",\
            "politician": "Your tax dollars",\
            "rapper": "Cristal"}.get(param.lower(), "Beer")
