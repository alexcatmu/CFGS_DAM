package com.example.insultador.ejercicio8;

import android.content.res.Resources;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Layout;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.Spinner;
import android.widget.Toast;


public class MainActivity extends AppCompatActivity  implements AdapterView.OnItemSelectedListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        GeneraSpinner();

    }


    private void GeneraSpinner(){

        Spinner spinner = (Spinner) findViewById(R.id.sp_tipo);
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
                R.array.array_tipos_campeones, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        spinner.setOnItemSelectedListener(this);

    }

    public void Generabotones(String tipo){
        int id = getResources().getIdentifier(tipo, "array", getPackageName());
        String[] nombres = getResources().getStringArray(id);

        LinearLayout buttonContainer = (LinearLayout) findViewById(R.id.layout_campeones);
        buttonContainer.removeAllViews();

        for (int i = 0;i < nombres.length; i++) {

            Button button = new Button(this);
            button.setText(nombres[i]);
            buttonContainer.addView(button);

        }

    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {

        Spinner spinner = (Spinner) findViewById(R.id.sp_tipo);
        String nombre_spin = String.valueOf(spinner.getSelectedItem()).toLowerCase();
        Generabotones("camps_"+nombre_spin);

    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }
}
