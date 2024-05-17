import bpy
import math

class Body:
    def __init__(self,name, mass, initial_velocity = [0,0], position = [0,0]) -> None:
        self.mass = mass
        self.velocity = initial_velocity
        self.pos = position
        self.name = name

    def move(self):
        self.pos[0] += self.velocity[0] 
        self.pos[1] += self.velocity[1]

class SolarSystem:
    def __init__(self) -> None:
        self.bodies = []

    def add_body(self, body):

        self.bodies.append(body)

    def remove_body(self, body):
       self.bodies.remove(body)

    def update_all(self):
        for body in self.bodies:
            body.move()
        return(self.bodies)
            

    
    @staticmethod
    def accelerate_due_to_gravity(first,second, distance, angle):
        G_const = 0.6673
        force = first.mass * second.mass / (distance ** 2) * G_const
        reverse = -1
        for body in first, second:
            acceleration = force / body.mass

            acc_x = acceleration * math.cos(math.radians(angle))
            acc_y = acceleration * math.sin(math.radians(angle))

            body.velocity = (body.velocity[0] + (reverse * acc_x),body.velocity[1] + (reverse * acc_y),)
            reverse = 1

            # if body == first: 
            #     print(angle, acc_x, acc_y, body.velocity)

    def check_collision(self, first, second, distance):
        if distance <= 0:
            if first.mass <= second.mass:
                self.remove_body(first)
            if first.mass >= second.mass:
                self.remove_body(second)

    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:

                distancex = second.pos[0] - first.pos[0] 
                distancey = second.pos[1] - first.pos[1]
                distance = math.sqrt(distancex**2 + distancey **2)

                if distancex == 0 and distancey > 0:
                    angle = 270
                elif distancex == 0 and distancey < 0:
                    angle = 90            
                else:
                    angle = math.degrees((math.atan(distancey/distancex)))
                                
                if distancex < 0 and distancey > 0:
                    angle += 360 
                if distancex > 0 and distancey > 0:
                    angle += 180
                if distancex > 0 and distancey < 0:
                    angle += 180
                # print(distancex, distancey, angle, math.cos(math.radians(angle)), math.sin(math.radians(angle)))

                self.accelerate_due_to_gravity(first, second, distance=distance, angle=angle)
                self.check_collision(first, second, distance=distance)

def main():
    
    global ss
    ss = SolarSystem()
    sun = Body(name = 'sun', mass = 20000, initial_velocity=[0,0], position=[0,0])
    mercury = Body(name = 'mercury', mass = 1, initial_velocity=(0, 8), position=[94,0])
    venus = Body(name = 'venus', mass = 2, initial_velocity=(0.5, -7), position=[214,0])
    earth = Body(name = 'earth', mass = 7, initial_velocity=(2, 7), position=[294,0])
    mars = Body(name = 'mars', mass = 3, initial_velocity=(0.7, -5), position=[412,0])
    saturn = Body(name = 'saturn', mass = 7, initial_velocity=(3.7, -5.4), position=[654,0])
    jupiter = Body(name = 'jupiter', mass = 10, initial_velocity=(6.7, -7), position=[847,0])
    neptune = Body(name = 'neptune', mass = 9, initial_velocity=(7.7, -6), position=[1132,0])
    uranus = Body(name = 'uranus', mass = 8, initial_velocity=(9.7, -9), position=[1429,0])
    
    ss.add_body(sun)
    ss.add_body(mercury)
    ss.add_body(venus)
    ss.add_body(earth)
    ss.add_body(mars)
    ss.add_body(saturn)
    ss.add_body(jupiter)
    ss.add_body(neptune)
    ss.add_body(uranus)

if __name__ == "__main__":
    main()
    

# Blender code starts here

frames = 500

solsys = bpy.data.collections[1].objects

for i in range (frames):
    
    ss.calculate_all_body_interactions()
    bodies = ss.update_all()

    solarray = bodies.copy()
    index = 0
    
    for j in solsys:
        
        x = solarray[index].pos[0] # index = solsys.index(j)
        y = solarray[index].pos[1]
        
        # To change location
        j.location[0] = x
        j.location[1] = y
        
        index = index + 1
    
        # Insert keyframe
        j.keyframe_insert(data_path = "location", frame = i)