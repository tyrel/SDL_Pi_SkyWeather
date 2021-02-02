import sqlite3
import time
import state

def log(level, message):
    with sqlite3.connect('/home/pi/data.db') as conn:
        cursor = conn.cursor()
        print("{}: {}".format(level, message))
        cursor.execute('INSERT INTO log (source, timestamp, level, message) VALUES (?, ?, ?, ?)', ('SkyWeather', int(round(time.time() * 1000)), level, message))
        conn.commit()

    
def insert_row(cursor, name, value, str_value = None):
    cursor.execute('INSERT INTO readings (sensor_name, timestamp, value, str_value) VALUES (?, ?, ?, ?)', (name, int(round(time.time() * 1000)), value, str_value))


def save_state():
    with sqlite3.connect('/home/pi/data.db') as conn:
        cursor = conn.cursor()

        if state.currentOutsideTemperature != 0.0:
            insert_row(cursor, 'weather_outside_temp', int(state.currentOutsideTemperature * 100))
        if state.currentOutsideHumidity != 1:
            insert_row(cursor, 'weather_outside_humidity', int(state.currentOutsideHumidity))
        if state.currentInsideTemperature != 0.0:
            insert_row(cursor, 'weather_inside_temp', int(state.currentInsideTemperature * 100))
        if state.currentInsideHumidity != 1:
            insert_row(cursor, 'weather_inside_humidity', int(state.currentInsideHumidity))

        conn.commit()


