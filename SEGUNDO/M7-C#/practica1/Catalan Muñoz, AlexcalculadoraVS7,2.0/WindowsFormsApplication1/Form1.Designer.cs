namespace WindowsFormsApplication1
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.bt_suma = new System.Windows.Forms.Button();
            this.bt_log = new System.Windows.Forms.Button();
            this.bt_resta = new System.Windows.Forms.Button();
            this.bt_elevar = new System.Windows.Forms.Button();
            this.bt_cos = new System.Windows.Forms.Button();
            this.bt_sqrt = new System.Windows.Forms.Button();
            this.bt_div = new System.Windows.Forms.Button();
            this.bt_sen = new System.Windows.Forms.Button();
            this.bt_mult = new System.Windows.Forms.Button();
            this.bt_igual = new System.Windows.Forms.Button();
            this.bt_tan = new System.Windows.Forms.Button();
            this.bt_decimal = new System.Windows.Forms.Button();
            this.bt_0 = new System.Windows.Forms.Button();
            this.bt_5 = new System.Windows.Forms.Button();
            this.bt_6 = new System.Windows.Forms.Button();
            this.bt_4 = new System.Windows.Forms.Button();
            this.bt_8 = new System.Windows.Forms.Button();
            this.bt_9 = new System.Windows.Forms.Button();
            this.bt_7 = new System.Windows.Forms.Button();
            this.bt_2 = new System.Windows.Forms.Button();
            this.bt_3 = new System.Windows.Forms.Button();
            this.bt_1 = new System.Windows.Forms.Button();
            this.bt_modulo = new System.Windows.Forms.Button();
            this.bt_eliminar = new System.Windows.Forms.Button();
            this.txt_resultado = new System.Windows.Forms.TextBox();
            this.text_acumulado = new System.Windows.Forms.TextBox();
            this.fileSystemWatcher1 = new System.IO.FileSystemWatcher();
            ((System.ComponentModel.ISupportInitialize)(this.fileSystemWatcher1)).BeginInit();
            this.SuspendLayout();
            // 
            // bt_suma
            // 
            this.bt_suma.Location = new System.Drawing.Point(267, 41);
            this.bt_suma.Name = "bt_suma";
            this.bt_suma.Size = new System.Drawing.Size(42, 33);
            this.bt_suma.TabIndex = 0;
            this.bt_suma.Text = "+";
            this.bt_suma.UseVisualStyleBackColor = true;
            this.bt_suma.Click += new System.EventHandler(this.bt_oper_basic);
            // 
            // bt_log
            // 
            this.bt_log.Location = new System.Drawing.Point(363, 41);
            this.bt_log.Name = "bt_log";
            this.bt_log.Size = new System.Drawing.Size(42, 33);
            this.bt_log.TabIndex = 5;
            this.bt_log.Text = "log";
            this.bt_log.UseVisualStyleBackColor = true;
            this.bt_log.Click += new System.EventHandler(this.bt_complejos_click);
            // 
            // bt_resta
            // 
            this.bt_resta.Location = new System.Drawing.Point(315, 41);
            this.bt_resta.Name = "bt_resta";
            this.bt_resta.Size = new System.Drawing.Size(42, 33);
            this.bt_resta.TabIndex = 6;
            this.bt_resta.Text = "-";
            this.bt_resta.UseVisualStyleBackColor = true;
            this.bt_resta.Click += new System.EventHandler(this.bt_oper_basic);
            // 
            // bt_elevar
            // 
            this.bt_elevar.Location = new System.Drawing.Point(315, 119);
            this.bt_elevar.Name = "bt_elevar";
            this.bt_elevar.Size = new System.Drawing.Size(42, 33);
            this.bt_elevar.TabIndex = 9;
            this.bt_elevar.Text = "^";
            this.bt_elevar.UseVisualStyleBackColor = true;
            this.bt_elevar.Click += new System.EventHandler(this.bt_oper_basic);
            // 
            // bt_cos
            // 
            this.bt_cos.Location = new System.Drawing.Point(363, 119);
            this.bt_cos.Name = "bt_cos";
            this.bt_cos.Size = new System.Drawing.Size(42, 33);
            this.bt_cos.TabIndex = 8;
            this.bt_cos.Text = "cos";
            this.bt_cos.UseVisualStyleBackColor = true;
            this.bt_cos.Click += new System.EventHandler(this.bt_complejos_click);
            // 
            // bt_sqrt
            // 
            this.bt_sqrt.Location = new System.Drawing.Point(267, 119);
            this.bt_sqrt.Name = "bt_sqrt";
            this.bt_sqrt.Size = new System.Drawing.Size(42, 33);
            this.bt_sqrt.TabIndex = 7;
            this.bt_sqrt.Text = "sqrt";
            this.bt_sqrt.UseVisualStyleBackColor = true;
            this.bt_sqrt.Click += new System.EventHandler(this.bt_complejos_click);
            // 
            // bt_div
            // 
            this.bt_div.Location = new System.Drawing.Point(315, 80);
            this.bt_div.Name = "bt_div";
            this.bt_div.Size = new System.Drawing.Size(42, 33);
            this.bt_div.TabIndex = 12;
            this.bt_div.Text = "/";
            this.bt_div.UseVisualStyleBackColor = true;
            this.bt_div.Click += new System.EventHandler(this.bt_oper_basic);
            // 
            // bt_sen
            // 
            this.bt_sen.Location = new System.Drawing.Point(363, 80);
            this.bt_sen.Name = "bt_sen";
            this.bt_sen.Size = new System.Drawing.Size(42, 33);
            this.bt_sen.TabIndex = 11;
            this.bt_sen.Text = "sen";
            this.bt_sen.UseVisualStyleBackColor = true;
            this.bt_sen.Click += new System.EventHandler(this.bt_complejos_click);
            // 
            // bt_mult
            // 
            this.bt_mult.Location = new System.Drawing.Point(267, 80);
            this.bt_mult.Name = "bt_mult";
            this.bt_mult.Size = new System.Drawing.Size(42, 33);
            this.bt_mult.TabIndex = 10;
            this.bt_mult.Text = "*";
            this.bt_mult.UseVisualStyleBackColor = true;
            this.bt_mult.Click += new System.EventHandler(this.bt_oper_basic);
            // 
            // bt_igual
            // 
            this.bt_igual.Location = new System.Drawing.Point(267, 158);
            this.bt_igual.Name = "bt_igual";
            this.bt_igual.Size = new System.Drawing.Size(42, 33);
            this.bt_igual.TabIndex = 13;
            this.bt_igual.Text = "=";
            this.bt_igual.UseVisualStyleBackColor = true;
            this.bt_igual.Click += new System.EventHandler(this.bt_oper_basic);
            // 
            // bt_tan
            // 
            this.bt_tan.Location = new System.Drawing.Point(363, 158);
            this.bt_tan.Name = "bt_tan";
            this.bt_tan.Size = new System.Drawing.Size(42, 33);
            this.bt_tan.TabIndex = 14;
            this.bt_tan.Text = "tan";
            this.bt_tan.UseVisualStyleBackColor = true;
            this.bt_tan.Click += new System.EventHandler(this.bt_complejos_click);
            // 
            // bt_decimal
            // 
            this.bt_decimal.Location = new System.Drawing.Point(112, 158);
            this.bt_decimal.Name = "bt_decimal";
            this.bt_decimal.Size = new System.Drawing.Size(42, 33);
            this.bt_decimal.TabIndex = 25;
            this.bt_decimal.Text = ",";
            this.bt_decimal.UseVisualStyleBackColor = true;
            this.bt_decimal.Click += new System.EventHandler(this.add_coma);
            // 
            // bt_0
            // 
            this.bt_0.Location = new System.Drawing.Point(16, 158);
            this.bt_0.Name = "bt_0";
            this.bt_0.Size = new System.Drawing.Size(90, 33);
            this.bt_0.TabIndex = 24;
            this.bt_0.Text = "0";
            this.bt_0.UseVisualStyleBackColor = true;
            this.bt_0.Click += new System.EventHandler(this.bt_numerico);
            // 
            // bt_5
            // 
            this.bt_5.Location = new System.Drawing.Point(64, 80);
            this.bt_5.Name = "bt_5";
            this.bt_5.Size = new System.Drawing.Size(42, 33);
            this.bt_5.TabIndex = 23;
            this.bt_5.Text = "5";
            this.bt_5.UseVisualStyleBackColor = true;
            this.bt_5.Click += new System.EventHandler(this.bt_numerico);
            // 
            // bt_6
            // 
            this.bt_6.Location = new System.Drawing.Point(112, 80);
            this.bt_6.Name = "bt_6";
            this.bt_6.Size = new System.Drawing.Size(42, 33);
            this.bt_6.TabIndex = 22;
            this.bt_6.Text = "6";
            this.bt_6.UseVisualStyleBackColor = true;
            this.bt_6.Click += new System.EventHandler(this.bt_numerico);
            // 
            // bt_4
            // 
            this.bt_4.Location = new System.Drawing.Point(16, 80);
            this.bt_4.Name = "bt_4";
            this.bt_4.Size = new System.Drawing.Size(42, 33);
            this.bt_4.TabIndex = 21;
            this.bt_4.Text = "4";
            this.bt_4.UseVisualStyleBackColor = true;
            this.bt_4.Click += new System.EventHandler(this.bt_numerico);
            // 
            // bt_8
            // 
            this.bt_8.Location = new System.Drawing.Point(64, 119);
            this.bt_8.Name = "bt_8";
            this.bt_8.Size = new System.Drawing.Size(42, 33);
            this.bt_8.TabIndex = 20;
            this.bt_8.Text = "8";
            this.bt_8.UseVisualStyleBackColor = true;
            this.bt_8.Click += new System.EventHandler(this.bt_numerico);
            // 
            // bt_9
            // 
            this.bt_9.Location = new System.Drawing.Point(112, 119);
            this.bt_9.Name = "bt_9";
            this.bt_9.Size = new System.Drawing.Size(42, 33);
            this.bt_9.TabIndex = 19;
            this.bt_9.Text = "9";
            this.bt_9.UseVisualStyleBackColor = true;
            this.bt_9.Click += new System.EventHandler(this.bt_numerico);
            // 
            // bt_7
            // 
            this.bt_7.Location = new System.Drawing.Point(16, 119);
            this.bt_7.Name = "bt_7";
            this.bt_7.Size = new System.Drawing.Size(42, 33);
            this.bt_7.TabIndex = 18;
            this.bt_7.Text = "7";
            this.bt_7.UseVisualStyleBackColor = true;
            this.bt_7.Click += new System.EventHandler(this.bt_numerico);
            // 
            // bt_2
            // 
            this.bt_2.Location = new System.Drawing.Point(64, 41);
            this.bt_2.Name = "bt_2";
            this.bt_2.Size = new System.Drawing.Size(42, 33);
            this.bt_2.TabIndex = 17;
            this.bt_2.Text = "2";
            this.bt_2.UseVisualStyleBackColor = true;
            this.bt_2.Click += new System.EventHandler(this.bt_numerico);
            // 
            // bt_3
            // 
            this.bt_3.Location = new System.Drawing.Point(112, 41);
            this.bt_3.Name = "bt_3";
            this.bt_3.Size = new System.Drawing.Size(42, 33);
            this.bt_3.TabIndex = 16;
            this.bt_3.Text = "3";
            this.bt_3.UseVisualStyleBackColor = true;
            this.bt_3.Click += new System.EventHandler(this.bt_numerico);
            // 
            // bt_1
            // 
            this.bt_1.Location = new System.Drawing.Point(16, 41);
            this.bt_1.Name = "bt_1";
            this.bt_1.Size = new System.Drawing.Size(42, 33);
            this.bt_1.TabIndex = 15;
            this.bt_1.Text = "1";
            this.bt_1.UseVisualStyleBackColor = true;
            this.bt_1.Click += new System.EventHandler(this.bt_numerico);
            // 
            // bt_modulo
            // 
            this.bt_modulo.Location = new System.Drawing.Point(315, 158);
            this.bt_modulo.Name = "bt_modulo";
            this.bt_modulo.Size = new System.Drawing.Size(42, 33);
            this.bt_modulo.TabIndex = 26;
            this.bt_modulo.Text = "%";
            this.bt_modulo.UseVisualStyleBackColor = true;
            this.bt_modulo.Click += new System.EventHandler(this.bt_oper_basic);
            // 
            // bt_eliminar
            // 
            this.bt_eliminar.Location = new System.Drawing.Point(160, 41);
            this.bt_eliminar.Name = "bt_eliminar";
            this.bt_eliminar.Size = new System.Drawing.Size(100, 33);
            this.bt_eliminar.TabIndex = 28;
            this.bt_eliminar.Text = "CE";
            this.bt_eliminar.UseVisualStyleBackColor = true;
            this.bt_eliminar.Click += new System.EventHandler(this.bt_reiniciar);
            // 
            // txt_resultado
            // 
            this.txt_resultado.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txt_resultado.Location = new System.Drawing.Point(16, 4);
            this.txt_resultado.Name = "txt_resultado";
            this.txt_resultado.ReadOnly = true;
            this.txt_resultado.Size = new System.Drawing.Size(389, 31);
            this.txt_resultado.TabIndex = 31;
            this.txt_resultado.Click += new System.EventHandler(this.txt_resultado_Click);
            this.txt_resultado.KeyDown += new System.Windows.Forms.KeyEventHandler(this.txt_resultado_KeyDown);
            // 
            // text_acumulado
            // 
            this.text_acumulado.Location = new System.Drawing.Point(16, 226);
            this.text_acumulado.Name = "text_acumulado";
            this.text_acumulado.ReadOnly = true;
            this.text_acumulado.Size = new System.Drawing.Size(389, 20);
            this.text_acumulado.TabIndex = 32;
            // 
            // fileSystemWatcher1
            // 
            this.fileSystemWatcher1.EnableRaisingEvents = true;
            this.fileSystemWatcher1.SynchronizingObject = this;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(429, 299);
            this.Controls.Add(this.text_acumulado);
            this.Controls.Add(this.txt_resultado);
            this.Controls.Add(this.bt_eliminar);
            this.Controls.Add(this.bt_modulo);
            this.Controls.Add(this.bt_decimal);
            this.Controls.Add(this.bt_0);
            this.Controls.Add(this.bt_5);
            this.Controls.Add(this.bt_6);
            this.Controls.Add(this.bt_4);
            this.Controls.Add(this.bt_8);
            this.Controls.Add(this.bt_9);
            this.Controls.Add(this.bt_7);
            this.Controls.Add(this.bt_2);
            this.Controls.Add(this.bt_3);
            this.Controls.Add(this.bt_1);
            this.Controls.Add(this.bt_tan);
            this.Controls.Add(this.bt_igual);
            this.Controls.Add(this.bt_div);
            this.Controls.Add(this.bt_sen);
            this.Controls.Add(this.bt_mult);
            this.Controls.Add(this.bt_elevar);
            this.Controls.Add(this.bt_cos);
            this.Controls.Add(this.bt_sqrt);
            this.Controls.Add(this.bt_resta);
            this.Controls.Add(this.bt_log);
            this.Controls.Add(this.bt_suma);
            this.Name = "Form1";
            this.Text = "v";
            ((System.ComponentModel.ISupportInitialize)(this.fileSystemWatcher1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button bt_suma;
        private System.Windows.Forms.Button bt_log;
        private System.Windows.Forms.Button bt_resta;
        private System.Windows.Forms.Button bt_elevar;
        private System.Windows.Forms.Button bt_cos;
        private System.Windows.Forms.Button bt_sqrt;
        private System.Windows.Forms.Button bt_div;
        private System.Windows.Forms.Button bt_sen;
        private System.Windows.Forms.Button bt_mult;
        private System.Windows.Forms.Button bt_igual;
        private System.Windows.Forms.Button bt_tan;
        private System.Windows.Forms.Button bt_decimal;
        private System.Windows.Forms.Button bt_0;
        private System.Windows.Forms.Button bt_5;
        private System.Windows.Forms.Button bt_6;
        private System.Windows.Forms.Button bt_4;
        private System.Windows.Forms.Button bt_8;
        private System.Windows.Forms.Button bt_9;
        private System.Windows.Forms.Button bt_7;
        private System.Windows.Forms.Button bt_2;
        private System.Windows.Forms.Button bt_3;
        private System.Windows.Forms.Button bt_1;
        private System.Windows.Forms.Button bt_modulo;
        private System.Windows.Forms.Button bt_eliminar;
        private System.Windows.Forms.TextBox txt_resultado;
        private System.Windows.Forms.TextBox text_acumulado;
        private System.IO.FileSystemWatcher fileSystemWatcher1;
    }
}

