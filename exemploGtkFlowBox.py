import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk


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

    def on_draw (self, area, cr, obxColor):
        contexto = area.get_style_context()
        ancho = area.get_allocated_width()
        alto = area.get_allocated_height()
        Gtk.render_background (contexto, cr, 0,0, ancho, alto)

        r, g, b, a = obxColor ["color"]
        cr.set_source_rgba (r, g, b, a)
        cr.rectangle (0, 0, ancho, alto)
        cr.fill()

    def novo_boton_color (self, cadea_color):
        rgba = Gdk.RGBA()
        rgba.parse (cadea_color)

        boton = Gtk.Button ()

        area = Gtk.DrawingArea ()
        area.set_size_request (24,24)
        area.connect ("draw",self.on_draw, {"color": rgba})

        boton.add(area)
        return boton


    def inicializaFlowbox (self, flowbox):
        colores = [ "AliceBlue",
            "AntiqueWhite",
            "AntiqueWhite1",
            "AntiqueWhite2",
            "AntiqueWhite3",
            "AntiqueWhite4",
            "aqua",
            "aquamarine",
            "aquamarine1",
            "aquamarine2",
            "aquamarine3",
            "aquamarine4",
            "azure",
            "azure1",
            "azure2",
            "azure3",
            "azure4",
            "beige",
            "bisque",
            "bisque1",
            "bisque2",
            "bisque3",
            "bisque4",
            "black",
            "BlanchedAlmond",
            "blue",
            "blue1",
            "blue2",
            "blue3",
            "blue4",
            "BlueViolet",
            "brown",
            "brown1",
            "brown2",
            "brown3",
            "brown4",
            "burlywood",
            "burlywood1",
            "burlywood2",
            "burlywood3",
            "burlywood4",
            "CadetBlue",
            "CadetBlue1",
            "CadetBlue2",
            "CadetBlue3",
            "CadetBlue4",
            "chartreuse",
            "chartreuse1",
            "chartreuse2",
            "chartreuse3",
            "chartreuse4",
            "chocolate",
            "chocolate1",
            "chocolate2",
            "chocolate3",
            "chocolate4",
            "coral",
            "coral1",
            "coral2",
            "coral3",
            "coral4"
        ]
        for color in colores:
            boton = self.novo_boton_color (color)
            flowbox.add (boton)



if __name__ == "__main__":
    ExemploGtkFlowBox()
    Gtk.main()