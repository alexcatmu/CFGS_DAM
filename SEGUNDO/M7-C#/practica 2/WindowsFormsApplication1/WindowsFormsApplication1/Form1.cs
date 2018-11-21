using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void cerrarToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void archivoToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void nueva_ventana()
        {
            textos a = new textos();
            a.MdiParent = this;

            a.Show();
        }

        private void eventos_archivo(object sender, EventArgs e)
        {
            switch (((ToolStripMenuItem)sender).Text) { 
            
                case "Nuevo":
                    nueva_ventana();
                    break;
            
            }
        }

        private void evento_editar(object sender, EventArgs e)
        {

        }

        private void evento_idioma(object sender, EventArgs e)
        {

        }

        private void evento_fuente(object sender, EventArgs e)
        {

        }

    }
}
