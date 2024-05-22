def main():
    CutPart = [135, 150, 178]  # Target lengths to be achieved (cm)
    CutModel = [1500, 1000, 800]   # Lengths of sponge pieces that can be used (cm)
    resultindex = 0


    for index in range(len(CutModel)):
        for x in range(int(CutPart[0])):  # Amount of trim
            for a in range(100):  # Tries the number of 135 cm pieces of sponge
                for b in range(100):  # Tries the number of 150 cm pieces of sponge
                    for c in range(100):  # Tries the number of 178 cm pieces of sponge
                        if 150 * a + 100 * b + 80 * c == CutModel[index] - x:
                            resultindex += 1
                            print(f"{resultindex}) amount of 150cm = {a}, amount of 100 cm = {b}, amount of 80 cm = {c} Trim={x} cm for the model {CutModel[index]} cm")
                            break

main()


