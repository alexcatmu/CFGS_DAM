package com.example.insultador.ejercicio8;

import android.content.Context;
import android.content.Intent;
import android.content.res.Resources;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Layout;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageButton;
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
        ResourceIdRetriever resourceId = new ResourceIdRetriever(getResources(), "array", getPackageName());
        int id = resourceId.GetId(tipo);

        final String[] nombres = getResources().getStringArray(id);

        LinearLayout buttonContainer = (LinearLayout) findViewById(R.id.layout_campeones);
        buttonContainer.removeAllViews();

        for (int i = 0;i < nombres.length; i++) {
            final ImageButton img_bt = new ImageButton(this);
            ResourceIdRetriever resourceIdRetriever = new ResourceIdRetriever(getResources(), "drawable", getPackageName());
            img_bt.setImageResource(resourceIdRetriever.GetId(nombres[i].toLowerCase()));

            final int finalI = i;
            img_bt.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    String joder = "yeeee";
                    Intent intent = new Intent(MainActivity.this, info_champion.class);
                    intent.putExtra("putadon",nombres[finalI].toLowerCase());
                    startActivity(intent);
                }
            });
            buttonContainer.addView(img_bt);

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
