namespace WindowsFormsApplication1
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
            this.Menu = new System.Windows.Forms.MenuStrip();
            this.archivoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.nuevoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.abrirToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cerrarToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.guardarComoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cerrarActualToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cerrarTodosToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.imprimirToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.buscarToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.reemplazarToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.contarToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.palabrasTotalesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.letrasToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.editarToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.textoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.tamañoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.copiarToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.pegarToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cortarToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.seleccionarTodoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.añadirFechaIHoraToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.fondoPáginaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.idiomaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.españolToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.inglésToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.catalánToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.fuenteToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.tamañoToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.interlineadoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.izdaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.izquierdaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.derechaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.centradoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mayusculaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.minúsculaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.negritaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cursivaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.colorTextoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.colorFondoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Menu.SuspendLayout();
            this.SuspendLayout();
            // 
            // Menu
            // 
            this.Menu.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.Menu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.archivoToolStripMenuItem,
            this.editarToolStripMenuItem,
            this.idiomaToolStripMenuItem,
            this.fuenteToolStripMenuItem});
            this.Menu.Location = new System.Drawing.Point(0, 0);
            this.Menu.Name = "Menu";
            this.Menu.Size = new System.Drawing.Size(708, 24);
            this.Menu.TabIndex = 0;
            this.Menu.Text = "Menu";
            // 
            // archivoToolStripMenuItem
            // 
            this.archivoToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.nuevoToolStripMenuItem,
            this.abrirToolStripMenuItem,
            this.cerrarToolStripMenuItem,
            this.guardarComoToolStripMenuItem,
            this.cerrarActualToolStripMenuItem,
            this.cerrarTodosToolStripMenuItem,
            this.imprimirToolStripMenuItem,
            this.buscarToolStripMenuItem,
            this.reemplazarToolStripMenuItem,
            this.contarToolStripMenuItem});
            this.archivoToolStripMenuItem.Name = "archivoToolStripMenuItem";
            this.archivoToolStripMenuItem.Size = new System.Drawing.Size(60, 20);
            this.archivoToolStripMenuItem.Text = "Archivo";
            this.archivoToolStripMenuItem.Click += new System.EventHandler(this.archivoToolStripMenuItem_Click);
            // 
            // nuevoToolStripMenuItem
            // 
            this.nuevoToolStripMenuItem.Name = "nuevoToolStripMenuItem";
            this.nuevoToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.nuevoToolStripMenuItem.Text = "Nuevo";
            this.nuevoToolStripMenuItem.Click += new System.EventHandler(this.eventos_archivo);
            // 
            // abrirToolStripMenuItem
            // 
            this.abrirToolStripMenuItem.Name = "abrirToolStripMenuItem";
            this.abrirToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.abrirToolStripMenuItem.Text = "Abrir";
            this.abrirToolStripMenuItem.Click += new System.EventHandler(this.eventos_archivo);
            // 
            // cerrarToolStripMenuItem
            // 
            this.cerrarToolStripMenuItem.Name = "cerrarToolStripMenuItem";
            this.cerrarToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.cerrarToolStripMenuItem.Text = "Guardar";
            this.cerrarToolStripMenuItem.Click += new System.EventHandler(this.eventos_archivo);
            // 
            // guardarComoToolStripMenuItem
            // 
            this.guardarComoToolStripMenuItem.Name = "guardarComoToolStripMenuItem";
            this.guardarComoToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.guardarComoToolStripMenuItem.Text = "Guardar como";
            this.guardarComoToolStripMenuItem.Click += new System.EventHandler(this.eventos_archivo);
            // 
            // cerrarActualToolStripMenuItem
            // 
            this.cerrarActualToolStripMenuItem.Name = "cerrarActualToolStripMenuItem";
            this.cerrarActualToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.cerrarActualToolStripMenuItem.Text = "Cerrar actual";
            this.cerrarActualToolStripMenuItem.Click += new System.EventHandler(this.eventos_archivo);
            // 
            // cerrarTodosToolStripMenuItem
            // 
            this.cerrarTodosToolStripMenuItem.Name = "cerrarTodosToolStripMenuItem";
            this.cerrarTodosToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.cerrarTodosToolStripMenuItem.Text = "Cerrar todos";
            this.cerrarTodosToolStripMenuItem.Click += new System.EventHandler(this.eventos_archivo);
            // 
            // imprimirToolStripMenuItem
            // 
            this.imprimirToolStripMenuItem.Name = "imprimirToolStripMenuItem";
            this.imprimirToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.imprimirToolStripMenuItem.Text = "Imprimir";
            this.imprimirToolStripMenuItem.Click += new System.EventHandler(this.eventos_archivo);
            // 
            // buscarToolStripMenuItem
            // 
            this.buscarToolStripMenuItem.Name = "buscarToolStripMenuItem";
            this.buscarToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.buscarToolStripMenuItem.Text = "Buscar";
            this.buscarToolStripMenuItem.Click += new System.EventHandler(this.eventos_archivo);
            // 
            // reemplazarToolStripMenuItem
            // 
            this.reemplazarToolStripMenuItem.Name = "reemplazarToolStripMenuItem";
            this.reemplazarToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.reemplazarToolStripMenuItem.Text = "Reemplazar";
            this.reemplazarToolStripMenuItem.Click += new System.EventHandler(this.eventos_archivo);
            // 
            // contarToolStripMenuItem
            // 
            this.contarToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.palabrasTotalesToolStripMenuItem,
            this.letrasToolStripMenuItem});
            this.contarToolStripMenuItem.Name = "contarToolStripMenuItem";
            this.contarToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.contarToolStripMenuItem.Text = "Contar";
            // 
            // palabrasTotalesToolStripMenuItem
            // 
            this.palabrasTotalesToolStripMenuItem.Name = "palabrasTotalesToolStripMenuItem";
            this.palabrasTotalesToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.palabrasTotalesToolStripMenuItem.Text = "Palabras";
            this.palabrasTotalesToolStripMenuItem.Click += new System.EventHandler(this.eventos_archivo);
            // 
            // letrasToolStripMenuItem
            // 
            this.letrasToolStripMenuItem.Name = "letrasToolStripMenuItem";
            this.letrasToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.letrasToolStripMenuItem.Text = "Letras";
            this.letrasToolStripMenuItem.Click += new System.EventHandler(this.eventos_archivo);
            // 
            // editarToolStripMenuItem
            // 
            this.editarToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.textoToolStripMenuItem,
            this.tamañoToolStripMenuItem,
            this.copiarToolStripMenuItem,
            this.pegarToolStripMenuItem,
            this.cortarToolStripMenuItem,
            this.seleccionarTodoToolStripMenuItem,
            this.añadirFechaIHoraToolStripMenuItem,
            this.fondoPáginaToolStripMenuItem});
            this.editarToolStripMenuItem.Name = "editarToolStripMenuItem";
            this.editarToolStripMenuItem.Size = new System.Drawing.Size(49, 20);
            this.editarToolStripMenuItem.Text = "Editar";
            // 
            // textoToolStripMenuItem
            // 
            this.textoToolStripMenuItem.Name = "textoToolStripMenuItem";
            this.textoToolStripMenuItem.Size = new System.Drawing.Size(174, 22);
            this.textoToolStripMenuItem.Text = "Texto";
            this.textoToolStripMenuItem.Click += new System.EventHandler(this.evento_editar);
            // 
            // tamañoToolStripMenuItem
            // 
            this.tamañoToolStripMenuItem.Name = "tamañoToolStripMenuItem";
            this.tamañoToolStripMenuItem.Size = new System.Drawing.Size(174, 22);
            this.tamañoToolStripMenuItem.Text = "Tamaño";
            this.tamañoToolStripMenuItem.Click += new System.EventHandler(this.evento_editar);
            // 
            // copiarToolStripMenuItem
            // 
            this.copiarToolStripMenuItem.Name = "copiarToolStripMenuItem";
            this.copiarToolStripMenuItem.Size = new System.Drawing.Size(174, 22);
            this.copiarToolStripMenuItem.Text = "Copiar";
            this.copiarToolStripMenuItem.Click += new System.EventHandler(this.evento_editar);
            // 
            // pegarToolStripMenuItem
            // 
            this.pegarToolStripMenuItem.Name = "pegarToolStripMenuItem";
            this.pegarToolStripMenuItem.Size = new System.Drawing.Size(174, 22);
            this.pegarToolStripMenuItem.Text = "Pegar";
            this.pegarToolStripMenuItem.Click += new System.EventHandler(this.evento_editar);
            // 
            // cortarToolStripMenuItem
            // 
            this.cortarToolStripMenuItem.Name = "cortarToolStripMenuItem";
            this.cortarToolStripMenuItem.Size = new System.Drawing.Size(174, 22);
            this.cortarToolStripMenuItem.Text = "Cortar";
            this.cortarToolStripMenuItem.Click += new System.EventHandler(this.evento_editar);
            // 
            // seleccionarTodoToolStripMenuItem
            // 
            this.seleccionarTodoToolStripMenuItem.Name = "seleccionarTodoToolStripMenuItem";
            this.seleccionarTodoToolStripMenuItem.Size = new System.Drawing.Size(174, 22);
            this.seleccionarTodoToolStripMenuItem.Text = "Seleccionar todo";
            this.seleccionarTodoToolStripMenuItem.Click += new System.EventHandler(this.evento_editar);
            // 
            // añadirFechaIHoraToolStripMenuItem
            // 
            this.añadirFechaIHoraToolStripMenuItem.Name = "añadirFechaIHoraToolStripMenuItem";
            this.añadirFechaIHoraToolStripMenuItem.Size = new System.Drawing.Size(174, 22);
            this.añadirFechaIHoraToolStripMenuItem.Text = "Añadir fecha i hora";
            this.añadirFechaIHoraToolStripMenuItem.Click += new System.EventHandler(this.evento_editar);
            // 
            // fondoPáginaToolStripMenuItem
            // 
            this.fondoPáginaToolStripMenuItem.Name = "fondoPáginaToolStripMenuItem";
            this.fondoPáginaToolStripMenuItem.Size = new System.Drawing.Size(174, 22);
            this.fondoPáginaToolStripMenuItem.Text = "Fondo página";
            this.fondoPáginaToolStripMenuItem.Click += new System.EventHandler(this.evento_editar);
            // 
            // idiomaToolStripMenuItem
            // 
            this.idiomaToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.españolToolStripMenuItem,
            this.inglésToolStripMenuItem,
            this.catalánToolStripMenuItem});
            this.idiomaToolStripMenuItem.Name = "idiomaToolStripMenuItem";
            this.idiomaToolStripMenuItem.Size = new System.Drawing.Size(56, 20);
            this.idiomaToolStripMenuItem.Text = "Idioma";
            // 
            // españolToolStripMenuItem
            // 
            this.españolToolStripMenuItem.Name = "españolToolStripMenuItem";
            this.españolToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.españolToolStripMenuItem.Text = "Español";
            this.españolToolStripMenuItem.Click += new System.EventHandler(this.evento_idioma);
            // 
            // inglésToolStripMenuItem
            // 
            this.inglésToolStripMenuItem.Name = "inglésToolStripMenuItem";
            this.inglésToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.inglésToolStripMenuItem.Text = "Inglés";
            this.inglésToolStripMenuItem.Click += new System.EventHandler(this.evento_idioma);
            // 
            // catalánToolStripMenuItem
            // 
            this.catalánToolStripMenuItem.Name = "catalánToolStripMenuItem";
            this.catalánToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.catalánToolStripMenuItem.Text = "Catalán";
            this.catalánToolStripMenuItem.Click += new System.EventHandler(this.evento_idioma);
            // 
            // fuenteToolStripMenuItem
            // 
            this.fuenteToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tamañoToolStripMenuItem1,
            this.interlineadoToolStripMenuItem,
            this.izdaToolStripMenuItem,
            this.mayusculaToolStripMenuItem,
            this.minúsculaToolStripMenuItem,
            this.negritaToolStripMenuItem,
            this.cursivaToolStripMenuItem,
            this.colorTextoToolStripMenuItem,
            this.colorFondoToolStripMenuItem});
            this.fuenteToolStripMenuItem.Name = "fuenteToolStripMenuItem";
            this.fuenteToolStripMenuItem.Size = new System.Drawing.Size(55, 20);
            this.fuenteToolStripMenuItem.Text = "Fuente";
            // 
            // tamañoToolStripMenuItem1
            // 
            this.tamañoToolStripMenuItem1.Name = "tamañoToolStripMenuItem1";
            this.tamañoToolStripMenuItem1.Size = new System.Drawing.Size(152, 22);
            this.tamañoToolStripMenuItem1.Text = "Tamaño";
            this.tamañoToolStripMenuItem1.Click += new System.EventHandler(this.evento_fuente);
            // 
            // interlineadoToolStripMenuItem
            // 
            this.interlineadoToolStripMenuItem.Name = "interlineadoToolStripMenuItem";
            this.interlineadoToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.interlineadoToolStripMenuItem.Text = "Interlineado";
            this.interlineadoToolStripMenuItem.Click += new System.EventHandler(this.evento_fuente);
            // 
            // izdaToolStripMenuItem
            // 
            this.izdaToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.izquierdaToolStripMenuItem,
            this.derechaToolStripMenuItem,
            this.centradoToolStripMenuItem});
            this.izdaToolStripMenuItem.Name = "izdaToolStripMenuItem";
            this.izdaToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.izdaToolStripMenuItem.Text = "Alinear";
            this.izdaToolStripMenuItem.Click += new System.EventHandler(this.evento_fuente);
            // 
            // izquierdaToolStripMenuItem
            // 
            this.izquierdaToolStripMenuItem.Name = "izquierdaToolStripMenuItem";
            this.izquierdaToolStripMenuItem.Size = new System.Drawing.Size(123, 22);
            this.izquierdaToolStripMenuItem.Text = "Izquierda";
            // 
            // derechaToolStripMenuItem
            // 
            this.derechaToolStripMenuItem.Name = "derechaToolStripMenuItem";
            this.derechaToolStripMenuItem.Size = new System.Drawing.Size(123, 22);
            this.derechaToolStripMenuItem.Text = "Derecha";
            // 
            // centradoToolStripMenuItem
            // 
            this.centradoToolStripMenuItem.Name = "centradoToolStripMenuItem";
            this.centradoToolStripMenuItem.Size = new System.Drawing.Size(123, 22);
            this.centradoToolStripMenuItem.Text = "Centrado";
            // 
            // mayusculaToolStripMenuItem
            // 
            this.mayusculaToolStripMenuItem.Name = "mayusculaToolStripMenuItem";
            this.mayusculaToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.mayusculaToolStripMenuItem.Text = "Mayúscula";
            this.mayusculaToolStripMenuItem.Click += new System.EventHandler(this.evento_fuente);
            // 
            // minúsculaToolStripMenuItem
            // 
            this.minúsculaToolStripMenuItem.Name = "minúsculaToolStripMenuItem";
            this.minúsculaToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.minúsculaToolStripMenuItem.Text = "Minúscula";
            this.minúsculaToolStripMenuItem.Click += new System.EventHandler(this.evento_fuente);
            // 
            // negritaToolStripMenuItem
            // 
            this.negritaToolStripMenuItem.Name = "negritaToolStripMenuItem";
            this.negritaToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.negritaToolStripMenuItem.Text = "Negrita";
            this.negritaToolStripMenuItem.Click += new System.EventHandler(this.evento_fuente);
            // 
            // cursivaToolStripMenuItem
            // 
            this.cursivaToolStripMenuItem.Name = "cursivaToolStripMenuItem";
            this.cursivaToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.cursivaToolStripMenuItem.Text = "Cursiva";
            this.cursivaToolStripMenuItem.Click += new System.EventHandler(this.evento_fuente);
            // 
            // colorTextoToolStripMenuItem
            // 
            this.colorTextoToolStripMenuItem.Name = "colorTextoToolStripMenuItem";
            this.colorTextoToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.colorTextoToolStripMenuItem.Text = "Color texto";
            this.colorTextoToolStripMenuItem.Click += new System.EventHandler(this.evento_fuente);
            // 
            // colorFondoToolStripMenuItem
            // 
            this.colorFondoToolStripMenuItem.Name = "colorFondoToolStripMenuItem";
            this.colorFondoToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.colorFondoToolStripMenuItem.Text = "Color fondo";
            this.colorFondoToolStripMenuItem.Click += new System.EventHandler(this.evento_fuente);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlDark;
            this.ClientSize = new System.Drawing.Size(708, 375);
            this.Controls.Add(this.Menu);
            this.IsMdiContainer = true;
            this.MainMenuStrip = this.Menu;
            this.Name = "Form1";
            this.Text = "Supereditor Alex";
            this.Menu.ResumeLayout(false);
            this.Menu.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip Menu;
        private System.Windows.Forms.ToolStripMenuItem archivoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem nuevoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem abrirToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem cerrarToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem editarToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem idiomaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem textoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem tamañoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem españolToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem inglésToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem catalánToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem guardarComoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem cerrarActualToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem cerrarTodosToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem imprimirToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem copiarToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem pegarToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem cortarToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem seleccionarTodoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem fuenteToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem tamañoToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem interlineadoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem izdaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem buscarToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem reemplazarToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem añadirFechaIHoraToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem fondoPáginaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem izquierdaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem derechaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem centradoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mayusculaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem minúsculaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem negritaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem cursivaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem colorTextoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem colorFondoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem contarToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem palabrasTotalesToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem letrasToolStripMenuItem;
    }
}

