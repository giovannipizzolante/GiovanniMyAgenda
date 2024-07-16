class Event:
    def __init__(self, title, date, description):
        self.title = title
        self.date = date
        self.description = description

    def __str__(self):
        return f"Title: {self.title}\nDate: {self.date}\nDescription: {self.description}"


class Agenda:
    def __init__(self):
        self.events = []

    def add_event(self, title, date, description):
        event = Event(title, date, description)
        self.events.append(event)

    def remove_event(self, title):
        for event in self.events:
            if event.title == title:
                self.events.remove(event)
                print(f"Event '{title}' removed.")
                return
        print(f"Event '{title}' not found.")

    def list_events(self):
        if not self.events:
            print("No events in the agenda.")
        else:
            for event in self.events:
                print(event)
        return self.events

if __name__ == "__main__":
    agenda = Agenda()
    print(
        """
     _____      _ _           _                                _       
    |  __ \    | (_)         (_)     /\                       | |      
    | |__) |__ | |_ _ __ ___  _     /  \   __ _  ___ _ __   __| | __ _ 
    |  ___/ _ \| | | '_ ` _ \| |   / /\ \ / _` |/ _ \ '_ \ / _` |/ _` |
    | |  | (_) | | | | | | | | |  / ____ \ (_| |  __/ | | | (_| | (_| |
    |_|   \___/|_|_|_| |_| |_|_| /_/    \_\__, |\___|_| |_|\__,_|\__,_|
                                          __/ |                       
                                         |___/                        
    
    Welcome to the Polimi Agenda Application!
    """
    )
    while True:
        print("\nMenu:")
        print("1. Add Event")
        print("2. Remove Event")
        print("3. List Events")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter event title: ")
            date = input("Enter event date: ")
            description = input("Enter event description: ")
            agenda.add_event(title, date, description)
            print("Event added successfully.")
        elif choice == "2":
            title = input("Enter event title to remove: ")
            agenda.remove_event(title)
        elif choice == "3":
            agenda.list_events()
        elif choice == "4":
            print("Exiting the Polimi Agenda Application. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")