<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form reemplaza a Dispose para limpiar la lista de componentes.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Requerido por el Diseñador de Windows Forms
    Private components As System.ComponentModel.IContainer

    'NOTA: el Diseñador de Windows Forms necesita el siguiente procedimiento
    'Se puede modificar usando el Diseñador de Windows Forms.  
    'No lo modifique con el editor de código.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.text_introduce = New System.Windows.Forms.TextBox()
        Me.text_resultado = New System.Windows.Forms.TextBox()
        Me.bt_generar = New System.Windows.Forms.Button()
        Me.text_comprueba = New System.Windows.Forms.TextBox()
        Me.Button2 = New System.Windows.Forms.Button()
        Me.radios_encrypt = New System.Windows.Forms.GroupBox()
        Me.MD5 = New System.Windows.Forms.RadioButton()
        Me.SHA256 = New System.Windows.Forms.RadioButton()
        Me.SHA384 = New System.Windows.Forms.RadioButton()
        Me.SHA512 = New System.Windows.Forms.RadioButton()
        Me.radios_text_arch = New System.Windows.Forms.GroupBox()
        Me.texto = New System.Windows.Forms.RadioButton()
        Me.archivo = New System.Windows.Forms.RadioButton()
        Me.elegir_archivo = New System.Windows.Forms.OpenFileDialog()
        Me.radios_encrypt.SuspendLayout()
        Me.radios_text_arch.SuspendLayout()
        Me.SuspendLayout()
        '
        'text_introduce
        '
        Me.text_introduce.Location = New System.Drawing.Point(12, 37)
        Me.text_introduce.Name = "text_introduce"
        Me.text_introduce.Size = New System.Drawing.Size(213, 20)
        Me.text_introduce.TabIndex = 0
        '
        'text_resultado
        '
        Me.text_resultado.Location = New System.Drawing.Point(12, 174)
        Me.text_resultado.Name = "text_resultado"
        Me.text_resultado.Size = New System.Drawing.Size(213, 20)
        Me.text_resultado.TabIndex = 1
        '
        'bt_generar
        '
        Me.bt_generar.Location = New System.Drawing.Point(12, 75)
        Me.bt_generar.Name = "bt_generar"
        Me.bt_generar.Size = New System.Drawing.Size(75, 23)
        Me.bt_generar.TabIndex = 2
        Me.bt_generar.Text = "generar"
        Me.bt_generar.UseVisualStyleBackColor = True
        '
        'text_comprueba
        '
        Me.text_comprueba.Location = New System.Drawing.Point(13, 219)
        Me.text_comprueba.Name = "text_comprueba"
        Me.text_comprueba.Size = New System.Drawing.Size(212, 20)
        Me.text_comprueba.TabIndex = 3
        '
        'Button2
        '
        Me.Button2.Location = New System.Drawing.Point(263, 185)
        Me.Button2.Name = "Button2"
        Me.Button2.Size = New System.Drawing.Size(90, 23)
        Me.Button2.TabIndex = 4
        Me.Button2.Text = "Comprobacion"
        Me.Button2.UseVisualStyleBackColor = True
        '
        'radios_encrypt
        '
        Me.radios_encrypt.Controls.Add(Me.MD5)
        Me.radios_encrypt.Controls.Add(Me.SHA256)
        Me.radios_encrypt.Controls.Add(Me.SHA384)
        Me.radios_encrypt.Controls.Add(Me.SHA512)
        Me.radios_encrypt.Location = New System.Drawing.Point(321, 37)
        Me.radios_encrypt.Name = "radios_encrypt"
        Me.radios_encrypt.Size = New System.Drawing.Size(135, 100)
        Me.radios_encrypt.TabIndex = 11
        Me.radios_encrypt.TabStop = False
        Me.radios_encrypt.Text = "+"
        '
        'MD5
        '
        Me.MD5.AutoSize = True
        Me.MD5.Checked = True
        Me.MD5.Location = New System.Drawing.Point(42, -4)
        Me.MD5.Name = "MD5"
        Me.MD5.Size = New System.Drawing.Size(48, 17)
        Me.MD5.TabIndex = 14
        Me.MD5.TabStop = True
        Me.MD5.Text = "MD5"
        Me.MD5.UseVisualStyleBackColor = True
        '
        'SHA256
        '
        Me.SHA256.AutoSize = True
        Me.SHA256.Location = New System.Drawing.Point(42, 19)
        Me.SHA256.Name = "SHA256"
        Me.SHA256.Size = New System.Drawing.Size(68, 17)
        Me.SHA256.TabIndex = 13
        Me.SHA256.TabStop = True
        Me.SHA256.Text = "SHA 256"
        Me.SHA256.UseVisualStyleBackColor = True
        '
        'SHA384
        '
        Me.SHA384.AutoSize = True
        Me.SHA384.Location = New System.Drawing.Point(42, 42)
        Me.SHA384.Name = "SHA384"
        Me.SHA384.Size = New System.Drawing.Size(68, 17)
        Me.SHA384.TabIndex = 12
        Me.SHA384.TabStop = True
        Me.SHA384.Text = "SHA 384"
        Me.SHA384.UseVisualStyleBackColor = True
        '
        'SHA512
        '
        Me.SHA512.AutoSize = True
        Me.SHA512.Location = New System.Drawing.Point(42, 65)
        Me.SHA512.Name = "SHA512"
        Me.SHA512.Size = New System.Drawing.Size(68, 17)
        Me.SHA512.TabIndex = 11
        Me.SHA512.TabStop = True
        Me.SHA512.Text = "SHA 512"
        Me.SHA512.UseVisualStyleBackColor = True
        '
        'radios_text_arch
        '
        Me.radios_text_arch.Controls.Add(Me.texto)
        Me.radios_text_arch.Controls.Add(Me.archivo)
        Me.radios_text_arch.Location = New System.Drawing.Point(231, 37)
        Me.radios_text_arch.Name = "radios_text_arch"
        Me.radios_text_arch.Size = New System.Drawing.Size(114, 100)
        Me.radios_text_arch.TabIndex = 12
        Me.radios_text_arch.TabStop = False
        '
        'texto
        '
        Me.texto.AutoSize = True
        Me.texto.Checked = True
        Me.texto.Location = New System.Drawing.Point(24, 52)
        Me.texto.Name = "texto"
        Me.texto.Size = New System.Drawing.Size(48, 17)
        Me.texto.TabIndex = 8
        Me.texto.TabStop = True
        Me.texto.Text = "texto"
        Me.texto.UseVisualStyleBackColor = True
        '
        'archivo
        '
        Me.archivo.AutoSize = True
        Me.archivo.Location = New System.Drawing.Point(24, 19)
        Me.archivo.Name = "archivo"
        Me.archivo.Size = New System.Drawing.Size(60, 17)
        Me.archivo.TabIndex = 7
        Me.archivo.TabStop = True
        Me.archivo.Text = "archivo"
        Me.archivo.UseVisualStyleBackColor = True
        '
        'elegir_archivo
        '
        Me.elegir_archivo.FileName = "OpenFileDialog1"
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(468, 289)
        Me.Controls.Add(Me.radios_text_arch)
        Me.Controls.Add(Me.radios_encrypt)
        Me.Controls.Add(Me.Button2)
        Me.Controls.Add(Me.text_comprueba)
        Me.Controls.Add(Me.bt_generar)
        Me.Controls.Add(Me.text_resultado)
        Me.Controls.Add(Me.text_introduce)
        Me.Name = "Form1"
        Me.Text = "Form1"
        Me.radios_encrypt.ResumeLayout(False)
        Me.radios_encrypt.PerformLayout()
        Me.radios_text_arch.ResumeLayout(False)
        Me.radios_text_arch.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents text_introduce As System.Windows.Forms.TextBox
    Friend WithEvents text_resultado As System.Windows.Forms.TextBox
    Friend WithEvents bt_generar As System.Windows.Forms.Button
    Friend WithEvents text_comprueba As System.Windows.Forms.TextBox
    Friend WithEvents Button2 As System.Windows.Forms.Button
    Friend WithEvents radios_encrypt As System.Windows.Forms.GroupBox
    Friend WithEvents MD5 As System.Windows.Forms.RadioButton
    Friend WithEvents SHA256 As System.Windows.Forms.RadioButton
    Friend WithEvents SHA384 As System.Windows.Forms.RadioButton
    Friend WithEvents SHA512 As System.Windows.Forms.RadioButton
    Friend WithEvents radios_text_arch As System.Windows.Forms.GroupBox
    Friend WithEvents texto As System.Windows.Forms.RadioButton
    Friend WithEvents archivo As System.Windows.Forms.RadioButton
    Friend WithEvents elegir_archivo As System.Windows.Forms.OpenFileDialog

End Class
