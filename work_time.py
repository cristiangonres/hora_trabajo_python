from datetime import time, datetime
import time
hora_salida = '19:00:00'
hora_salida_time = datetime.strptime(hora_salida, '%H:%M:%S')

while 1 == 1:
    now_str = datetime.now().time().strftime("%H:%M:%S")
    now = datetime.now()
    hora_actual = now.hour
    print(hora_actual)
    minuto_actual = now.minute
    segundo_actual = now.second
    tiempo_actual = datetime.time(now.hour , now.minute, now.second)
    hora_salida = datetime.time(19 , 00, 00)
    
    date_dif = hora_salida - tiempo_actual
    
    
    
    print(date_dif)
    
    print (f'le falta para salir {now}')
    time.sleep(10)