using System;

public class fechaActual
{
    private int dia;
	public fechaActual(int pdia)
	{
        this.dia = pdia;

	}

    public int  getDia(){

        return this.dia;
    }

    public void setDia(int pdia) {
        this.dia = pdia;
    }
}
