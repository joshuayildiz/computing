import sublime
import sublime_plugin
import re

class AlignCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel(
            "Align by (Leave blank for all columns):", 
            "", 
            self.on_done, 
            None, 
            None
        )

    def on_done(self, user_input):
        self.view.run_command("execute_align", {"substring": user_input})

class ExecuteAlignCommand(sublime_plugin.TextCommand):
    def run(self, edit, substring):
        for region in self.view.sel():
            if region.empty(): continue
            
            lines_regions = self.view.split_by_newlines(region)
            line_texts = [self.view.substr(r) for r in lines_regions]
            
            if substring:
                # MODE 1: Align by specific character (First occurrence)
                max_pos = max((text.find(substring) for text in line_texts), default=-1)
                if max_pos == -1: continue

                for i in range(len(lines_regions) - 1, -1, -1):
                    content = line_texts[i]
                    pos = content.find(substring)
                    if pos != -1 and pos < max_pos:
                        self.view.insert(edit, lines_regions[i].begin() + pos, " " * (max_pos - pos))
            else:
                # MODE 2: Align "Stuff" (Multiple columns via whitespace)
                # Split lines into words
                rows = [re.split(r'(\s+)', text.strip()) for text in line_texts]
                # Filter out the empty splits and keep only (text, gap) pairs
                cleaned_rows = []
                for row in rows:
                    # Filter to keep only actual content or the spaces between them
                    cleaned_rows.append([item for item in row if item.strip() or item])

                # Find max width for each "content" column
                max_widths = {}
                for row in cleaned_rows:
                    for i, part in enumerate(row):
                        if part.strip(): # It's a word
                            column_index = i // 2
                            max_widths[column_index] = max(max_widths.get(column_index, 0), len(part))

                # Reconstruct lines
                for i in range(len(lines_regions) - 1, -1, -1):
                    new_line = ""
                    row = cleaned_rows[i]
                    for j, part in enumerate(row):
                        if part.strip(): # It's a word
                            col_idx = j // 2
                            # Pad the word to the max width of that column
                            # unless it's the last word in the line
                            if j < len(row) - 1:
                                new_line += part.ljust(max_widths[col_idx])
                            else:
                                new_line += part
                        else: # It's an existing gap, we'll normalize it to 1 space
                            new_line += " " 
                    
                    self.view.replace(edit, lines_regions[i], new_line)