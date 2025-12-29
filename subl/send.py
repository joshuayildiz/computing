import sublime
import sublime_plugin
import subprocess
import os

class SendCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cwd = self.get_working_dir()

        for region in reversed(self.view.sel()):
            # Acme behavior: if no selection, use the current line
            if region.empty():
                region = self.view.line(region)

            cmd = self.view.substr(region).strip()
            if not cmd:
                continue

            try:
                # Use a login shell to ensure your .zshrc/.bash_profile PATH is loaded
                # We use stderr=subprocess.STDOUT to merge the streams
                process = subprocess.Popen(
                    cmd,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    cwd=cwd,
                    text=True,
                    env=os.environ.copy()
                )

                # communicate() now returns stdout and stderr merged into one string
                output, _ = process.communicate()

                if output:
                    # Ensure it ends with a newline for clean buffer insertion
                    if not output.endswith('\n'):
                        output += '\n'
                    self.view.replace(edit, region, output)

            except Exception as e:
                # Fallback: write the Python exception to the buffer
                self.view.replace(edit, region, f"Error: {str(e)}\n")

    def get_working_dir(self):
        if self.view.file_name():
            return os.path.dirname(self.view.file_name())
        folders = self.view.window().folders()
        return folders[0] if folders else os.path.expanduser("~")
