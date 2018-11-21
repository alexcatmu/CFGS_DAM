using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace eventos_de_formulario
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        
        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            MessageBox.Show("Tecla pulsada en textbox1 keydown");
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            MessageBox.Show("Tecla pulsada en form1 keydown");
        }
        /*
       protected override bool ProcessCmdKey(ref Message msg, Keys keyData)
       {

           if (keyData == (Keys.F))
           {
               MessageBox.Show("Tecla en formulario F");
           }
           else {
               MessageBox.Show("Tecla de formulario");
           }
            
           return base.ProcessCmdKey(ref msg, keyData);
       }* */
    }
         
}
