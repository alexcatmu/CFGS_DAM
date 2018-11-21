using System;
using System.IO;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Media;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using WMPLib;


namespace alarma_ceshar
{
    public partial class Form1 : Form
    {
        public int actual_hora;
        public int actual_min;
        public int actual_sec;

        public String rutaSong;

        public Form1()
        {
            InitializeComponent();
            OpenFileDialog openFileDialog1 = new OpenFileDialog();


            if (openFileDialog1.ShowDialog(this) == DialogResult.OK)
            {
                rutaSong = openFileDialog1.InitialDirectory + openFileDialog1.FileName;
            }


            IniciarHorarios();
            fechaActual fa_inst = new fechaActual();
            lb_dia.Text = fa_inst.fecha_actual;

            SelectAlarmas();

        }

        private void IniciarHorarios()
        {

            cb_hora.Items.Clear();
            cb_minutos.Items.Clear();
            cb_segundos.Items.Clear();


            for (int i = 0; i <= 23; i++)
            {
                cb_hora.Items.Add(i);
            }
            for (int i = 0; i <= 59; i++)
            {
                cb_minutos.Items.Add(i);
            }
            for (int i = 0; i <= 59; i++)
            {
                cb_segundos.Items.Add(i);
            }
        }

        private void SelectAlarmas()
        {
            leerAlarmas alarmasActivas = new leerAlarmas("Alarma_activa.txt");
            List<string> listaActivas = alarmasActivas.hacerSelector();
            cb_alarmas_activas.Items.Clear();


            foreach (string linea in listaActivas)
            {
                cb_alarmas_activas.Items.Add(linea);
            }

            cb_alarmas_inactivas.Items.Clear();

            leerAlarmas alarmasInactivas = new leerAlarmas("Alarma_inactiva.txt");
            List<string> listaInactivas = alarmasInactivas.hacerSelector();
            foreach (string linea in listaInactivas)
            {
                cb_alarmas_inactivas.Items.Add(linea);
            }
        }

        private void Time_Tick(object sender, EventArgs e)
        {
            lb_hora.Text = DateTime.Now.ToLongTimeString();
            this.actual_hora = DateTime.Now.Hour;
            this.actual_min = DateTime.Now.Minute;
            this.actual_sec = DateTime.Now.Second;

            foreach (String lineas in cb_alarmas_activas.Items)
            {
                List<string> tiempo_alarma = lineas.Split(':').ToList();
                int hora = Convert.ToInt32(tiempo_alarma[0]);
                int minutos = Convert.ToInt32(tiempo_alarma[1]);
                int segundos = Convert.ToInt32(tiempo_alarma[2]);
                if (hora == actual_hora && minutos == actual_min && segundos == actual_sec) 
                {
                    WMPLib.WindowsMediaPlayer wplayer = new WMPLib.WindowsMediaPlayer();
                    wplayer.URL = this.rutaSong;
                    wplayer.controls.play();
                }
                
            }
            
        }

        private void bt_anadir_Click(object sender, EventArgs e)
        {
            String hora = Convert.ToString(cb_hora.SelectedItem);
            String min = Convert.ToString(cb_minutos.SelectedItem);
            String sec = Convert.ToString(cb_segundos.SelectedItem);

            if (hora.Length < 2) {
                hora = "0" + hora;
            }

            if (min.Length < 2) {
                min = "0" + min;
            }

            if (sec.Length < 2) {
                sec = "0" + sec;
            }

            GuardaAlarma Ga = new GuardaAlarma(hora, min, sec);
            Ga.EscribeFichero("Alarma_activa.txt");

            SelectAlarmas();
            IniciarHorarios();

        }

        private void bt_activaToInactiva_Click(object sender, EventArgs e)
        {
            String AlarmaCambiar = Convert.ToString(cb_alarmas_activas.SelectedItem);
            String ArchivoOrigen = "Alarma_activa.txt";
            String ArchivoDestino = "Alarma_inactiva.txt";
            ConvertActivaInactiva(AlarmaCambiar, ArchivoOrigen, ArchivoDestino);
        }

        private void ConvertActivaInactiva(String alarmaCambiar, String ArchivoOrigen, String ArchivoDestino)
        {
            //
            //Cambiar de un lado hacia el otro 
            //
            List<string> tiempo_alarma = alarmaCambiar.Split(':').ToList();
            String hora = tiempo_alarma[0];
            String minutos = tiempo_alarma[1];
            String segundos = tiempo_alarma[2];

            GuardaAlarma save = new GuardaAlarma(hora, minutos, segundos);
            save.EscribeFichero(ArchivoDestino);

            leerAlarmas leerOrigen = new leerAlarmas(ArchivoOrigen);
            List<string> ListaOrigen = leerOrigen.leerArchivoReturn();

            List<string> ListaFinal = new List<string>();

            GuardaAlarma del = new GuardaAlarma(ArchivoOrigen);
            del.DeleteFile();

            GuardaAlarma ReEscribir = new GuardaAlarma(ArchivoOrigen);
            alarmaCambiar = alarmaCambiar.Replace(":", "\t");
            foreach (string line in ListaOrigen) 
            {
                if (line != alarmaCambiar)
                {
                    ReEscribir.ReEscribe(line);
                }
            }

            SelectAlarmas();

        }

    }
}
