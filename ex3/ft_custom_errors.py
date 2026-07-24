#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 22:37:09 by horarivo            #+#    #+#            #
#   Updated: 2026/06/21 17:21:45 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown watering error"):
        super().__init__(message)


def water_plant(plant_name: str, amount: int) -> None:
    if plant_name == "":
        raise PlantError("Plant name cannot be empty!")
    if amount < 0:
        raise WaterError("Water amount cannot be negative!")
    if amount == 0:
        raise WaterError("Not enough water in the tank!")
    if amount > 50:
        raise WaterError("Overwatering! Max 50L per plant")
    print(f"Successfully watered {plant_name} with {amount}L")


def check_plant_health(plant_name: str, days_last_watered: int) -> None:
    if plant_name == "":
        raise PlantError("Plant name cannot be empty!")
    if days_last_watered < 0:
        raise GardenError("Invalid days value!")
    if days_last_watered > 7:
        raise PlantError(f"The {plant_name} plant is wilting!")
    print(f"{plant_name} is healthy (watered {days_last_watered} days ago)")


def test_custom_errors() -> None:
    print("\nTesting PlantError...")
    try:
        check_plant_health("tomato", 10)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        water_plant("lettuce", 0)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")

    try:
        check_plant_health("basil", 10)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        water_plant("carrot", 0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
