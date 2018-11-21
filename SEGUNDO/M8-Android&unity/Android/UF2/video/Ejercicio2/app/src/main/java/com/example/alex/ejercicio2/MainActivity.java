package com.example.alex.ejercicio2;

import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.MediaController;
import android.widget.VideoView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        VideoView visor = (VideoView)findViewById(R.id.videoView1);
        Uri video = Uri.parse("android.resource://" + getPackageName() + "/"
                + R.raw.castell);
        visor.setVideoURI(video);
        visor.setMediaController(new MediaController(this));
        visor.start();
    }
}
