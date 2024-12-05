import krpc
import matplotlib.pyplot as plt
import time as t

# Подключение к серверу kRPC
conn = krpc.connect('orbit_data')

# Получение объекта космического корабля
vessel = conn.space_center.active_vessel

# Создание массивов для данных о времени и высоте
time_values = []
altitude_values = []
time = 0

# Получение высоты корабля на протяжении полета
while True:
    # Получение текущей высоты
    altitude = vessel.flight().surface_altitude
    velocity = vessel.flight(vessel.orbit.body.reference_frame).speed
    print(velocity)
    time_values.append(time)  # Запись текущего времени в массив
    altitude_values.append(altitude)  # Запись текущей высоты в массив

    t.sleep(1)
    time += 1
    # Проверка условия завершения сбора данных
    if altitude > 150000:  # Остановка считывания данных при наборе высоты 160км
        break

    # Построение графика скорости от времени
plt.plot(time_values, altitude_values)
plt.title('Изменение высоты от времени (KSP)')
plt.xlabel('Время, секунды')
plt.ylabel('Высота, метры')
plt.show()
