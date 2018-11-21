Imports System.Security.Cryptography
Imports System.IO
Public Class encriptacion
    Dim encriptar_des = New DESCryptoServiceProvider()
    Dim encriptar_tripleDes = New TripleDESCryptoServiceProvider()
    Dim encriptar_aes = New AesCryptoServiceProvider()
    Dim encriptar_RSA As New RSACryptoServiceProvider()

    Private Shared dirPruebas As String = "claveRSA"
    Private Shared ficPruebas As String = Path.Combine(dirPruebas, "MisClaves.xml")

    Private Sub btDES_Click(sender As Object, e As EventArgs) Handles btDES.Click
        If (RBencriptar.Checked = True) Then
            Try
                encriptarDES()
            Catch ex As Exception
                MessageBox.Show(ex.Message)
                MessageBox.Show("Stack Trace: " & vbCrLf & ex.StackTrace)
            End Try

        End If

        If (RBdesencriptar.Checked = True) Then
            Try
                desencriptarDES()
            Catch ex As Exception
                MessageBox.Show(ex.Message)
                MessageBox.Show("Stack Trace: " & vbCrLf & ex.StackTrace)
            End Try
        End If
    End Sub


    Private Sub btTripleDES_Click(sender As Object, e As EventArgs) Handles btTripleDES.Click
        If (RBencriptar.Checked = True) Then
            Try
                encriptartripleDES()
            Catch ex As Exception
                MessageBox.Show(ex.Message)
                MessageBox.Show("Stack Trace: " & vbCrLf & ex.StackTrace)
            End Try
        End If

        If (RBdesencriptar.Checked = True) Then
            Try
                desencriptartripleDES()
            Catch ex As Exception
                MessageBox.Show(ex.Message)
                MessageBox.Show("Stack Trace: " & vbCrLf & ex.StackTrace)
            End Try
        End If
    End Sub

    Private Sub btAES_Click(sender As Object, e As EventArgs) Handles btAES.Click
        If (RBencriptar.Checked = True) Then
            Try
                encriptarAes()
            Catch ex As Exception
                MessageBox.Show(ex.Message)
                MessageBox.Show("Stack Trace: " & vbCrLf & ex.StackTrace)
            End Try
        End If

        If (RBdesencriptar.Checked = True) Then
            Try
                desencriptarAes()
            Catch ex As Exception
                MessageBox.Show(ex.Message)
                MessageBox.Show("Stack Trace: " & vbCrLf & ex.StackTrace)
            End Try
        End If
    End Sub


    Private Sub btRSA_Click(sender As Object, e As EventArgs) Handles btRSA.Click
        If (RBencriptar.Checked = True) Then
            Try
                encriptarRSA()
            Catch ex As Exception
                MessageBox.Show(ex.Message)
                MessageBox.Show("Stack Trace: " & vbCrLf & ex.StackTrace)
            End Try
        End If

        If (RBdesencriptar.Checked = True) Then
            Try
                desencriptarRSA()
            Catch ex As Exception
                MessageBox.Show(ex.Message)
                MessageBox.Show("Stack Trace: " & vbCrLf & ex.StackTrace)
            End Try
        End If
    End Sub

    Private Sub encriptarDES()
        Me.encriptar_des.GenerateKey()
        Dim fraseCodificada() As Byte = System.Text.Encoding.Unicode.GetBytes(texto_original.Text)
        Dim Stream = New System.IO.MemoryStream
        Dim texto_stream = New CryptoStream(Stream, Me.encriptar_des.CreateEncryptor(), CryptoStreamMode.Write)
        texto_stream.Write(fraseCodificada, 0, fraseCodificada.Length)
        texto_stream.FlushFinalBlock()
        Dim cifrado_str = Convert.ToBase64String(Stream.ToArray)
        texto_encript.Text = cifrado_str
    End Sub

    Private Sub encriptartripleDES()
        Me.encriptar_tripleDes.GenerateKey()
        Dim fraseCodificada() As Byte = System.Text.Encoding.Unicode.GetBytes(texto_original.Text)
        Dim Stream = New System.IO.MemoryStream
        Dim texto_stream = New CryptoStream(Stream, Me.encriptar_tripleDes.CreateEncryptor(), CryptoStreamMode.Write)
        texto_stream.Write(fraseCodificada, 0, fraseCodificada.Length)
        texto_stream.FlushFinalBlock()
        Dim cifrado_str = Convert.ToBase64String(Stream.ToArray)
        texto_encript.Text = cifrado_str
    End Sub

    Private Sub encriptarAes()
        Me.encriptar_aes.GenerateKey()
        Dim fraseCodificada() As Byte = System.Text.Encoding.Unicode.GetBytes(texto_original.Text)
        Dim Stream = New System.IO.MemoryStream
        Dim texto_stream = New CryptoStream(Stream, Me.encriptar_aes.CreateEncryptor(), CryptoStreamMode.Write)
        texto_stream.Write(fraseCodificada, 0, fraseCodificada.Length)
        texto_stream.FlushFinalBlock()
        Dim cifrado_str = Convert.ToBase64String(Stream.ToArray)
        texto_encript.Text = cifrado_str
    End Sub

    Private Sub encriptarRSA()
        Dim claves As String

        claves = encriptar_RSA.ToXmlString(True)
        Dim s_writer As New StreamWriter(ficPruebas, False)
        s_writer.WriteLine(claves)
        s_writer.Close()

        Dim string_claves As String
        Dim lector As New StreamReader(ficPruebas)
        string_claves = lector.ReadToEnd
        lector.Close()
        encriptar_RSA.FromXmlString(string_claves)

        Dim texto_enc As Byte() = encriptar_RSA.Encrypt(System.Text.Encoding.Unicode.GetBytes(texto_original.Text), False)
        Dim texto_enc_decode As String = Convert.ToBase64String(texto_enc.ToArray)
        texto_encript.Text = texto_enc_decode

    End Sub


    Private Sub desencriptartripleDES()

        Dim encryptedBytes() As Byte = Convert.FromBase64String(texto_encript.Text)
        Dim ms As New System.IO.MemoryStream
        Dim decStream As New CryptoStream(ms, Me.encriptar_tripleDes.CreateDecryptor, CryptoStreamMode.Write)

        decStream.Write(encryptedBytes, 0, encryptedBytes.Length)
        decStream.FlushFinalBlock()

        texto_decript.Text = System.Text.Encoding.Unicode.GetString(ms.ToArray)
    End Sub

    Private Sub desencriptarDES()

        Dim encryptedBytes() As Byte = Convert.FromBase64String(texto_encript.Text)
        Dim ms As New System.IO.MemoryStream
        Dim decStream As New CryptoStream(ms, Me.encriptar_des.CreateDecryptor, CryptoStreamMode.Write)

        decStream.Write(encryptedBytes, 0, encryptedBytes.Length)
        decStream.FlushFinalBlock()

        texto_decript.Text = System.Text.Encoding.Unicode.GetString(ms.ToArray)
    End Sub

    Private Sub desencriptarAes()

        Dim encryptedBytes() As Byte = Convert.FromBase64String(texto_encript.Text)
        Dim ms As New System.IO.MemoryStream
        Dim decStream As New CryptoStream(ms, Me.encriptar_aes.CreateDecryptor, CryptoStreamMode.Write)

        decStream.Write(encryptedBytes, 0, encryptedBytes.Length)
        decStream.FlushFinalBlock()

        texto_decript.Text = System.Text.Encoding.Unicode.GetString(ms.ToArray)
    End Sub

    Private Sub desencriptarRSA()

        Dim Bytes() As Byte = Convert.FromBase64String(texto_encript.Text)

        Dim key_xml As String
        Dim read As New StreamReader(ficPruebas)
        key_xml = read.ReadToEnd
        read.Close()

        Dim txt_dec As Byte() = encriptar_RSA.Decrypt(Bytes, False)
        Dim txt_dec_show As String = System.Text.Encoding.Unicode.GetString(txt_dec)

        texto_decript.Text = txt_dec_show

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim txt_show As String = "Seguir los pasos para utilizar correctamente" + vbCr
        txt_show += "La caja de arriba a la izquierda es el texto original que introduce el usuario, el de abajo a la izquierda es el texto cifrado(las claves las genera el código del programa) y la caja de abajo a la derecha es el texto descifrado. No intente hakiar plis" + vbCr
        txt_show += "1.- Elegir encriptar" + vbCr
        txt_show += "2.- Elegir el método de encriptación" + vbCr
        txt_show += "3.- Se mostrará el texto encriptado" + vbCr
        txt_show += "4.- Una vez esté el texto encriptado podemos marcar desencriptar y elegir el mismo método por el que hemos encriptado" + vbCr
        txt_show += "Nota: No intentar desencriptar por un método que no este encriptado, CAPTURARÉ su error"
        MessageBox.Show(txt_show)
    End Sub
End Class
