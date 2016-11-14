"""
A simple spell-checking application.  Used for illustrating a Trie
class.

Author: Nathan Sprague
Version: 11/2014
"""
import tkinter as tk
import trie
import re
import time

# Globals to control layout:
TEXT_WIDTH = 80
TEXT_HEIGHT = 24
INFO_WIDTH = 60


class SpellChecker(tk.Frame):
    """ This class represents the visible Spell Checking Frame widget. """


    def __init__(self, parent, dictionary_file):
        """ Create the necessary widgets and pack them into the frame. """

        tk.Frame.__init__(self, parent)
        self.dictionary = trie.Trie()
        self._read_dictionary(dictionary_file)
        parent.title("CS240 Spell Checker")

        self.text = tk.Text(self, height=TEXT_HEIGHT, width=TEXT_WIDTH,
                            wrap=tk.WORD)
        self.text.grid(row=0, column=0, columnspan=2)

        self.button = tk.Button(self, text="Check Spelling")
        self.button.grid(row=1, column=0)
        self.button.bind('<ButtonPress>', self._button_callback)

        self.info_text = tk.StringVar()
        self.info_label = tk.Label(self, textvariable=self.info_text,
                                   width=INFO_WIDTH)
        self.info_label.grid(row=1, column=1, sticky='E')

        self.pack()

    def _read_dictionary(self, dict_loc):
        """
        Build the Trie from a dictionary file. The file should have
        one word per line.
        """
        with open(dict_loc, 'r') as f:
            for line in f:
                self.dictionary.insert(line.lower().rstrip())

    def _button_callback(self, *args):
        """ This method will be called on button presses. """

        # Clear any tags from previous spell checking.
        self.text.tag_remove("s", "0.0", "end")

        # Find the number of lines in the text box.
        last_line = int(self.text.index("end-1c").split(".")[0])

        word_count = 0
        error_count = 0
        start_time = time.perf_counter()

        # A regular expression that should match words.
        rgx = re.compile("([a-zA-Z][a-zA-Z']*[a-zA-Z])|([a-zA-Z])")

        # Loop through all lines...
        for line_num in range(last_line + 1):

            # Extract the current line
            cur_line = self.text.get(str(line_num) + ".0",
                                     str(line_num) + ".end")

            # Check each word in the current line.  Tag if misspelled.
            for match in re.finditer(rgx, cur_line):
                word_count += 1
                if match.group().lower() not in self.dictionary:
                    error_count += 1
                    self.text.tag_add("s",
                                      "{}.{}".format(line_num, match.start()),
                                      "{}.{}".format(line_num, match.end()))

        # Set the tag color to red on yellow.
        self.text.tag_config("s", foreground="red", background="yellow")

        # Display an informational string.
        total_time = time.perf_counter() - start_time
        result_str = "Words checked: {}.  Total Time: {:.4f}s.  Errors: {}"
        self.info_text.set(result_str.format(word_count, total_time,
                                             error_count))

if __name__ == "__main__":
    root = tk.Tk()
    sc = SpellChecker(root, 'american-english.txt')
    root.mainloop()
