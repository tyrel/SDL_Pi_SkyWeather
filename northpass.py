import sqlite3
import time
import state
import sys

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
        try:
            cursor = conn.cursor()

            if state.currentOutsideTemperature != 0.0:
                insert_row(cursor, 'weather_outside_temp', int(state.currentOutsideTemperature * 100))
            if state.currentOutsideHumidity != 1:
                insert_row(cursor, 'weather_outside_humidity', int(state.currentOutsideHumidity * 100))
            if state.currentInsideTemperature != 0.0:
                insert_row(cursor, 'weather_inside_temp', int(state.currentInsideTemperature * 100))
            if state.currentInsideHumidity != 1:
                insert_row(cursor, 'weather_inside_humidity', int(state.currentInsideHumidity * 100))

            insert_row(cursor, 'weather_rain_hour', int(state.currentRain60Minutes * 100))

            insert_row(cursor, 'weather_sunlight_visible', int(state.currentSunlightVisible * 100))
            insert_row(cursor, 'weather_sunlight_ir', int(state.currentSunlightIR * 100))
            insert_row(cursor, 'weather_sunlight_uv', int(state.currentSunlightUV * 100))
            insert_row(cursor, 'weather_sunlight_uvindex', int(state.currentSunlightUVIndex * 100))

            insert_row(cursor, 'weather_wind_speed', int(state.ScurrentWindSpeed * 100))
            insert_row(cursor, 'weather_wind_gust', int(state.ScurrentWindGust * 100))
            insert_row(cursor, 'weather_wind_direction', int(state.ScurrentWindDirection * 100))

            insert_row(cursor, 'weather_total_rain', int(state.currentTotalRain * 100))
        
            insert_row(cursor, 'weather_pressure', int(state.currentBarometricPressure * 100))
            insert_row(cursor, 'weather_altitude', int(state.currentAltitude * 100))
            insert_row(cursor, 'weather_sealevel', int(state.currentSeaLevel * 100))
        
            insert_row(cursor, 'weather_indoor_air_quality', int(state.Indoor_AirQuality_Sensor_Value * 100))
            insert_row(cursor, 'weather_outdoor_air_quality', int(state.Outdoor_AirQuality_Sensor_Value * 100))
            insert_row(cursor, 'weather_daily_outdoor_aq', int(state.Hour24_Outdoor_AirQuality_Sensor_Value * 100))

            # TODO lightning

            conn.commit()
        except:
            e = sys.exc_info()[0]
            print("Exception saving state to SQLite database: %s" % e)


