from modelos.cuenta import Cuenta

class DaoCuenta(object):

  def __init__(self,manejador):
    self.manejador = manejador

  def getCuentaByNip(self, nip):
    for c in self.manejador.getRows(self.manejador.getConexion(),"cuentas"):
      if c[4] == nip:
        return Cuenta(c[0],c[1],c[2],c[3],c[4])
    return None

  def getCuentaById(self,id):
    for c in self.manejador.getRows(self.manejador.getConexion(),"cuentas"):
      if c[0] == id:
        return Cuenta(c[0],c[1],c[2],c[3],c[4])
    return None

  def updateCuenta(self, cuenta):
    query = """
      UPDATE cuentas
      SET
      fecha_fin = ?,
      cvv = ?,
      saldo = ?,
      nip = ?
      WHERE id = ?;
    """
    params = (cuenta.getFechaFin(), cuenta.getCvv(), cuenta.getSaldo(), cuenta.getNip(), cuenta.getId())
    self.manejador.hazQuery(self.manejador.getConexion(),query,params)
    return True
