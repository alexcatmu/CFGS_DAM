Imports System.Threading

Module Module1

    Private hilo1 As Thread
    Private hilo2 As Thread
    Private tiempohilo1 As Integer = 0
    Private tiempohilo2 As Integer = 0

    Sub Main()
        hilo1 = New Thread(AddressOf proceso)
        hilo2 = New Thread(AddressOf proceso)

        hilo1.Name = "hilo1"
        hilo1.Start("hilo1")
        Thread.Sleep(100)
        hilo2.Name = "hilo2"

        hilo2.Start("hilo2")



        Thread.Sleep(10000)

        hilo1.Abort()
        hilo2.Abort()
        While hilo1.IsAlive Or hilo2.IsAlive
            
        End While



            Console.WriteLine("hilo1 total: " & tiempohilo1)

            Console.WriteLine("hilo2 total: " & tiempohilo2)


        Dim respuesta As String = Console.ReadLine

    End Sub

    Private Sub proceso(ByVal Parametro As Object)



        Randomize()

        Dim i As Integer
        Dim thread_act As Thread

        thread_act = Thread.CurrentThread

        Try
            For i = 0 To 10
                Dim num_random As Integer = CInt((1000 * Rnd()))
                Console.WriteLine(Parametro & " " & num_random & thread_act.Name)

                If (thread_act.Name = "hilo1") Then
                    tiempohilo1 += num_random
                Else
                    tiempohilo2 += num_random
                End If
                Thread.Sleep(num_random)

            Next i

        Catch ex As ThreadAbortException

        End Try
    End Sub

End Module
