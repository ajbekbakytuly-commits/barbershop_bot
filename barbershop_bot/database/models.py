from datetime import datetime

class Appointment:

    def __init__(self, user_id, master_id, service_id, date, time):
        self.user_id = user_id
        self.master_id = master_id
        self.service_id = service_id
        self.date = date
        self.time = time
        self.status = "active"

    def to_tuple(self):
        return (
            self.user_id,
            self.master_id,
            self.service_id,
            self.date,
            self.time,
            self.status
        )