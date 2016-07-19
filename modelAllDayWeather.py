class AllDayWeather:
    """A class defining an all_day_weather characterized by :
    - its day date
    - its day name
    - its month date
    - its month name
    - its year date
    
    - its max temperature
    - its min temperature
    
    - its short description
    - its icon url
    
    - its max wind speed
    - its max wind direction
    - its average wind speed
    - its average wind direction
    
    - its max humidity
    - its min humidity
    - its average humidity"""

    
    def __init__(self, day_date, day_name, month_date, month_name, year_date, max_temp, min_temp, description, icon_url, max_wind_speed, max_wind_dir, ave_wind_speed, ave_wind_dir, max_hum, min_hum, ave_hum):
        """Constructor"""
        self.day_date = day_date
        self.day_name = day_name
        self.month_date = month_date
        self.month_name = month_name
        self.year_date = year_date
        
        self.max_temp = max_temp
        self.min_temp = min_temp
        
        self.description = description
        self.icon_url = icon_url
        
        self.max_wind_speed = max_wind_speed
        self.max_wind_dir = max_wind_dir
        self.ave_wind_speed = ave_wind_speed
        self.ave_wind_dir = ave_wind_dir
        
        self.max_hum = max_hum
        self.min_hum = min_hum
        self.ave_hum = ave_hum
