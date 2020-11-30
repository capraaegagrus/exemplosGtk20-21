import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk
import panelGrid


class FilaListBoxConDatos (Gtk.ListBoxRow):
    def __init__(self, palabra):
        super(Gtk.ListBoxRow, self).__init__()
        self.palabra = palabra
        #self.etiqueta = Gtk.Label(label=palabra)
        self.add (Gtk.Label (label=palabra))


class ExemploGtkListBox(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo con Gtk.ListBox")
        self.set_border_width (10)

        caixaExterna = Gtk.Box (orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add (caixaExterna)

        listBox = Gtk.ListBox()
        listBox.set_selection_mode (Gtk.SelectionMode.NONE)
        caixaExterna.pack_start(listBox, True, True, 0)

        row = Gtk.ListBoxRow ()
        caixaH = Gtk.Box (orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(caixaH)
        caixaV = Gtk.Box (orientation=Gtk.Orientation.VERTICAL)
        caixaH.pack_start(caixaV, True, True, 0)

        etiqueta1 = Gtk.Label (label="Data é hora automática", xalign=0)
        etiqueta2 = Gtk.Label (label="Require acceso a interrede", xalign=0)
        caixaV.pack_start(etiqueta1, True, True, 0)
        caixaV.pack_start (etiqueta2, True, True, 0)

        interruptor  = Gtk.Switch ()
        interruptor.props.valign = Gtk.Align.CENTER
        caixaH.pack_start (interruptor, False, True, 0)

        listBox.add(row)

        fila = Gtk.ListBoxRow()
        caixaH = Gtk.Box (orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila.add(caixaH)
        etiqueta3 = Gtk.Label (label="Palabra a filtrar", xalign=0)
        combo = Gtk.ComboBoxText()
        palabras = "Estes é un ListBox mal ordeado".split()
        n = 0
        for palabra in palabras:
            combo.insert (n, str(n), palabra)
            n=+n
        combo.connect ("changed", self.on_combo_changed)

        caixaH.pack_start (etiqueta3, True, True, 0)
        caixaH.pack_start (combo, False, True, 0)

        listBox.add(fila)

        listBox2 = Gtk.ListBox()

        for palabra in palabras:
            listBox2.add(FilaListBoxConDatos(palabra))

        def func_ordea ( fila1, fila2, data, notify_destroy):
            return fila1.palabra.lower() > fila2.palabra.lower()

        def func_filtrado (fila, data, notify_destroy):
            return False if fila.palabra.lower() =="mal" else True

        listBox2.set_sort_func (func_ordea, None, False)
        listBox2.set_filter_func (func_filtrado, None, False)

        listBox2.connect ("row-activated", self.on_fila_activada)
        caixaExterna.pack_start (listBox2, True, True, 0)
        listBox2.show_all()

        self.connect ("destroy", Gtk.main_quit)
        self.show_all()


    def on_fila_activada(self, controlListBox, fila):
        print (fila.palabra)

    def on_combo_changed (self, control, datos):
        """Por rematar"""


if __name__ == "__main__":
    ExemploGtkListBox()
    Gtk.main()