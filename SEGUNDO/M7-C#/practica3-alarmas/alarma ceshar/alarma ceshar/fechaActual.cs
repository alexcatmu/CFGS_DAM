using System;

public class fechaActual
{
    private int dia;
    public string fecha_actual;
	public fechaActual()
	{
        DateTime thisDay = DateTime.Today;
        this.fecha_actual = thisDay.ToString("D");
	}
}
