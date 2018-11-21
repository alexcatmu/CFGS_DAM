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

        Double resultado = 0.0f;
        Double numero = 0.0f;
        bool borrar = false;
        string operador = "";
        bool primer_operador = true;
        string texto_acumulado = "";




        protected override bool ProcessCmdKey(ref Message msg, Keys keyData)
        {
            switch(keyData){
                case Keys.D0:
                    bt_0.PerformClick();
                 break;
                case Keys.D1:
                 bt_1.PerformClick();
                 break;
                case Keys.D2:
                 bt_2.PerformClick();
                 break;
                case Keys.D3:
                 bt_3.PerformClick();
                 break;
                case Keys.D4:
                 bt_4.PerformClick();
                 break;
                case Keys.D5:
                 bt_5.PerformClick();
                 break;
                case Keys.D6:
                 bt_6.PerformClick();
                 break;
                case Keys.D7:
                 bt_7.PerformClick();
                 break;
                case Keys.D8:
                 bt_8.PerformClick();
                 break;
                case Keys.D9:
                 bt_9.PerformClick();
                 break;
                /*case Keys.Subtract:
                 bt_resta.PerformClick();
                 break;
                case Keys.Multiply:
                 bt_0.PerformClick();
                 break;
                case Keys.Divide:
                 bt_0.PerformClick();
                 break;
                case Keys:
                 bt_0.PerformClick();
                 break;*/
            }

            return base.ProcessCmdKey(ref msg, keyData);
        }




        private void bt_numerico(object sender, EventArgs e)
        {
            if (borrar == true) {
                txt_resultado.Text = "";
                this.borrar = false;
            }

            txt_resultado.Text += ((Button)sender).Text;
            this.numero = Convert.ToDouble(txt_resultado.Text);
        }

        private void boton_igual() {
            switch (this.operador) { 
                case "+":
                    if (this.primer_operador == true)
                    {
                        this.resultado = this.numero;
                        this.primer_operador = false;
                    }
                    else
                    {
                        this.resultado += this.numero;
                        this.numero = 0.0;
                    }
                    break;

                case "-":
                    if (this.primer_operador == true)
                    {
                        this.resultado = this.numero;
                        this.primer_operador = false;
                    }
                    else
                    {
                        this.resultado = this.resultado - this.numero;
                        this.numero = 0.0;
                    }
                    break;

                case "*":
                    if (this.primer_operador == true)
                    {
                        this.resultado = this.numero;
                        this.primer_operador = false;
                    }
                    else
                    {
                        this.resultado =this.resultado * this.numero;
                        this.numero = 0.0;
                    }
                    break;

                case "/":
                    if (this.primer_operador == true)
                    {
                        this.resultado = this.numero;
                        this.primer_operador = false;
                    }
                    else
                    {
                        this.resultado = this.resultado / this.numero;
                        this.numero = 0.0;
                    }
                    break;

                case "%":
                    if (this.primer_operador == true)
                    {
                        this.resultado = this.numero;
                        this.primer_operador = false;
                    }
                    else
                    {
                        this.resultado = this.resultado % this.numero;
                        this.numero = 0.0;
                    }
                    break;

                case "^":
                    if (this.primer_operador == true)
                    {
                        this.resultado = this.numero;
                        this.primer_operador = false;
                    }
                    else
                    {
                        this.resultado = Math.Pow(this.resultado, this.numero);
                        this.numero = 0.0;
                    }
                    break;
            }
            txt_resultado.Text = Convert.ToString(this.resultado);
            text_acumulado.Text += Convert.ToString(this.resultado);
        }
        

        private void bt_oper_basic(object sender, EventArgs e)
        {
            txt_resultado.Text = "";
            if (this.operador == "=")
            {
                text_acumulado.Text += ((Button)sender).Text;
            }
            else {
                text_acumulado.Text += Convert.ToString(this.numero) + ((Button)sender).Text;
            }

            if (((Button)sender).Text == "=") {
                boton_igual();
            }



            if (this.primer_operador == true)
            {
                this.resultado = this.numero;
                this.operador = ((Button)sender).Text;
            }
            if (((Button)sender).Text != "=")
            {
                switch (this.operador)
                {
                    case "+":
                        if (this.primer_operador == true)
                        {
                            this.resultado = this.numero;
                            this.primer_operador = false;
                        }
                        else
                        {
                            this.resultado += this.numero;
                            this.numero = 0.0;
                        }
                        break;

                    case "-":
                        if (this.primer_operador == true)
                        {
                            this.resultado = this.numero;
                            this.primer_operador = false;
                        }
                        else
                        {
                            this.resultado = this.resultado - this.numero;
                            this.numero = 0.0;
                        }
                        break;

                    case "*":
                        if (this.primer_operador == true)
                        {
                            this.resultado = this.numero;
                            this.primer_operador = false;
                        }
                        else
                        {
                            this.resultado = this.resultado * this.numero;
                            this.numero = 0.0;
                        }
                        break;

                    case "/":
                        if (this.primer_operador == true)
                        {
                            this.resultado = this.numero;
                            this.primer_operador = false;
                        }
                        else
                        {
                            this.resultado = this.resultado / this.numero;
                            this.numero = 0.0;
                        }
                        break;

                    case "%":
                        if (this.primer_operador == true)
                        {
                            this.resultado = this.numero;
                            this.primer_operador = false;
                        }
                        else
                        {
                            this.resultado = this.resultado % this.numero;
                            this.numero = 0.0;
                        }
                        break;

                    case "^":
                        if (this.primer_operador == true)
                        {
                            this.resultado = this.numero;
                            this.primer_operador = false;
                        }
                        else
                        {
                            this.resultado = Math.Pow(this.resultado, this.numero);
                            this.numero = 0.0;
                        }
                        break;
                }
            }
            txt_resultado.Text = Convert.ToString(this.resultado);
            

            this.operador = ((Button)sender).Text;
            this.borrar = true;
        }


        private void bt_reiniciar(object sender, EventArgs e)
        {
            this.resultado = 0.0f;
            this.numero = 0.0f;
            this.borrar = false;
            txt_resultado.Text = "";
            this.texto_acumulado = "";
            this.primer_operador = true;
            text_acumulado.Text = "";
            this.operador = "";
        }


        private void bt_complejos_click(object sender, EventArgs e)
        {
            text_acumulado.Text += ((Button)sender).Text;
            switch (((Button)sender).Text) { 
                case "log":
                    if (this.primer_operador == true)
                    {
                        this.resultado = Math.Log(this.numero);
                        this.primer_operador = false;
                    }
                    else
                    {
                        this.resultado += Math.Log(this.numero);
                        this.numero = this.resultado;
                    }
                    break;

                break;

                case "sen":

                    if (this.primer_operador == true)
                    {
                        this.resultado = Math.Sin(this.numero);
                        this.primer_operador = false;
                    }
                    else
                    {
                        this.resultado += Math.Sin(this.numero);
                        this.numero = this.resultado;
                    }
                break;

                case "cos":

                    if (this.primer_operador == true)
                    {
                        this.resultado = Math.Cos(this.numero);
                        this.primer_operador = false;
                    }
                    else
                    {
                        this.resultado += Math.Cos(this.numero);
                        this.numero = this.resultado;
                    }
                break;

                case "tan":

                    if (this.primer_operador == true)
                    {
                        this.resultado = Math.Tan(this.numero);
                        this.primer_operador = false;
                    }
                    else
                    {
                        this.resultado += Math.Tan(this.numero);
                        this.numero = this.resultado;
                    }
                break;

                case "sqrt":

                    if (this.primer_operador == true)
                    {
                        this.resultado = Math.Sqrt(this.numero);
                        this.primer_operador = false;
                    }
                    else
                    {
                        this.resultado += Math.Sqrt(this.numero);
                        this.numero = this.resultado;
                    }
                break;
            }

            txt_resultado.Text = Convert.ToString(this.resultado);
            this.operador = ((Button)sender).Text;
            this.borrar = true;

        }

        private void txt_resultado_KeyDown(object sender, KeyEventArgs e)
        {

        }

        private void txt_resultado_Click(object sender, EventArgs e)
        {
            
        }

        private void add_coma(object sender, EventArgs e)
        {
            txt_resultado.Text += ",";
        }




    }
}
