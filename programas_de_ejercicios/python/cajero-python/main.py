from persistencia.manejador import Manejador

from persistencia.dao.cuentaDao import DaoCuenta
from persistencia.dao.personaDao import DaoPersona

from servicios.cuentaServicio import ServicioCuenta
from servicios.personaServicio import ServicioPersona

from presentacion.controladores.cuentaControlador import ControladorCuenta
from presentacion.controladores.personaControlador import ControladorPersona

from presentacion.vistas.ventanaPrincipal import VentanaPrincipal

class App(object):
  def __init__(self):
    pass

  def main(self):
    m = Manejador()
    conexion = m.getConexion()
    with conexion as c:

      m.crearTablas(c)

      personas = m.getRows(c,"personas")
      cuentas = m.getRows(c,"cuentas")

      if not personas and not cuentas:
        m.hazQuery(conexion,"INSERT INTO cuentas('id','fecha_fin','cvv','saldo','nip') VALUES('1234-1234-1234-1111','07/19','765',0.00,'1111')")
        m.hazQuery(conexion,"INSERT INTO personas('curp','nombre','apat','amat','id_cuenta') VALUES('RELA960813HDFBPN08','Angel','Rebollo','Lopez','1234-1234-1234-1111')")
        m.guardarCambios(c)

      daoCuenta = DaoCuenta(m)
      daoPersona = DaoPersona(m)
      servicioPersona = ServicioPersona(daoPersona)
      servicioCuenta = ServicioCuenta(daoCuenta)
      ctrlCuenta = ControladorCuenta(servicioCuenta,servicioPersona)

      VentanaPrincipal(ctrlCuenta)

app = App()
app.main()
