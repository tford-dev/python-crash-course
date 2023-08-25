import unittest;
from test_file_0 import get_formatted_name;

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('terry', 'stylez');
        self.assertEqual(formatted_name, 'Terry Stylez');
    
    def full_government_name(self):
        formatted_name = get_formatted_name('kanye', 'west', 'omari');
        self.assertEqual(formatted_name, "Kanye Omari West");
if __name__ == '__main__':
    unittest.main();