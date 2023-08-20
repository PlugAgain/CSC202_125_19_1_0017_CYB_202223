import math

class LectureRoom:
    def __init__(self, material, attenuation):
        self.material = material
        self.attenuation = attenuation
    
    def calculate_sound_intensity(self, power, distance):
        return power / (4 * math.pi * distance ** 2)
    
    def calculate_sound_level(self, intensity):
        return 10 * math.log10(intensity / 10 ** -12)
    
    def simulate_sound_penetration(self, power, distance):
        intensity = self.calculate_sound_intensity(power, distance)
        attenuated_intensity = intensity * (10 ** (-self.attenuation * distance))
        sound_level = self.calculate_sound_level(attenuated_intensity)
        print(sound_level)
        return sound_level

def main_in_room():
    # Room materials and their attenuations
    room_materials = {
        'acoustic foam': 0.01,
        'fiberglass insulation': 0.03,
        'double glazed windows': 0.06,
        'triple glazed windows': 0.09
    }

    HUMAN_HEARING_THRESHOLD = 140 # in decibels

    # Input parameters
    lawnmower_power = float(input("Enter lawnmower power in watts: "))
    material = input("Enter the room material: ")
    distance = float(input("Enter your distance from the lawnmower in meters: "))

    # Check if the entered material is valid
    if material not in room_materials:
        print("Invalid room material.")
        return
    
    # Create the room object
    room = LectureRoom(material, room_materials[material])

    # Simulate sound penetration
    sound_level = math.ceil(room.simulate_sound_penetration(lawnmower_power, distance))

    # Check if sound level exceeds hearing threshold or distance threshold
    if sound_level > HUMAN_HEARING_THRESHOLD:
        print(f"The sound level reaching you in the {material} room is {sound_level}. You can't hear anything, the noise is too much.")
    else:
        print(f"The sound level reaching you in the {material} room is {sound_level}. You can hear, the noise is not much.")

# usage
main_in_room()
