<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class encriptacion
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
        Me.texto_original = New System.Windows.Forms.TextBox()
        Me.btRSA = New System.Windows.Forms.Button()
        Me.btDES = New System.Windows.Forms.Button()
        Me.btTripleDES = New System.Windows.Forms.Button()
        Me.btAES = New System.Windows.Forms.Button()
        Me.RBencriptar = New System.Windows.Forms.RadioButton()
        Me.RBdesencriptar = New System.Windows.Forms.RadioButton()
        Me.GBenc_dec = New System.Windows.Forms.GroupBox()
        Me.texto_encript = New System.Windows.Forms.TextBox()
        Me.texto_decript = New System.Windows.Forms.TextBox()
        Me.Button1 = New System.Windows.Forms.Button()
        Me.GBenc_dec.SuspendLayout()
        Me.SuspendLayout()
        '
        'texto_original
        '
        Me.texto_original.Font = New System.Drawing.Font("Microsoft Sans Serif", 10.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.texto_original.Location = New System.Drawing.Point(13, 13)
        Me.texto_original.Multiline = True
        Me.texto_original.Name = "texto_original"
        Me.texto_original.ScrollBars = System.Windows.Forms.ScrollBars.Both
        Me.texto_original.Size = New System.Drawing.Size(316, 151)
        Me.texto_original.TabIndex = 0
        '
        'btRSA
        '
        Me.btRSA.Location = New System.Drawing.Point(463, 13)
        Me.btRSA.Name = "btRSA"
        Me.btRSA.Size = New System.Drawing.Size(75, 23)
        Me.btRSA.TabIndex = 1
        Me.btRSA.Text = "RSA"
        Me.btRSA.UseVisualStyleBackColor = True
        '
        'btDES
        '
        Me.btDES.Location = New System.Drawing.Point(463, 42)
        Me.btDES.Name = "btDES"
        Me.btDES.Size = New System.Drawing.Size(75, 23)
        Me.btDES.TabIndex = 2
        Me.btDES.Text = "DES"
        Me.btDES.UseVisualStyleBackColor = True
        '
        'btTripleDES
        '
        Me.btTripleDES.Location = New System.Drawing.Point(463, 71)
        Me.btTripleDES.Name = "btTripleDES"
        Me.btTripleDES.Size = New System.Drawing.Size(75, 23)
        Me.btTripleDES.TabIndex = 3
        Me.btTripleDES.Text = "Triple DES"
        Me.btTripleDES.UseVisualStyleBackColor = True
        '
        'btAES
        '
        Me.btAES.Location = New System.Drawing.Point(463, 101)
        Me.btAES.Name = "btAES"
        Me.btAES.Size = New System.Drawing.Size(75, 23)
        Me.btAES.TabIndex = 4
        Me.btAES.Text = "AES"
        Me.btAES.UseVisualStyleBackColor = True
        '
        'RBencriptar
        '
        Me.RBencriptar.AutoSize = True
        Me.RBencriptar.Checked = True
        Me.RBencriptar.Location = New System.Drawing.Point(7, 12)
        Me.RBencriptar.Name = "RBencriptar"
        Me.RBencriptar.Size = New System.Drawing.Size(67, 17)
        Me.RBencriptar.TabIndex = 5
        Me.RBencriptar.TabStop = True
        Me.RBencriptar.Text = "Encriptar"
        Me.RBencriptar.UseVisualStyleBackColor = True
        '
        'RBdesencriptar
        '
        Me.RBdesencriptar.AutoSize = True
        Me.RBdesencriptar.Location = New System.Drawing.Point(7, 41)
        Me.RBdesencriptar.Name = "RBdesencriptar"
        Me.RBdesencriptar.Size = New System.Drawing.Size(85, 17)
        Me.RBdesencriptar.TabIndex = 6
        Me.RBdesencriptar.Text = "Desencriptar"
        Me.RBdesencriptar.UseVisualStyleBackColor = True
        '
        'GBenc_dec
        '
        Me.GBenc_dec.Controls.Add(Me.RBdesencriptar)
        Me.GBenc_dec.Controls.Add(Me.RBencriptar)
        Me.GBenc_dec.Location = New System.Drawing.Point(345, 30)
        Me.GBenc_dec.Name = "GBenc_dec"
        Me.GBenc_dec.Size = New System.Drawing.Size(107, 71)
        Me.GBenc_dec.TabIndex = 7
        Me.GBenc_dec.TabStop = False
        '
        'texto_encript
        '
        Me.texto_encript.Location = New System.Drawing.Point(13, 195)
        Me.texto_encript.Multiline = True
        Me.texto_encript.Name = "texto_encript"
        Me.texto_encript.ScrollBars = System.Windows.Forms.ScrollBars.Both
        Me.texto_encript.Size = New System.Drawing.Size(316, 124)
        Me.texto_encript.TabIndex = 8
        '
        'texto_decript
        '
        Me.texto_decript.Location = New System.Drawing.Point(345, 195)
        Me.texto_decript.Multiline = True
        Me.texto_decript.Name = "texto_decript"
        Me.texto_decript.ScrollBars = System.Windows.Forms.ScrollBars.Vertical
        Me.texto_decript.Size = New System.Drawing.Size(193, 124)
        Me.texto_decript.TabIndex = 9
        '
        'Button1
        '
        Me.Button1.Location = New System.Drawing.Point(345, 140)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(75, 23)
        Me.Button1.TabIndex = 10
        Me.Button1.Text = "Info"
        Me.Button1.UseVisualStyleBackColor = True
        '
        'encriptacion
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(550, 330)
        Me.Controls.Add(Me.Button1)
        Me.Controls.Add(Me.texto_decript)
        Me.Controls.Add(Me.texto_encript)
        Me.Controls.Add(Me.GBenc_dec)
        Me.Controls.Add(Me.btAES)
        Me.Controls.Add(Me.btTripleDES)
        Me.Controls.Add(Me.btDES)
        Me.Controls.Add(Me.btRSA)
        Me.Controls.Add(Me.texto_original)
        Me.MaximizeBox = False
        Me.MaximumSize = New System.Drawing.Size(566, 369)
        Me.MinimumSize = New System.Drawing.Size(566, 369)
        Me.Name = "encriptacion"
        Me.Text = "encriptacion"
        Me.GBenc_dec.ResumeLayout(False)
        Me.GBenc_dec.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents texto_original As System.Windows.Forms.TextBox
    Friend WithEvents btRSA As System.Windows.Forms.Button
    Friend WithEvents btDES As System.Windows.Forms.Button
    Friend WithEvents btTripleDES As System.Windows.Forms.Button
    Friend WithEvents btAES As System.Windows.Forms.Button
    Friend WithEvents RBencriptar As System.Windows.Forms.RadioButton
    Friend WithEvents RBdesencriptar As System.Windows.Forms.RadioButton
    Friend WithEvents GBenc_dec As System.Windows.Forms.GroupBox
    Friend WithEvents texto_encript As System.Windows.Forms.TextBox
    Friend WithEvents texto_decript As System.Windows.Forms.TextBox
    Friend WithEvents Button1 As System.Windows.Forms.Button

End Class
