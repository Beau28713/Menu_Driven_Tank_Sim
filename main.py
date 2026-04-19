def set_level(level, log):
    try:
        new_level = float(input("Enter new tank level (0-100): "))
        if 0 <= new_level <= 100:
            level[0] = new_level
            log.append(f"Set tank level to {level[0]}%")
            print(f"Tank level set to {level[0]}%")
        else:
            print("Level must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def start_pump(pump_on, log):
    if not pump_on[0]:
        pump_on[0] = True
        log.append("Pump started")
        print("Pump started.")
    else:
        print("Pump is already on.")

def stop_pump(pump_on, log):
    if pump_on[0]:
        pump_on[0] = False
        log.append("Pump stopped")
        print("Pump stopped.")
    else:
        print("Pump is already off.")

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
    else:
        print("No alarms.")

def save_log(log):
    with open("tank_log.txt", "w") as f:
        for entry in log:
            f.write(entry + "\n")
    print("Log saved to tank_log.txt")

def simulate(level, pump_on, log):
    if pump_on[0]:
        level[0] = min(100, level[0] + 5)
        log.append(f"Level increased to {level[0]}%")
    else:
        level[0] = max(0, level[0] - 1)
        log.append(f"Level decreased to {level[0]}%")

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
        print("5. Save log")
        print("6. Exit")
        print(f"Current level: {level[0]}%, Pump: {'On' if pump_on[0] else 'Off'}")

        choice = input("Choose an option: ").strip()
        if choice == '1':
            set_level(level, log)
        elif choice == '2':
            start_pump(pump_on, log)
        elif choice == '3':
            stop_pump(pump_on, log)
        elif choice == '4':
            view_alarms(level)
        elif choice == '5':
            save_log(log)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        # Simulate time step
        simulate(level, pump_on, log)

if __name__ == "__main__":
    main()