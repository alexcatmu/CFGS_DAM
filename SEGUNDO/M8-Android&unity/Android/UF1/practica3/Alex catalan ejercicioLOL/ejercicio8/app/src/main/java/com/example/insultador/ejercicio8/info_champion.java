package com.example.insultador.ejercicio8;

import android.content.res.Resources;
import android.content.res.XmlResourceParser;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import org.xmlpull.v1.XmlPullParser;
import org.xmlpull.v1.XmlPullParserException;
import org.xmlpull.v1.XmlPullParserFactory;

import java.io.IOException;
import java.io.InputStream;

public class info_champion extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_info_champion);
        ImageView img_bt = new ImageView(this);

        ResourceIdRetriever resourceIdRetriever = new ResourceIdRetriever(getResources(), "drawable", getPackageName());


        String nombreChamp = getIntent().getExtras().getString("putadon");
        Toast.makeText(this, nombreChamp, Toast.LENGTH_LONG).show();

        img_bt.setImageResource(resourceIdRetriever.GetId(nombreChamp));

        LinearLayout buttonContainer = (LinearLayout) findViewById(R.id.layout_champ);
        buttonContainer.addView(img_bt);

        ResourceIdRetriever resourceIdInfoChamp = new ResourceIdRetriever(getResources(), "string", getPackageName());

        String aux = "default";

        if(nombreChamp.equals("ashe")){
            aux = nombreChamp;
        }
        if(nombreChamp.equals("vayne")){
            aux = nombreChamp;
        }


        TextView tv_champinfo = new TextView(this);

        tv_champinfo.setText(nombreChamp);
        buttonContainer.addView(tv_champinfo);


        TextView tv_champname = new TextView(this);
        tv_champname.setText(resourceIdInfoChamp.GetId(aux+"_info"));
        buttonContainer.addView(tv_champname);




    }
}
