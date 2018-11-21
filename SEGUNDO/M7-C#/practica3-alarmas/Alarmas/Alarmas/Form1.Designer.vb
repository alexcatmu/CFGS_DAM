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
        Me.lbl_hora_actual = New System.Windows.Forms.Label()
        Me.lbl_dia_actual = New System.Windows.Forms.Label()
        Me.cb_hora = New System.Windows.Forms.ComboBox()
        Me.cb_minutos = New System.Windows.Forms.ComboBox()
        Me.cb_segundos = New System.Windows.Forms.ComboBox()
        Me.lbl_alarma = New System.Windows.Forms.Label()
        Me.cb_activa = New System.Windows.Forms.CheckBox()
        Me.SuspendLayout()
        '
        'lbl_hora_actual
        '
        Me.lbl_hora_actual.AutoSize = True
        Me.lbl_hora_actual.Font = New System.Drawing.Font("Microsoft Sans Serif", 15.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lbl_hora_actual.Location = New System.Drawing.Point(12, 9)
        Me.lbl_hora_actual.MinimumSize = New System.Drawing.Size(250, 50)
        Me.lbl_hora_actual.Name = "lbl_hora_actual"
        Me.lbl_hora_actual.Size = New System.Drawing.Size(250, 50)
        Me.lbl_hora_actual.TabIndex = 0
        Me.lbl_hora_actual.Tag = ""
        Me.lbl_hora_actual.Text = "hora_actual"
        Me.lbl_hora_actual.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        '
        'lbl_dia_actual
        '
        Me.lbl_dia_actual.AutoSize = True
        Me.lbl_dia_actual.Font = New System.Drawing.Font("Microsoft Sans Serif", 15.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lbl_dia_actual.Location = New System.Drawing.Point(12, 203)
        Me.lbl_dia_actual.MinimumSize = New System.Drawing.Size(250, 50)
        Me.lbl_dia_actual.Name = "lbl_dia_actual"
        Me.lbl_dia_actual.Size = New System.Drawing.Size(250, 50)
        Me.lbl_dia_actual.TabIndex = 1
        Me.lbl_dia_actual.Text = "dia_actual"
        Me.lbl_dia_actual.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        '
        'cb_hora
        '
        Me.cb_hora.FormattingEnabled = True
        Me.cb_hora.Location = New System.Drawing.Point(56, 105)
        Me.cb_hora.Name = "cb_hora"
        Me.cb_hora.Size = New System.Drawing.Size(48, 21)
        Me.cb_hora.TabIndex = 2
        '
        'cb_minutos
        '
        Me.cb_minutos.FormattingEnabled = True
        Me.cb_minutos.Location = New System.Drawing.Point(110, 105)
        Me.cb_minutos.Name = "cb_minutos"
        Me.cb_minutos.Size = New System.Drawing.Size(48, 21)
        Me.cb_minutos.TabIndex = 3
        '
        'cb_segundos
        '
        Me.cb_segundos.FormattingEnabled = True
        Me.cb_segundos.Location = New System.Drawing.Point(164, 105)
        Me.cb_segundos.Name = "cb_segundos"
        Me.cb_segundos.Size = New System.Drawing.Size(48, 21)
        Me.cb_segundos.TabIndex = 4
        '
        'lbl_alarma
        '
        Me.lbl_alarma.AutoSize = True
        Me.lbl_alarma.Font = New System.Drawing.Font("Microsoft Sans Serif", 10.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lbl_alarma.Location = New System.Drawing.Point(12, 59)
        Me.lbl_alarma.MinimumSize = New System.Drawing.Size(250, 30)
        Me.lbl_alarma.Name = "lbl_alarma"
        Me.lbl_alarma.Size = New System.Drawing.Size(250, 30)
        Me.lbl_alarma.TabIndex = 5
        Me.lbl_alarma.Tag = ""
        Me.lbl_alarma.Text = "Alarma"
        Me.lbl_alarma.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        '
        'cb_activa
        '
        Me.cb_activa.AutoSize = True
        Me.cb_activa.Font = New System.Drawing.Font("Microsoft Sans Serif", 10.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.cb_activa.Location = New System.Drawing.Point(110, 152)
        Me.cb_activa.Name = "cb_activa"
        Me.cb_activa.Size = New System.Drawing.Size(65, 21)
        Me.cb_activa.TabIndex = 6
        Me.cb_activa.Text = "Activa"
        Me.cb_activa.UseVisualStyleBackColor = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(284, 262)
        Me.Controls.Add(Me.cb_activa)
        Me.Controls.Add(Me.lbl_alarma)
        Me.Controls.Add(Me.cb_segundos)
        Me.Controls.Add(Me.cb_minutos)
        Me.Controls.Add(Me.cb_hora)
        Me.Controls.Add(Me.lbl_dia_actual)
        Me.Controls.Add(Me.lbl_hora_actual)
        Me.MaximumSize = New System.Drawing.Size(300, 300)
        Me.Name = "Form1"
        Me.Text = "Form1"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents lbl_hora_actual As System.Windows.Forms.Label
    Friend WithEvents lbl_dia_actual As System.Windows.Forms.Label
    Friend WithEvents cb_hora As System.Windows.Forms.ComboBox
    Friend WithEvents cb_minutos As System.Windows.Forms.ComboBox
    Friend WithEvents cb_segundos As System.Windows.Forms.ComboBox
    Friend WithEvents lbl_alarma As System.Windows.Forms.Label
    Friend WithEvents cb_activa As System.Windows.Forms.CheckBox

End Class
