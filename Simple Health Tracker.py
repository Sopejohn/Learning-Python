"""
Created on Sun Jan  28 08:14:57 2024

@author: mosope
"""

class HealthTracker:
    def __init__(self):
        self.water_intake = 0
        self.sleep_duration = 0

    def track_water_intake(self, liters):
        try:
            liters = float(liters)
            if liters > 0:
                self.water_intake += liters
                print(f"Water intake tracked: {liters} liters")
            else:
                print("Invalid amount. Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for water intake.")

    def track_sleep_duration(self, length):
        try:
            length = float(length)
            if length >= 0:
                self.sleep_duration += length
                print(f"Sleep duration tracked: {length} hours")
            else:
                print("Invalid duration. Please enter a non-negative value.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for sleep duration.")

    def display_summary(self):
        print("\nHealth Summary:")
        print(f"Water Intake: {self.water_intake} liters")
        print(f"Sleep Duration: {self.sleep_duration} hours")

def main():
    health_tracker = HealthTracker()

    print("Welcome to the Health Tracker!")
    print("Track - track your health metrics")
    print("Summary - display health summary")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "track":
            metric = input("Enter the health metric (water/sleep): ").lower()
            if metric == "water":
                amount = input("Enter the amount of water in liters: ")
                health_tracker.track_water_intake(amount)
            elif metric == "sleep":
                duration = input("Enter the sleep duration in hours: ")
                health_tracker.track_sleep_duration(duration)
            else:
                print("Invalid health metric. Supported metrics: water, sleep.")
        elif command == "summary":
            health_tracker.display_summary()
        else:
            print("Command not recognized!")

if __name__ == "__main__":
    main()
