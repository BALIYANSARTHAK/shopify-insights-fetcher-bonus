def find_competitors(brand_name: str):
    static_mapping = {
        "memy": ["hairoriginals.com", "beardo.in", "bombayshavingcompany.com"],
        "colourpop": ["nyxcosmetics.com", "maccosmetics.com"]
    }
    key = brand_name.lower()
    return static_mapping.get(key, [])