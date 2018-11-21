Imports System.Security.Cryptography
Imports System.IO

Public Class Form1

    Private Sub bt_generar_click(sender As Object, e As EventArgs) Handles bt_generar.Click
        Dim utf8Encoding As New System.Text.UTF8Encoding
        Dim fraseCodificada() As Byte = utf8Encoding.GetBytes(text_introduce.Text)
        Dim ByteHash() As Byte
        If (MD5.Checked = True) Then
            ByteHash = New MD5CryptoServiceProvider().ComputeHash(fraseCodificada)

        ElseIf (SHA256.Checked = True) Then
            ByteHash = New SHA256CryptoServiceProvider().ComputeHash(fraseCodificada)

        ElseIf (SHA384.Checked = True) Then
            ByteHash = New SHA384CryptoServiceProvider().ComputeHash(fraseCodificada)

        ElseIf (SHA512.Checked = True) Then
            ByteHash = New SHA512CryptoServiceProvider().ComputeHash(fraseCodificada)

        End If


        Dim fraseHEX As New System.Text.StringBuilder(ByteHash.Length)
        For i = 0 To (ByteHash.Length - 1)
            fraseHEX.Append(ByteHash(i).ToString("X2"))
        Next
        text_resultado.Text = fraseHEX.ToString().ToLower()


    End Sub





    Private Sub tipo_encrypt(sender As Object, e As EventArgs) Handles radios_encrypt.Enter

    End Sub

    Private Sub tipo_archivo(sender As Object, e As EventArgs) Handles radios_text_arch.Enter

    End Sub

    Private Sub bt_comprobacion(sender As Object, e As EventArgs) Handles Button2.Click
        Dim resultado As String = text_resultado.Text
        Dim comprueba As String = text_comprueba.Text
        If (resultado = comprueba) Then
            MessageBox.Show("Mismo hash!!")
        Else
            MessageBox.Show("Diferente hash!!")
        End If

    End Sub

    Private Sub archivo_CheckedChanged(sender As Object, e As EventArgs) Handles archivo.CheckedChanged

        If (archivo.Checked = True) Then
            Dim path As String
            bt_generar.Enabled = False
            If elegir_archivo.ShowDialog = 1 Then
                path = elegir_archivo.FileName
                Dim RD As FileStream = New FileStream(path, FileMode.Open, FileAccess.Read, FileShare.Read)

                Dim ByteHash() As Byte
                If (MD5.Checked = True) Then
                    ByteHash = New MD5CryptoServiceProvider().ComputeHash(RD)

                ElseIf (SHA256.Checked = True) Then
                    ByteHash = New SHA256CryptoServiceProvider().ComputeHash(RD)

                ElseIf (SHA384.Checked = True) Then
                    ByteHash = New SHA384CryptoServiceProvider().ComputeHash(RD)

                ElseIf (SHA512.Checked = True) Then
                    ByteHash = New SHA512CryptoServiceProvider().ComputeHash(RD)

                End If
                Dim fraseHEX As New System.Text.StringBuilder(ByteHash.Length)
                For i = 0 To (ByteHash.Length - 1)
                    fraseHEX.Append(ByteHash(i).ToString("X2"))
                Next
                text_resultado.Text = fraseHEX.ToString().ToLower()
                text_introduce.Text = elegir_archivo.FileName
            End If

        Else
            bt_generar.Enabled = True
        End If


    End Sub

    Private Sub MD5_CheckedChanged(sender As Object, e As EventArgs) Handles MD5.CheckedChanged

    End Sub
End Class
