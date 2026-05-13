def ft_seed_inventory(seed: str, q: int, u: str) -> None:
    if (u == "packets"):
        print(seed.capitalize(), "seeds:", q, u, "available")
    elif (u == "grams"):
        print(seed.capitalize(), "seeds:", q, u, "total")
    elif (u == "area"):
        print(seed.capitalize(), "seeds:", "covers", q, "square meters")
    else:
        print(seed.capitalize(), "seeds:", q, "Unknown unit type")
