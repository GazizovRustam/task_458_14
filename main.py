def main():
    with open('GasPrices.txt', 'r') as gasFile:
        descr = gasFile.readlines()
    for ch in descr:
        print(ch.strip('\n'))


if __name__ == "__main__":
    main()