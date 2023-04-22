class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory
    
    def make_computations(self):
        return self.__cpu * self.__memory

    def __str__(self):
        return f"Computer (CPU: {self.__cpu}, Memory: {self.__memory})"

    def __eq__(self, other):
        if isinstance(other, Computer):
            return self.__memory == other.get_memory()

        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Computer):
            return self.__memory < other.get_memory()

        return False

    def __le__(self, other):
        if isinstance(other, Computer):
            return self.__memory <= other.get_memory()

        return False

    def __gt__(self, other):
        if isinstance(other, Computer):
            return self.__memory > other.get_memory()

        return False

    def __ge__(self, other):
        if isinstance(other, Computer):
            return self.__memory >= other.get_memory()

        return False

class Phone:
    def __init__(self):
        self.__sim_cards_list = []

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        for sim_card in self.__sim_cards_list:
            if sim_card["number"] == sim_card_number:
                print(f"Идет звонок на номер {call_to_number} с сим-карты {sim_card['operator']}")
                break

    def __str__(self):
        return f"Phone (Sim cards: {self.__sim_cards_list})"

class SmartPhone(Computer, Phone):
    def use_gps(self, location):
        print(f"Маршрут до {location} проложен")

    def __str__(self):
        return f"SmartPhone (CPU: {self.get_cpu()}, Memory: {self.get_memory()}, Sim cards: {self.get_sim_cards_list()})"

computer = Computer(cpu=3.5, memory=8)
phone = Phone()
phone.set_sim_cards_list([{"number": 1, "operator": "Beeline"}, {"number": 2, "operator": "Megacom"}])
smartphone1 = SmartPhone(cpu=2.5, memory=4)
smartphone1.set_sim_cards_list([{"number": 1, "operator": "Beeline"}, {"number": 3, "operator": "O!"}])
smartphone2 = SmartPhone(cpu=3.2, memory=6)
smartphone2.set_sim_cards_list([{"number": 2, "operator": "Megacom"}, {"number": 4, "operator": "Line"}])
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# ---------------------------------------------------------------------------------------------------

print(computer.make_computations())
phone.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Bishkek City")
print(computer == smartphone2)
print(computer > smartphone2)

