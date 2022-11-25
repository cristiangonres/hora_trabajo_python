from datetime import time, datetime
import time

while 1 == 1:
    now_str = datetime.now().time().strftime("%H:%M:%S")
    now = datetime.now()
    hora_actual = now.hour
    print(hora_actual)
    minuto_actual = now.minute
    segundo_actual = now.second
    if hora_actual >= 19:
        print('Es hora de irse a casa')
    else:
        print (f'Son las:  {now_str}, te falta {18-hora_actual} HORAS, {59-minuto_actual} MINUTOS, {59-segundo_actual} SEGUNDOS para salir')
    time.sleep(10)