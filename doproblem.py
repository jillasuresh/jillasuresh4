while True:
    try:
        number1=int(input('Number1:'))
    except ValueError:
        print("")
        continue
    else:
        break
