import sublime
import sublime_plugin
import subprocess

class SwiftfmtCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = sublime.Region(0, self.view.size())
		content = self.view.substr(region)

		try:
			cfmt = subprocess.run(
				['swift', 'format', '-'],
				input=content.encode('utf-8'),
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE,
				check=True
			)

			formatted = cfmt.stdout.decode('utf-8')
			self.view.replace(edit, region, formatted)
		except subprocess.CalledProcessError as e:
			sublime.message_dialog(f"Error running swiftfmt:\n{e.stderr.decode('utf-8')}")

class SwiftfmtEventListener(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		# No file name, doesn't exist on disk, skip
		if not view.file_name():
			return

		# Not a go file, skip.
		if not view.file_name().endswith('.swift'):
			return

		# Call GofmtCommand.run
		view.run_command("swiftfmt")
