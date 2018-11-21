Public Class Fichero

    Dim rutaFichero As String

    Sub New(ByVal rutaFichero_c As String)
        rutaFichero = rutaFichero_c
    End Sub

    Function LeerFichero()
        Dim palabras As Integer
        Dim letras As Integer
        Using reader As New System.IO.StreamReader(rutaFichero)

            Dim letraAnterior As Boolean
            letraAnterior = False

            While Not reader.EndOfStream
                Dim buffer(1) As Char
                reader.Read(buffer, 0, 1)

                If (Char.IsLetter(buffer(0))) Then
                    letraAnterior = True
                    letras += 1
                End If

                If ((Char.IsWhiteSpace(buffer(0))) And (letraAnterior = True)) Then
                    palabras += 1
                    letraAnterior = False
                End If

            End While

        End Using

        Dim array_final() As Integer = {palabras, letras}
        Return array_final

    End Function

    Function CuentaLetras()
        Return LeerFichero()

    End Function
End Class
