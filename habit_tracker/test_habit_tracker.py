import subprocess
import sys
import unittest
from pathlib import Path


class HabitTrackerTests(unittest.TestCase):
    def test_import_does_not_block(self):
        project_dir = Path(__file__).resolve().parent
        script = f"""
import sys
sys.path.insert(0, r'{project_dir}')
import habit_tracker
print('imported')
"""

        result = subprocess.run(
            [sys.executable, "-c", script],
            capture_output=True,
            text=True,
            timeout=3,
            cwd=project_dir,
        )

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("imported", result.stdout)


if __name__ == "__main__":
    unittest.main()
