import datetime
import time
import winsound


class AlarmClock:

    def __init__(self):
        # List used to store alarms
        self.alarms = []

        # Snooze duration
        self.snooze_minutes = 5

        # Alarm ID
        self.next_id = 1

    # -----------------------------------------
    # ADD ALARM
    # -----------------------------------------
    def set_alarm(self):

        alarm_time = input(
            "\nEnter alarm time (HH:MM - 24 hour format): "
        )

        # Check correct time format
        try:
            datetime.datetime.strptime(alarm_time, "%H:%M")
        except ValueError:
            print("Invalid time format!")
            print("Please enter time like 07:30 or 18:45")
            return

        label = input("Enter alarm label: ")

        alarm = {
            "id": self.next_id,
            "time": alarm_time,
            "label": label,
            "status": "Active"
        }

        self.alarms.append(alarm)

        print("\nAlarm set successfully!")
        print("Alarm ID :", self.next_id)
        print("Time     :", alarm_time)
        print("Label    :", label)

        self.next_id += 1

    # -----------------------------------------
    # DISPLAY ALARMS
    # -----------------------------------------
    def display_alarms(self):

        if len(self.alarms) == 0:
            print("\nNo alarms set.")
            return

        print("\n========== ALARMS ==========")

        for alarm in self.alarms:

            print("ID     :", alarm["id"])
            print("Time   :", alarm["time"])
            print("Label  :", alarm["label"])
            print("Status :", alarm["status"])
            print("----------------------------")

    # -----------------------------------------
    # LINEAR SEARCH
    # -----------------------------------------
    def search_alarm(self, alarm_id):

        for alarm in self.alarms:

            if alarm["id"] == alarm_id:
                return alarm

        return None

    # -----------------------------------------
    # DELETE ALARM
    # -----------------------------------------
    def delete_alarm(self):

        try:
            alarm_id = int(input("\nEnter Alarm ID: "))

            alarm = self.search_alarm(alarm_id)

            if alarm is not None:

                self.alarms.remove(alarm)

                print("Alarm deleted successfully.")

            else:
                print("Alarm not found.")

        except ValueError:
            print("Please enter a valid ID.")

    # -----------------------------------------
    # RING ALARM
    # -----------------------------------------
    def ring_alarm(self, alarm):

        print("\n")
        print("================================")
        print("         🔔 ALARM RINGING 🔔")
        print("================================")
        print("Label :", alarm["label"])
        print("Time  :", alarm["time"])

        # Ring continuously until user chooses
        while True:

            # Windows alarm sound
            winsound.Beep(1000, 700)
            winsound.Beep(1200, 700)
            winsound.Beep(1000, 700)

            print("\n1. Stop Alarm")
            print("2. Snooze for 5 Minutes")

            choice = input("Enter choice: ")

            if choice == "1":

                alarm["status"] = "Completed"

                print("\nAlarm stopped.")
                break

            elif choice == "2":

                self.snooze(alarm)
                break

            else:

                print("Invalid choice.")

    # -----------------------------------------
    # SNOOZE
    # -----------------------------------------
    def snooze(self, alarm):

        current_time = datetime.datetime.now()

        snooze_time = current_time + datetime.timedelta(
            minutes=self.snooze_minutes
        )

        alarm["time"] = snooze_time.strftime("%H:%M")

        alarm["status"] = "Snoozed"

        print("\n😴 Alarm snoozed!")

        print(
            "Alarm will ring again at:",
            alarm["time"]
        )

    # -----------------------------------------
    # CHECK ALARMS
    # -----------------------------------------
    def check_alarms(self):

        current_time = datetime.datetime.now().strftime("%H:%M")

        for alarm in self.alarms:

            if alarm["time"] == current_time:

                if (
                    alarm["status"] == "Active"
                    or alarm["status"] == "Snoozed"
                ):

                    self.ring_alarm(alarm)

    # -----------------------------------------
    # START CLOCK
    # -----------------------------------------
    def start_clock(self):

        print("\n================================")
        print("       ALARM CLOCK STARTED")
        print("================================")
        print("Press Ctrl + C to stop clock.\n")

        try:

            last_checked_minute = ""

            while True:

                current_time_full = datetime.datetime.now()

                current_time = current_time_full.strftime(
                    "%H:%M:%S"
                )

                print(
                    "\rCurrent Time :",
                    current_time,
                    end=""
                )

                # Check only once per minute
                current_minute = current_time_full.strftime(
                    "%H:%M"
                )

                if current_minute != last_checked_minute:

                    self.check_alarms()

                    last_checked_minute = current_minute

                time.sleep(1)

        except KeyboardInterrupt:

            print("\n\nAlarm Clock stopped.")


# =========================================
# MAIN PROGRAM
# =========================================

clock = AlarmClock()

while True:

    print("\n")
    print("================================")
    print("        DIGITAL ALARM CLOCK")
    print("================================")
    print("1. Set Alarm")
    print("2. Display Alarms")
    print("3. Delete Alarm")
    print("4. Start Alarm Clock")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":

        clock.set_alarm()

    elif choice == "2":

        clock.display_alarms()

    elif choice == "3":

        clock.delete_alarm()

    elif choice == "4":

        clock.start_clock()

    elif choice == "5":

        print("\nThank you for using Digital Alarm Clock!")
        break

    else:

        print("\nInvalid choice!")