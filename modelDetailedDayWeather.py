class DetailedDayWeather:
    """A class defining an all_day_weather characterized by :
    - its day icon url
    - its day title
    - its day description
    
    - its evening icon url
    - its evening title
    - its evening description"""

    
    def __init__(self, day_icon_url, day_title, day_description, eve_icon_url, eve_title, eve_description):
        """Constructor"""
        self.day_icon_url = day_icon_url
        self.day_title = day_title
        self.day_description = day_description
        
        self.eve_icon_url = eve_icon_url
        self.eve_title = eve_title
        self.eve_description = eve_description
