using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace alarma_ceshar
{
    class leerAlarmas
    {

        String nombreFichero;
        public leerAlarmas(String ruta_lectura) 
        {
            this.nombreFichero = ruta_lectura;
        }

        public List<string> hacerSelector()
        {
            List<string> array_final_selector = new List<string>();
            if (File.Exists(this.nombreFichero))
            {
                foreach (string line in File.ReadLines(this.nombreFichero))
                {
                    List<string> tiempo_alarma = line.Split('\t').ToList();
                    String hora = tiempo_alarma[0] + ":";
                    String minutos = tiempo_alarma[1] + ":";
                    String segundos = tiempo_alarma[2];

                    String lineaFinal = hora + minutos + segundos;
                    array_final_selector.Add(lineaFinal);
                }
            }
            return array_final_selector;
        }

        public List<string> leerArchivoReturn()
        {
            List<string> array_lineasArchivo = new List<string>();
            if (File.Exists(this.nombreFichero))
            {
                foreach (string line in File.ReadLines(this.nombreFichero))
                {
                    array_lineasArchivo.Add(line);
                }
            }
            return array_lineasArchivo;
        }

    }
}
