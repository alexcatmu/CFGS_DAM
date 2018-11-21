Public Class Form1

    Public alfabeto As String = "abcdefghijklmnñopqrstuvwxyz"

    Private array_mi_propio_porcentaje() As Double

    Private porcentaje_alfabeto_estadistica(26) As Double

    Private alfabeto_estadistico(26) As String

    Private array_abecedario_ataque(26) As String

    Dim mi_propio_texto As String


    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

        For i = 0 To Me.alfabeto.Length - 1
            Me.array_abecedario_ataque(i) = Me.alfabeto(i)
        Next

        Me.porcentaje_alfabeto_estadistica = {12.53,
                                                1.42,
                                                4.68,
                                                5.86,
                                                13.68,
                                                0.69,
                                                1.01,
                                                0.7,
                                                6.25,
                                                0.44,
                                                0.003,
                                                4.97,
                                                3.15,
                                                6.71,
                                                0.007,
                                                8.68,
                                                2.51,
                                                0.88,
                                                6.87,
                                                7.98,
                                                4.63,
                                                3.93,
                                                0.9,
                                                0.02,
                                                0.22,
                                                0.9,
                                                0.52
                                             }

        For i As Integer = 1 To 26
            inc_dec.Items.Add(i)
        Next

        Me.mi_propio_texto = My.Computer.FileSystem.ReadAllText(AppDomain.CurrentDomain.BaseDirectory & "\muchaspalabrasprimo.txt")
        'texto_enc_dec.Text = Me.mi_propio_texto
        Me.array_mi_propio_porcentaje = porcentajes_abecedario(True)

        Dim stringo As String = ""
        For i = 0 To Me.array_mi_propio_porcentaje.Length  - 1
            stringo += Convert.ToString(Me.array_mi_propio_porcentaje(i)) + vbCr
        Next
        Label2.Text = stringo
        'Aqui estaria el porcentaje de mi propiaa estadistica con lo que hay en el texto de arriba

    End Sub


    Private Sub bt_encriptar_Click(sender As Object, e As EventArgs) Handles bt_encriptar.Click
        encrypt_decrypt(False)
    End Sub


    Private Sub bt_desencriptar_Click(sender As Object, e As EventArgs) Handles Button2.Click

        encrypt_decrypt(True)

    End Sub

    Private Sub encrypt_decrypt(valor_inicial As Boolean)

        Dim texto_inicial As String = ""
        Dim valor_avance As Integer = 0
        Dim texto_final As String = ""
        Dim letra As String
        Dim auxiliar As Integer = 0
        valor_avance = inc_dec.SelectedItem
        texto_inicial = texto_enc_dec.Text
        Dim i As Integer
        For i = 0 To texto_inicial.Length - 1
            letra = texto_inicial(i)
            Dim j As Integer = 0
            If (valor_inicial) Then
                auxiliar = 27 - valor_avance
            Else
                auxiliar = valor_avance
            End If

            Dim continuar As Boolean = True
            While (j < alfabeto.Length And continuar = True)
                If auxiliar > 26 Then
                    auxiliar = 0
                End If

                If alfabeto(j) = letra Then
                    texto_final += alfabeto(auxiliar)
                    continuar = False
                ElseIf letra = " " Then
                    texto_final += " "
                    continuar = False
                End If
                j += 1
                auxiliar += 1
            End While
            If continuar = True Then
                texto_final += letra
            End If
        Next
        txt_resultado.Text = texto_final
    End Sub

    Private Sub bt_ataque_click(sender As Object, e As EventArgs) Handles Button1.Click
        'Este es el array con los porcentajes del texto cifrado que nos da el usuario
        'Este array contiene 26 posiciones con el porcentaje de cada una de las letras originales
        'Se busca relacion con las 26 posiciones de porcentaje de las letras para este ataque.
        Dim array_porcentajes_cifrado As Array = porcentajes_abecedario(False)
        Dim array_abecedario_usuario(26) As String

        For i = 0 To Me.alfabeto.Length - 1
            array_abecedario_usuario(i) = Me.alfabeto(i)
        Next


        Dim letra_auxiliar As String
        Dim letra_usuario As String
        Dim porcentaje_auxiliar As Double
        Dim porcentaje_usuario As Double

        For i = 0 To porcentaje_alfabeto_estadistica.Length - 1
            For j = 0 To Me.porcentaje_alfabeto_estadistica.Length - 2
                If Me.porcentaje_alfabeto_estadistica(j + 1) > Me.porcentaje_alfabeto_estadistica(j) Then

                    porcentaje_auxiliar = Me.porcentaje_alfabeto_estadistica(j + 1)
                    Me.porcentaje_alfabeto_estadistica(j + 1) = Me.porcentaje_alfabeto_estadistica(j)
                    Me.porcentaje_alfabeto_estadistica(j) = porcentaje_auxiliar

                    letra_auxiliar = Me.array_abecedario_ataque(j + 1)
                    Me.array_abecedario_ataque(j + 1) = Me.array_abecedario_ataque(j)
                    Me.array_abecedario_ataque(j) = letra_auxiliar

                End If

                If array_porcentajes_cifrado(j + 1) > array_porcentajes_cifrado(j) Then
                    porcentaje_usuario = array_porcentajes_cifrado(j + 1)
                    array_porcentajes_cifrado(j + 1) = array_porcentajes_cifrado(j)
                    array_porcentajes_cifrado(j) = porcentaje_usuario

                    letra_usuario = array_abecedario_usuario(j + 1)
                    array_abecedario_usuario(j + 1) = array_abecedario_usuario(j)
                    array_abecedario_usuario(j) = letra_usuario

                End If

            Next
        Next
        Dim texto_string_aux As String = ""
        Dim encontrado As Boolean
        Dim cont As Integer

        For i = 0 To texto_enc_dec.Text.Length - 1
            If (texto_enc_dec.Text(i) = " ") Then
                texto_string_aux += " "

            Else
                encontrado = False
                cont = 0
                While (cont < array_porcentajes_cifrado.Length And encontrado = False)

                    If (texto_enc_dec.Text(i) = array_abecedario_usuario(cont)) Then

                        texto_string_aux += array_abecedario_ataque(cont)
                        encontrado = True
                    End If
                    cont += 1
                End While
                If encontrado = False Then
                    texto_string_aux += texto_enc_dec.Text(i)
                End If
            End If
        Next

        txt_resultado.Text = texto_string_aux




        Dim message = String.Join(Environment.NewLine, array_abecedario_usuario.ToArray())
        MessageBox.Show(message)

        Dim message2 = String.Join(Environment.NewLine, array_abecedario_ataque.ToArray())
        MessageBox.Show(message2)


    End Sub


    Private Function porcentajes_abecedario(Mio As Boolean)
        Dim array_porcen(26) As Double
        Dim texto As String
        If (Mio = False) Then
            texto = texto_enc_dec.Text
        Else
            texto = Me.mi_propio_texto
        End If

        For i = 0 To texto.Length - 1
            Dim stringo As String = texto(i)
            For j = 0 To array_porcen.Length - 1
                If stringo = Me.alfabeto(j) Then
                    array_porcen(j) += 1
                End If
            Next
        Next

        Dim total_letras As Integer = texto.Length
        Dim aux As Integer = total_letras
        For i = 0 To texto.Length - 1
            If texto(i) = " " Then
                aux -= 1
            End If
        Next

        total_letras = aux

        Dim prueba As Double = 0.0
        For i = 0 To array_porcen.Length - 1
            array_porcen(i) = array_porcen(i) / total_letras * 100
            prueba += array_porcen(i)
        Next
        Return array_porcen

    End Function
    '
    'Private Function letra_original() As Object
    'Throw New NotImplementedException
    ' End Function


    Private Sub intercambiar_Click(sender As Object, e As EventArgs) Handles intercambiar.Click
        texto_enc_dec.Text = txt_resultado.Text
        txt_resultado.Text = ""
    End Sub

    Private Sub RadioButton1_CheckedChanged(sender As Object, e As EventArgs)

        texto_enc_dec.SelectionStart = 0
        texto_enc_dec.SelectionLength = texto_enc_dec.Text.Length - 1

        'If (RadioButton1.Checked = True) Then
        '    If (Not String.IsNullOrEmpty(texto_enc_dec.Text)) Then
        '        texto_enc_dec.SelectionStart = 0
        '        texto_enc_dec.SelectionLength = texto_enc_dec.Text.Length
        '    End If

        'Else
        '    If (Not String.IsNullOrEmpty(texto_enc_dec.Text)) Then
        '        texto_enc_dec.SelectionStart = 0
        '        texto_enc_dec.SelectionLength = False
        '    End If
        'End If

        'If (RadioButton2.Checked = True) Then
        '    If (Not String.IsNullOrEmpty(txt_resultado.Text)) Then
        '        txt_resultado.SelectionStart = 0
        '        txt_resultado.SelectionLength = txt_resultado.Text.Length
        '    End If

        'Else
        '    If (Not String.IsNullOrEmpty(txt_resultado.Text)) Then
        '        txt_resultado.SelectionStart = 0
        '        txt_resultado.SelectionLength = False
        '    End If
        'End If





    End Sub

End Class
