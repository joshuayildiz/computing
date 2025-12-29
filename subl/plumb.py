import sublime
import sublime_plugin
import subprocess
import os
import re

class PlumbCommand(sublime_plugin.TextCommand):
    # Regex breakdown:
    # 1. Path: Letters, numbers, and common path symbols (._/-)
    # 2. Line/Col: Optional :digits:digits or just :digits
    PATH_REGEX = r'[a-zA-Z0-9\.\-_/]+(?::\d+){0,2}'

    def run(self, edit):
        for region in self.view.sel():
            target_text = ""

            if region.empty():
                # --- Expansion Logic ---
                # Find the boundaries of the "word" under the cursor using our path characters
                line_region = self.view.line(region)
                line_text = self.view.substr(line_region)
                
                # Calculate cursor position relative to the line
                pos_in_line = region.begin() - line_region.begin()
                
                # Find all potential matches in the line
                matches = re.finditer(self.PATH_REGEX, line_text)
                for m in matches:
                    if m.start() <= pos_in_line <= m.end():
                        target_text = m.group(0)
                        break
            else:
                # Use the manual selection
                target_text = self.view.substr(region).strip()

            if not target_text:
                continue

            self.execute_plumb(target_text)

    def execute_plumb(self, path_text):
        cwd = self.get_working_dir()
        subl_bin = "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl"

        try:
            # We use Popen so Sublime doesn't freeze
            subprocess.Popen(
                [subl_bin, path_text],
                cwd=cwd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True
            )
        except Exception as e:
            sublime.status_message(f"Plumb failed: {e}")

    def get_working_dir(self):
        if self.view.file_name():
            return os.path.dirname(self.view.file_name())
        folders = self.view.window().folders()
        return folders[0] if folders else os.path.expanduser("~")
