class TimeStamp:
    def __init__(self, time_dict):
        self.year = time_dict['year']
        self.month = time_dict['month']
        self.day = time_dict['day']
        self.hour = time_dict['hour']
        self.mins = time_dict['min']
        self.sec  = time_dict['sec']
        self.ms   = time_dict['ms']

    def __str__(self):
        time_dict = {'year': self.year,
            'month': self.month,
            'day': self.day,
            'hour': self.hour,
            'min': self.mins,
            'sec': self.sec,
            'ms': self.ms}

        return 'TimeStamp: ' + str(time_dict) 

    def __abs__(self):
        year_abs = abs(self.year) 
        month_abs = abs(self.month) 
        day_abs = abs(self.day) 
        hour_abs = abs(self.hour) 
        mins_abs = abs(self.mins) 
        sec_abs = abs(self.sec) 
        ms_abs = abs(self.ms)
        
        time_dict = {'year': year_abs,
            'month': month_abs,
            'day': day_abs,
            'hour': hour_abs,
            'min': mins_abs,
            'sec': sec_abs,
            'ms': ms_abs}

        return TimeStamp(time_dict)              


    def __lt__(self, otherTimeStamp):
        if self.year < otherTimeStamp.year:
            return True
        elif self.year < otherTimeStamp.year:
            return False
        else:
            if self.month < otherTimeStamp.month:
                return True
            elif self.month < otherTimeStamp.month:
                return False
            else:
                if self.day < otherTimeStamp.day:
                    return True
                elif self.day < otherTimeStamp.day:
                    return False
                else:
                    if self.hour < otherTimeStamp.hour:
                        return True
                    elif self.hour < otherTimeStamp.hour:
                        return False
                    else:
                        if self.mins < otherTimeStamp.mins:
                            return True
                        elif self.mins < otherTimeStamp.mins:
                            return False
                        else:  
                            if self.sec < otherTimeStamp.sec:
                                return True
                            elif self.sec < otherTimeStamp.sec:
                                return False
                            else:  
                                if self.ms < otherTimeStamp.ms:
                                    return True
                                elif self.ms < otherTimeStamp.ms:
                                    return False
                                else: return False      

    def __le__(self, otherTimeStamp):
        if self.year < otherTimeStamp.year:
            return True
        elif self.year > otherTimeStamp.year:
            return False
        else:
            if self.month < otherTimeStamp.month:
                return True
            elif self.month > otherTimeStamp.month:
                return False
            else:
                if self.day < otherTimeStamp.day:
                    return True
                elif self.day > otherTimeStamp.day:
                    return False
                else:
                    if self.hour < otherTimeStamp.hour:
                        return True
                    elif self.hour > otherTimeStamp.hour:
                        return False
                    else:
                        if self.mins < otherTimeStamp.mins:
                            return True
                        elif self.mins > otherTimeStamp.mins:
                            return False
                        else:  
                            if self.sec < otherTimeStamp.sec:
                                return True
                            elif self.sec > otherTimeStamp.sec:
                                return False
                            else:  
                                if self.ms < otherTimeStamp.ms:
                                    return True
                                elif self.ms > otherTimeStamp.ms:
                                    return False
                                else: return True                                                                                                                        


    def __gt__(self, otherTimeStamp):
        if self.year > otherTimeStamp.year:
            return True
        elif self.year > otherTimeStamp.year:
            return False
        else:
            if self.month > otherTimeStamp.month:
                return True
            elif self.month > otherTimeStamp.month:
                return False
            else:
                if self.day > otherTimeStamp.day:
                    return True
                elif self.day > otherTimeStamp.day:
                    return False
                else:
                    if self.hour > otherTimeStamp.hour:
                        return True
                    elif self.hour > otherTimeStamp.hour:
                        return False
                    else:
                        if self.mins > otherTimeStamp.mins:
                            return True
                        elif self.mins > otherTimeStamp.mins:
                            return False
                        else:  
                            if self.sec > otherTimeStamp.sec:
                                return True
                            elif self.sec > otherTimeStamp.sec:
                                return False
                            else:  
                                if self.ms > otherTimeStamp.ms:
                                    return True
                                elif self.ms > otherTimeStamp.ms:
                                    return False
                                else: return False 

    def __sub__(self, otherTimeStamp):
        year_diff = self.year - otherTimeStamp.year
        month_diff = self.month - otherTimeStamp.month
        day_diff = self.day - otherTimeStamp.day
        hour_diff = self.hour - otherTimeStamp.hour
        mins_diff = self.mins - otherTimeStamp.mins
        sec_diff = self.sec - otherTimeStamp.sec
        ms_diff = self.ms - otherTimeStamp.ms
        
        time_dict = {'year': year_diff,
            'month': month_diff,
            'day': day_diff,
            'hour': hour_diff,
            'min': mins_diff,
            'sec': sec_diff,
            'ms': ms_diff}

        return TimeStamp(time_dict)    


        