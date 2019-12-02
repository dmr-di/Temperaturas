__autor__='danimr'

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import funciones

class Conversor:
    def __init__(self):
        #iniciamos la libreria Gtk
        b = Gtk.Builder()
        b.add_from_file('ventana.glade')
        # cargamos los widgets con algún evento asociado o que son referenciados
        self.vprincipal = b.get_object('vPrincipal')
        self.lblresult = b.get_object('lblResult')
        self.btnsalir = b.get_object('btnSalir')
        self.btncalcular = b.get_object('btnCalcular')
        self.cmbt1 = b.get_object('cmbT1')
        self.cmbt2 = b.get_object('cmbT2')
        self.enttemp = b.get_object('entTemp')

        # diccionario de eventos
        dic = {'on_vPrincipal_destroy': self.salir, 'on_btnSalir_clicked': self.salir, 'on_btnCalcula_clicked': self.calcular, }

        # conectamostodo y mostramos
        b.connect_signals(dic)
        self.vprincipal.show()

    # ahora codificamos las funciones
    def salir(self, widget):
        Gtk.main_quit()
    def calcular(self, widget):
        try:
            self.select1 = self.cmbt1.get_active_text()
            self.select2 = self.cmbt2.get_active_text()
            if self.select1 == 'Celsius' and self.select2 == 'Fahrenheit':
                self.var = funciones.celtofah(self.enttemp.get_text())
                self.lblresult.set_text(self.var)
            if self.select1 == 'Celsius' and self.select2 == 'Kelvin':
                self.var = funciones.celtokel(self.enttemp.get_text())
                self.lblresult.set_text(self.var)
        except:
            self.lblresult.set_text('algún error')

if __name__ == '__main__':
    main = Conversor()
    Gtk.main()
