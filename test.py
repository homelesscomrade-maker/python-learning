while True: 
    try:
        find = int(input("Номер комнаты: "))   
    except ValueError:
        print("Введите число")
        continue
    if find % 20 != 0:
        entrance = find // 20 + 1
        print(f"Номер подъезда: {entrance}")
    else:
        entrance = find // 20
        print(f"Номер подъезда: {entrance}")
    if find % 4 == 0:
        floor = (find - (entrance - 1) * 20) // 4
    else:
        floor = (find - (entrance - 1) * 20) // 4 + 1
    print(f"Этаж: {floor}")
