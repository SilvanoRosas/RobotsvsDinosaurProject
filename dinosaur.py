class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.health = 100
        self.energy = 150
        self.attack_power = attack_power
        self.attack_type = ('Claw', 'Bite', 'Slash')


    def attack_robot(self, robot_to_attack):
        if self.energy > 10:
            while True:
                try:
                    attack_choice = int(input(f'Choose attack type: (1) {self.attack_type[0]}, (2) {self.attack_type[1]}, or (3) {self.attack_type[2]}.'))
                except ValueError:
                    continue
                if attack_choice == 1:
                    print(f'{self.type} attacked {robot_to_attack.name} with {self.attack_type[0]}')
                    break
                elif attack_choice == 2:
                    print(f'{self.type} attacked {robot_to_attack.name} with {self.attack_type[1]}')
                    break
                elif attack_choice == 3:
                    print(f'{self.type} attacked {robot_to_attack.name} with {self.attack_type[2]}')
                    break

            self.energy -= 10
            robot_to_attack.health -= self.attack_power
            print(f'{self.type} energy is now {self.energy}')
            print(f'{robot_to_attack.name} health is now {robot_to_attack.health}')


############ OLD - KEEP FOR QUICK TESTING ##########
        # if self.energy > 10:
        #     print(f'{self.type} attacked {robot_to_attack.name}')
        #     self.energy -= 10
        #     robot_to_attack.health -= self.attack_power
        #     print(f'{self.type} energy is now {self.energy}')
        #     print(f'{robot_to_attack.name} health is now {robot_to_attack.health}')