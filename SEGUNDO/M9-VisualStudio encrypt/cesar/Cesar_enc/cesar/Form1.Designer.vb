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
        Me.bt_encriptar = New System.Windows.Forms.Button()
        Me.Button2 = New System.Windows.Forms.Button()
        Me.texto_enc_dec = New System.Windows.Forms.TextBox()
        Me.txt_resultado = New System.Windows.Forms.TextBox()
        Me.inc_dec = New System.Windows.Forms.ComboBox()
        Me.Button1 = New System.Windows.Forms.Button()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.intercambiar = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'bt_encriptar
        '
        Me.bt_encriptar.Location = New System.Drawing.Point(80, 256)
        Me.bt_encriptar.Margin = New System.Windows.Forms.Padding(4)
        Me.bt_encriptar.Name = "bt_encriptar"
        Me.bt_encriptar.Size = New System.Drawing.Size(88, 26)
        Me.bt_encriptar.TabIndex = 0
        Me.bt_encriptar.Text = "encriptar"
        Me.bt_encriptar.UseVisualStyleBackColor = True
        '
        'Button2
        '
        Me.Button2.Location = New System.Drawing.Point(339, 256)
        Me.Button2.Margin = New System.Windows.Forms.Padding(4)
        Me.Button2.Name = "Button2"
        Me.Button2.Size = New System.Drawing.Size(88, 26)
        Me.Button2.TabIndex = 1
        Me.Button2.Text = "desencriptar"
        Me.Button2.UseVisualStyleBackColor = True
        '
        'texto_enc_dec
        '
        Me.texto_enc_dec.Font = New System.Drawing.Font("Microsoft Sans Serif", 9.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.texto_enc_dec.ForeColor = System.Drawing.SystemColors.WindowText
        Me.texto_enc_dec.Location = New System.Drawing.Point(60, 45)
        Me.texto_enc_dec.Margin = New System.Windows.Forms.Padding(4)
        Me.texto_enc_dec.Multiline = True
        Me.texto_enc_dec.Name = "texto_enc_dec"
        Me.texto_enc_dec.ScrollBars = System.Windows.Forms.ScrollBars.Vertical
        Me.texto_enc_dec.Size = New System.Drawing.Size(365, 110)
        Me.texto_enc_dec.TabIndex = 3
        '
        'txt_resultado
        '
        Me.txt_resultado.Font = New System.Drawing.Font("Microsoft Sans Serif", 9.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.txt_resultado.Location = New System.Drawing.Point(60, 163)
        Me.txt_resultado.Margin = New System.Windows.Forms.Padding(4)
        Me.txt_resultado.Multiline = True
        Me.txt_resultado.Name = "txt_resultado"
        Me.txt_resultado.ScrollBars = System.Windows.Forms.ScrollBars.Vertical
        Me.txt_resultado.Size = New System.Drawing.Size(365, 86)
        Me.txt_resultado.TabIndex = 4
        '
        'inc_dec
        '
        Me.inc_dec.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
        Me.inc_dec.FormattingEnabled = True
        Me.inc_dec.Location = New System.Drawing.Point(181, 14)
        Me.inc_dec.Margin = New System.Windows.Forms.Padding(4)
        Me.inc_dec.Name = "inc_dec"
        Me.inc_dec.Size = New System.Drawing.Size(82, 23)
        Me.inc_dec.TabIndex = 5
        '
        'Button1
        '
        Me.Button1.Location = New System.Drawing.Point(213, 307)
        Me.Button1.Margin = New System.Windows.Forms.Padding(4)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(88, 26)
        Me.Button1.TabIndex = 6
        Me.Button1.Text = "Ataquee"
        Me.Button1.UseVisualStyleBackColor = True
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(525, 17)
        Me.Label1.Margin = New System.Windows.Forms.Padding(4, 0, 4, 0)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(129, 15)
        Me.Label1.TabIndex = 7
        Me.Label1.Text = "Porcentaje de mi texto"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(525, 32)
        Me.Label2.Margin = New System.Windows.Forms.Padding(4, 0, 4, 0)
        Me.Label2.MinimumSize = New System.Drawing.Size(116, 289)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(116, 289)
        Me.Label2.TabIndex = 8
        '
        'intercambiar
        '
        Me.intercambiar.Location = New System.Drawing.Point(213, 255)
        Me.intercambiar.Margin = New System.Windows.Forms.Padding(4)
        Me.intercambiar.Name = "intercambiar"
        Me.intercambiar.Size = New System.Drawing.Size(88, 26)
        Me.intercambiar.TabIndex = 9
        Me.intercambiar.Text = "Intercambiar "
        Me.intercambiar.UseVisualStyleBackColor = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(7.0!, 15.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(784, 462)
        Me.Controls.Add(Me.intercambiar)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.Button1)
        Me.Controls.Add(Me.inc_dec)
        Me.Controls.Add(Me.txt_resultado)
        Me.Controls.Add(Me.texto_enc_dec)
        Me.Controls.Add(Me.Button2)
        Me.Controls.Add(Me.bt_encriptar)
        Me.Font = New System.Drawing.Font("Microsoft Sans Serif", 9.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Margin = New System.Windows.Forms.Padding(4)
        Me.MaximizeBox = False
        Me.MaximumSize = New System.Drawing.Size(800, 500)
        Me.MinimumSize = New System.Drawing.Size(800, 500)
        Me.Name = "Form1"
        Me.Text = "Form1"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents bt_encriptar As System.Windows.Forms.Button
    Friend WithEvents Button2 As System.Windows.Forms.Button
    Friend WithEvents texto_enc_dec As System.Windows.Forms.TextBox
    Friend WithEvents txt_resultado As System.Windows.Forms.TextBox
    Friend WithEvents inc_dec As System.Windows.Forms.ComboBox
    Friend WithEvents Button1 As System.Windows.Forms.Button
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents intercambiar As System.Windows.Forms.Button

End Class
