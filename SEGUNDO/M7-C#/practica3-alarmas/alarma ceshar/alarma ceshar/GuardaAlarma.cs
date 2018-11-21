using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace alarma_ceshar
{
    class GuardaAlarma
    {
        public String hora;
        public String minuto;
        public String segundo;
        public String ruta;

        public GuardaAlarma(String hora_c, String minuto_c, String segundo_c) 
        {
            this.hora = hora_c;
            this.minuto = minuto_c;
            this.segundo = segundo_c;

        }

        public GuardaAlarma(String ruta_c)
        {
            this.ruta = ruta_c;

        }

        public void DeleteFile()
        {
            File.Delete(this.ruta);
        }

        public void ReEscribe(String Linea)
        {
            StreamWriter w = File.AppendText(this.ruta);
            w.WriteLine(Linea);
            w.Close();
        }

        public void EscribeFichero(String ruta)
        {
            StreamWriter w = File.AppendText(ruta);
            String hora_s = Convert.ToString(this.hora);
            String minuto_s = Convert.ToString(this.minuto);
            String segundo_s = Convert.ToString(this.segundo);
            String cadenaFinal = hora_s + "\t" + minuto_s + "\t" + segundo_s;
            w.WriteLine(cadenaFinal);
            w.Close();
        }
    }
}
