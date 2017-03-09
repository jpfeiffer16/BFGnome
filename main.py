from bf import bf
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
import sys
import os

class Handler:
    def on_delete_window(self, *args):
        Gtk.main_quit(*args)
    def on_btn_run_clicked(self, button):
        code_text = code_buffer.get_text(code_buffer.get_start_iter(), code_buffer.get_end_iter(), False)
        input_text = txt_input.get_text()
        lbl_output.set_text(bf(code_text, input_text).run())

EXEC_FOLDER = os.path.dirname(os.path.realpath(__file__)) + "/"
builder = Gtk.Builder()
builder.add_from_file(EXEC_FOLDER + "ui.glade")
builder.connect_signals(Handler())
txt_input = builder.get_object("txt_input")
txt_code = builder.get_object("txt_code")
code_buffer = builder.get_object("code_buffer")
lbl_output = builder.get_object("lbl_output")
main_window = builder.get_object("main_window")

main_window.show_all()
Gtk.main()