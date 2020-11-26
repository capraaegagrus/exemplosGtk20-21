import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk
import panelGrid


class ExemploGtkFlowBox(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo con Gtk.FlowBox")
        self.set_default_size(300, 200)
        self.set_border_width(10)

        cabeceira =Gtk.HeaderBar (title = "Exemplo con FlowBox")
        cabeceira.set_subtitle ("Aplicación demostrativa de FlowBox")
        cabeceira.props.show_close_button = True
        self.set_titlebar (cabeceira)

        scroll = Gtk.ScrolledWindow ()
        scroll.set_policy (Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        flowbox = Gtk.FlowBox ()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line (30)
        flowbox.set_selection_mode (Gtk.SelectionMode.NONE)
        scroll.add (flowbox)
        self.inicializaFlowbox (flowbox)

        self.add(scroll)

        self.connect ("destroy", Gtk.main_quit)
        self.show_all()




    def inicializaFlowbox (self, flowbox):
        n = 0
        """
        while n < 50:
            panel = panelGrid.Panel()
            flowbox.add (panel)
            n=n+1
        """
        for n in range (50):
            boton = Gtk.Button (label = str (n))
            flowbox.add (boton)

if __name__ == "__main__":
    ExemploGtkFlowBox()
    Gtk.main()