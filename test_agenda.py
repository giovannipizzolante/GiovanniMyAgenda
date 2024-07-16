import unittest
from agenda import Agenda, Event

class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()

    def test_add_event(self):
        # Test adding an event
        self.agenda.add_event("Meeting", "2024-07-16", "Meeting with the team")
        events = self.agenda.list_events()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].title, "Meeting")
        self.assertEqual(events[0].date, "2024-07-16")
        self.assertEqual(events[0].description, "Meeting with the team")

    def test_remove_event(self):
        # Test removing an event
        self.agenda.add_event("Meeting", "2024-07-16", "Meeting with the team")
        self.agenda.remove_event("Meeting")
        events = self.agenda.list_events()
        self.assertEqual(len(events), 0)

        # Test removing an event that does not exist
        self.agenda.add_event("Workshop", "2024-07-17", "Workshop on AI")
        self.agenda.remove_event("Nonexistent Event")
        events = self.agenda.list_events()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].title, "Workshop")

    def test_list_events(self):
        # Test listing events when no events are added
        events = self.agenda.list_events()
        self.assertEqual(events, [])

        # Test listing events when multiple events are added
        self.agenda.add_event("Meeting", "2024-07-16", "Meeting with the team")
        self.agenda.add_event("Workshop", "2024-07-17", "Workshop on AI")
        events = self.agenda.list_events()
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0].title, "Meeting")
        self.assertEqual(events[1].title, "Workshop")

if __name__ == "__main__":
    unittest.main()

