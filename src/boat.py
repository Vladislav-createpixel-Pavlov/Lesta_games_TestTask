class RowingBoat:
    def __init__(self, max_passengers=4, max_load=500):
        self.max_passengers = max_passengers
        self.current_passengers = 0
        self.is_floating = True
        self.speed = 0
        self.direction = 'north'
    
    def load_passenger(self, passenger_weight):
        if self.current_passengers >= self.max_passengers or not self.is_floating:
            return False
        else:
            self.current_passengers += 1
            return True
        
    def row_forward(self, distance_in_meters):
        if self.is_floating and self.current_passengers > 0:
            print(f'Лодка проплыла {distance_in_meters} метров.')
            return True
        else:
            print('Нельзя двигаться вперёд без пассажиров или находясь на суше.')
            return False
            
    def change_direction(self, new_direction):
        valid_directions = ['north', 'south', 'east', 'west']
        if new_direction in valid_directions:
            self.direction = new_direction
            return True
        else:
            print('Неверное направление')
            return False
        
    def check_status(self):
        return {
            'is_floating': self.is_floating,
            'current_passengers': self.current_passengers,
            'speed': self.speed,
            'direction': self.direction

        }
