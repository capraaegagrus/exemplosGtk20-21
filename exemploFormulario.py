import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk



class ExemploFormulario(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo de formulario con Gtk")
        self.set_default_size(300, 200)
        self.set_border_width(10)

        caixaV = Gtk.Box (orientation=Gtk.Orientation.VERTICAL, spacing = 6)
        etiqueta = Gtk.Label(label="Información sobre o producto2")
        #etiqueta.set_justify()
        cadro1 = Gtk.Frame (label = "Datos básicos")
        cadro2 = Gtk.Frame (label = "Datos económicos")
        self.add(caixaV)
        caixaV.pack_start(etiqueta,False, False, 2)
        caixaV.pack_start(cadro1,True,True,20)
        caixaV.pack_start(cadro2,True,True,20)

        caixaV2 = Gtk.Box (orientation=Gtk.Orientation.VERTICAL, spacing = 6)
        cadro1.add(caixaV2)
        lblNome = Gtk.Label (label = "Nome")
        txtNome = Gtk.Entry()
        lblDescripcion = Gtk.Label (label="Descripción")
        txvDescripcion = Gtk.TextView()
        caixaH = Gtk.Box (spacing = 2)
        chkContador = Gtk.CheckButton(label = "Engadir contador de visitas")
        caixaV2.pack_start (lblNome, False, False, 2)
        caixaV2.pack_start(txtNome, True, False, 2)
        caixaV2.pack_start(lblDescripcion, False, False, 2)
        caixaV2.pack_start(txvDescripcion, True, True, 2)
        caixaV2.pack_start(caixaH, True, True, 10)
        caixaV2.pack_start(chkContador, False, False, 2)

        lblFoto = Gtk.Label (label="Foto")
        txtFoto = Gtk.Entry()
        btnElixirFoto = Gtk.Button (label="Elixir...")
        caixaH.pack_start (lblFoto, False, False,2)
        caixaH.pack_start (txtFoto, False, False, 2)
        caixaH.pack_start(btnElixirFoto, False, False, 2)

        caixaV3 = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        cadro2.add(caixaV3)
        caixaH3 = Gtk.Box (spacing = 6)
        lblPromocion = Gtk.Label ("Promoción")
        rbtNingun = Gtk.RadioButton(label = "Ningún")
        rbtTransporte = Gtk.RadioButton(label = "Transporte gratuito")
        rbtDesconto = Gtk.RadioButton(label = "Desconto 5%")
        caixaV3.pack_start (caixaH3, False, False,2)
        caixaV3.pack_start(lblPromocion, False, False, 2)
        caixaV3.pack_start(rbtNingun, False, False, 2)
        caixaV3.pack_start(rbtTransporte, False, False, 2)
        caixaV3.pack_start(rbtDesconto, False, False, 2)

        lblPrezo = Gtk.Label (label="Prezo")
        txtPrezo = Gtk.Entry ()
        lblEuro = Gtk.Label (label="€")
        lblImpostos = Gtk.Label (label="Impostos")
        cmbImpostos = Gtk.ComboBoxText()
        cmbImpostos.append_text("4%")
        cmbImpostos.append_text("7%")
        cmbImpostos.append_text("14%")
        caixaH3.pack_start (lblPrezo, False, False,2)
        caixaH3.pack_start(txtPrezo, False, False, 2)
        caixaH3.pack_start(lblEuro, False, False, 2)
        caixaH3.pack_start(lblImpostos, False, False, 2)
        caixaH3.pack_start(cmbImpostos, False, False, 2)





        self.connect ("destroy", Gtk.main_quit)
        self.show_all()



if __name__ == "__main__":
    ExemploFormulario()
    Gtk.main()