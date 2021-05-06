from dice import Dice


def main():
    dice = Dice()
    rolls_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    simulation_number = int(input('Cuantas simulaciones se ejecturan: '))
    roll_number = int(input('Cuantos veces se tirará el dado: '))

    simulations = []
    for _ in range(simulation_number):
        rolls = []
        for _ in range(roll_number):
            result = dice.roll(True)
            rolls.append(result)

        simulations.append(rolls)

    for rolls in simulations:
        for key, value in rolls_count.items():
            if key in rolls:
                rolls_count[key] += 1

    for key, value in rolls_count.items():
        probability = round(value / simulation_number, 4) * 100
        print(f'La probabilida de obtener al menos un {key} en {roll_number} tiro/os es: {probability}%')


if __name__ == '__main__':
    main()
