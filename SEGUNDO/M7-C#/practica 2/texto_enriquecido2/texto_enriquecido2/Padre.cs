using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace texto_enriquecido2
{
    public partial class Padre : Form
    {
        private Hijos formulario_hijo;
        public Padre()
        {
            InitializeComponent();
        }

        private void nuevoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Hijos nuevo_hijo = new Hijos();
            nuevo_hijo.MdiParent = this;
            nuevo_hijo.Show();

        }
    }
}
