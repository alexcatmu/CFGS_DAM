Imports System.Threading
Imports System.IO.StreamReader

Module Module1

    Private hilo1 As Thread
    Private hilo2 As Thread
    Private tiempohilos As Long
    Private tiempoprincipal As Long

    Sub Main()
        hilo1 = New Thread(AddressOf proceso)
        hilo2 = New Thread(AddressOf proceso)

        hilo1.Name = "Fichero1"
        tiempohilos = DateTime.Now.Ticks


        hilo1.Start("Fichero1")
        Thread.Sleep(100)
        hilo2.Name = "Fichero2"

        hilo2.Start("Fichero2")

        tiempoprincipal = DateTime.Now.Ticks

        hiloPrincipal("Fichero1")
        hiloPrincipal("Fichero2")

        Console.ReadLine()



    End Sub

    Private Sub proceso(ByVal Parametro As Object)
        Dim leerFichero As New Fichero(Thread.CurrentThread.Name + ".txt")

        Dim datos() As Integer = leerFichero.CuentaLetras()

        Dim palabras As Integer = datos(0)

        Dim letras As Integer = datos(1)

        Console.WriteLine(Thread.CurrentThread.Name + " palabras: " + Convert.ToString(palabras))
        Console.WriteLine(Thread.CurrentThread.Name + " letras: " + Convert.ToString(letras))

        If (Thread.CurrentThread.Name = "Fichero2") Then
            Dim finhilos As Long = DateTime.Now.Ticks
            Dim total As Long = finhilos - tiempohilos - 100
            Console.WriteLine("Tiempo en ejecutar los dos hilos: " + Convert.ToString(total))
        End If




    End Sub

    Private Sub hiloPrincipal(file)

        Dim leerFichero As New Fichero(file + ".txt")

        Dim datos() As Integer = leerFichero.CuentaLetras()

        Dim palabras As Integer = datos(0)

        Dim letras As Integer = datos(1)

        Console.WriteLine("principal " + file + " palabras: " + Convert.ToString(palabras))
        Console.WriteLine("principal " + file + " letras: " + Convert.ToString(letras))
        If (file = "Fichero2") Then
            Dim finprincipal As Long = DateTime.Now.Ticks
            Dim total As Long = finprincipal - tiempoprincipal
            Console.WriteLine("Tiempo en ejecutar los dos hilos: " + Convert.ToString(total))
        End If

    End Sub

End Module
