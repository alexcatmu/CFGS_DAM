namespace alarma_ceshar
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador requerida.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén utilizando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben eliminar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido del método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.cb_hora = new System.Windows.Forms.ComboBox();
            this.cb_segundos = new System.Windows.Forms.ComboBox();
            this.cb_minutos = new System.Windows.Forms.ComboBox();
            this.lb_hora = new System.Windows.Forms.Label();
            this.lb_dia = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.Time = new System.Windows.Forms.Timer(this.components);
            this.bt_anadir = new System.Windows.Forms.Button();
            this.cb_alarmas_activas = new System.Windows.Forms.ComboBox();
            this.bt_activaToInactiva = new System.Windows.Forms.Button();
            this.cb_alarmas_inactivas = new System.Windows.Forms.ComboBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.dateTimePicker1 = new System.Windows.Forms.DateTimePicker();
            this.SuspendLayout();
            // 
            // cb_hora
            // 
            this.cb_hora.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cb_hora.FormattingEnabled = true;
            this.cb_hora.Location = new System.Drawing.Point(48, 92);
            this.cb_hora.Name = "cb_hora";
            this.cb_hora.Size = new System.Drawing.Size(60, 21);
            this.cb_hora.TabIndex = 0;
            // 
            // cb_segundos
            // 
            this.cb_segundos.DisplayMember = "5";
            this.cb_segundos.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cb_segundos.FormattingEnabled = true;
            this.cb_segundos.Location = new System.Drawing.Point(180, 92);
            this.cb_segundos.Name = "cb_segundos";
            this.cb_segundos.Size = new System.Drawing.Size(60, 21);
            this.cb_segundos.TabIndex = 1;
            // 
            // cb_minutos
            // 
            this.cb_minutos.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cb_minutos.FormattingEnabled = true;
            this.cb_minutos.Location = new System.Drawing.Point(114, 92);
            this.cb_minutos.Name = "cb_minutos";
            this.cb_minutos.Size = new System.Drawing.Size(60, 21);
            this.cb_minutos.TabIndex = 2;
            // 
            // lb_hora
            // 
            this.lb_hora.AutoSize = true;
            this.lb_hora.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_hora.Location = new System.Drawing.Point(44, 9);
            this.lb_hora.MinimumSize = new System.Drawing.Size(250, 50);
            this.lb_hora.Name = "lb_hora";
            this.lb_hora.Size = new System.Drawing.Size(250, 50);
            this.lb_hora.TabIndex = 3;
            this.lb_hora.Text = "hora_actual";
            this.lb_hora.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lb_dia
            // 
            this.lb_dia.AutoSize = true;
            this.lb_dia.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_dia.Location = new System.Drawing.Point(47, 253);
            this.lb_dia.MinimumSize = new System.Drawing.Size(250, 50);
            this.lb_dia.Name = "lb_dia";
            this.lb_dia.Size = new System.Drawing.Size(250, 50);
            this.lb_dia.TabIndex = 4;
            this.lb_dia.Text = "dia_actual";
            this.lb_dia.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(48, 65);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(30, 13);
            this.label1.TabIndex = 6;
            this.label1.Text = "Hora";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(114, 64);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(44, 13);
            this.label2.TabIndex = 7;
            this.label2.Text = "Minutos";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(180, 65);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(55, 13);
            this.label3.TabIndex = 8;
            this.label3.Text = "Segundos";
            // 
            // Time
            // 
            this.Time.Enabled = true;
            this.Time.Interval = 1000;
            this.Time.Tick += new System.EventHandler(this.Time_Tick);
            // 
            // bt_anadir
            // 
            this.bt_anadir.Location = new System.Drawing.Point(262, 90);
            this.bt_anadir.Name = "bt_anadir";
            this.bt_anadir.Size = new System.Drawing.Size(23, 23);
            this.bt_anadir.TabIndex = 9;
            this.bt_anadir.Text = "+";
            this.bt_anadir.UseVisualStyleBackColor = true;
            this.bt_anadir.Click += new System.EventHandler(this.bt_anadir_Click);
            // 
            // cb_alarmas_activas
            // 
            this.cb_alarmas_activas.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cb_alarmas_activas.FormattingEnabled = true;
            this.cb_alarmas_activas.Location = new System.Drawing.Point(43, 175);
            this.cb_alarmas_activas.Name = "cb_alarmas_activas";
            this.cb_alarmas_activas.Size = new System.Drawing.Size(83, 21);
            this.cb_alarmas_activas.TabIndex = 10;
            // 
            // bt_activaToInactiva
            // 
            this.bt_activaToInactiva.Location = new System.Drawing.Point(151, 175);
            this.bt_activaToInactiva.Name = "bt_activaToInactiva";
            this.bt_activaToInactiva.Size = new System.Drawing.Size(29, 21);
            this.bt_activaToInactiva.TabIndex = 11;
            this.bt_activaToInactiva.Text = "->";
            this.bt_activaToInactiva.UseVisualStyleBackColor = true;
            this.bt_activaToInactiva.Click += new System.EventHandler(this.bt_activaToInactiva_Click);
            // 
            // cb_alarmas_inactivas
            // 
            this.cb_alarmas_inactivas.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cb_alarmas_inactivas.FormattingEnabled = true;
            this.cb_alarmas_inactivas.Location = new System.Drawing.Point(201, 175);
            this.cb_alarmas_inactivas.Name = "cb_alarmas_inactivas";
            this.cb_alarmas_inactivas.Size = new System.Drawing.Size(76, 21);
            this.cb_alarmas_inactivas.TabIndex = 12;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(40, 149);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(81, 13);
            this.label4.TabIndex = 13;
            this.label4.Text = "Alarmas activas";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(198, 149);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(89, 13);
            this.label5.TabIndex = 14;
            this.label5.Text = "Alarmas inactivas";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(151, 202);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(29, 21);
            this.button1.TabIndex = 15;
            this.button1.Text = "<-";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // dateTimePicker1
            // 
            this.dateTimePicker1.Location = new System.Drawing.Point(68, 9);
            this.dateTimePicker1.Name = "dateTimePicker1";
            this.dateTimePicker1.Size = new System.Drawing.Size(200, 20);
            this.dateTimePicker1.TabIndex = 16;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(334, 312);
            this.Controls.Add(this.dateTimePicker1);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.cb_alarmas_inactivas);
            this.Controls.Add(this.bt_activaToInactiva);
            this.Controls.Add(this.cb_alarmas_activas);
            this.Controls.Add(this.bt_anadir);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.lb_dia);
            this.Controls.Add(this.lb_hora);
            this.Controls.Add(this.cb_minutos);
            this.Controls.Add(this.cb_segundos);
            this.Controls.Add(this.cb_hora);
            this.MaximumSize = new System.Drawing.Size(350, 350);
            this.MinimumSize = new System.Drawing.Size(350, 350);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ComboBox cb_hora;
        private System.Windows.Forms.ComboBox cb_segundos;
        private System.Windows.Forms.ComboBox cb_minutos;
        private System.Windows.Forms.Label lb_hora;
        private System.Windows.Forms.Label lb_dia;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Timer Time;
        private System.Windows.Forms.Button bt_anadir;
        private System.Windows.Forms.ComboBox cb_alarmas_activas;
        private System.Windows.Forms.Button bt_activaToInactiva;
        private System.Windows.Forms.ComboBox cb_alarmas_inactivas;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.DateTimePicker dateTimePicker1;
    }
}

