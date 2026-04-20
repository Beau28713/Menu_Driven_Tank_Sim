import csv
import os

def set_level(level):
    try:
        new_level = float(input("Enter new tank level (0-100): "))
        if 0 <= new_level <= 100:
            level[0] = new_level
            print(f"Tank level set to {level[0]}%")
        else:
            print("Level must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return level[0]

def start_pump(pump_on):
    if not pump_on[0]:
        pump_on[0] = True
        print("Pump started.")
    else:
        print("Pump is already on.")
    return pump_on[0]

def stop_pump(pump_on):
    if pump_on[0]:
        pump_on[0] = False
        print("Pump stopped.")
    else:
        print("Pump is already off.")
    return pump_on[0]

def view_alarms(level):
    alarms = []
    if level[0] < 10:
        alarms.append("Low level alarm")
        
    if level[0] > 90:
        alarms.append("High level alarm")
        
    if alarms:
        print("Alarms:")
        for alarm in alarms:
            print(f"- {alarm}")
        return alarms
    else:
        print("No alarms.")
        return "No Alarms"

def save_log(log):
    filename = "tank_log.csv"
    file_exists = os.path.isfile(filename)
    with open(filename, "a", newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Level %", "Alarm", "Pump State"])
        for entry in log:
            writer.writerows([entry])
    print("Log saved to tank_log.csv")

def simulate(level, pump_on):
    if pump_on[0]:
        level[0] = min(100, level[0] + 5)
    else:
        level[0] = max(0, level[0] - 1)

def main():
    level = [50.0]
    pump_on = [False]    
    log = []
    
    
    while True:
        print("\nTank Simulator Menu:")
        print("1. Set tank level")
        print("2. Start pump")
        print("3. Stop pump")
        print("4. View alarms")
        print("5. Run simulation step")
        print("6. Exit")
        print(f"Current level: {level[0]}%, Pump: {'On' if pump_on[0] else 'Off'}")

        choice = input("Choose an option: ").strip()
        if choice == '1':
            set_level(level)
        elif choice == '2':
            start_pump(pump_on)
        elif choice == '3':
            stop_pump(pump_on)
        elif choice == '4':
            active_alarm = view_alarms(level)
        elif choice == '5':
            pass
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            
        log = [((level[0], active_alarm if 'active_alarm' in locals() else "No Alarms", 'On' if pump_on[0] else 'Off'))]
        print(log)
        save_log(log)

        # Simulate time step
        simulate(level, pump_on,)

if __name__ == "__main__":
    main()