import sublime
import sublime_plugin
import subprocess

class FormatOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):
        path = view.file_name()
        if not path:
            return

        if path.endswith(".go"):
            subprocess.Popen(f"go fmt {path}", shell=True)
