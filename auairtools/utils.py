class TimeStamp:
    def __init__(self, time_dict):
        self.year = time_dict['year']
        self.month = time_dict['month']
        self.day = time_dict['day']
        self.hour = time_dict['hour']
        self.mins = time_dict['min']
        self.sec  = time_dict['sec']
        self.ms   = time_dict['ms']
        print(self.year, self.ms)

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
