package com.example.alex.sablelaser;

import android.hardware.SensorManager;
import android.media.MediaPlayer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    private Acelerometer acelerometro;

    private boolean SaberOn;
    MediaPlayer sound_lightSaberOn;

    MediaPlayer sound_lightSaberOff;

    private final float minAcc = 3;

    long prevTimeSwing;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        sound_lightSaberOn = MediaPlayer.create(this, R.raw.light_saber_on);
        sound_lightSaberOff = MediaPlayer.create(this, R.raw.saberoff);
        acelerometro = new Acelerometer((SensorManager) getSystemService(SENSOR_SERVICE), this);
        SaberOn = false;

    }

    // Call accelerometer onResume
    protected void onResume() {
        super.onResume();
        acelerometro.onResume();
    }

    // Call accelerometer onPause
    protected void onPause() {
        super.onPause();
        acelerometro.onPause();
    }

    public void botonON(View view)
    {
        // Compute the time difference from the previous play
        long difference = System.currentTimeMillis() - prevTimeSwing;
        SaberOn = true;
        // If the 0.5 seconds have passed, play the sound.
        if (difference > 1000) {
            prevTimeSwing = System.currentTimeMillis();
            if(sound_lightSaberOn.isPlaying()){
                // Pause the sound and move the pointer to 100ms
                sound_lightSaberOn.pause();
                sound_lightSaberOn.seekTo(100);
            }
            sound_lightSaberOn.start();
        }
    }

    public void botonOFF(View view)
    {
        SaberOn = false;
        // Compute the time difference from the previous play
        long difference = System.currentTimeMillis() - prevTimeSwing;

        // If the 0.5 seconds have passed, play the sound.
        if (difference > 1000) {
            prevTimeSwing = System.currentTimeMillis();
            if(sound_lightSaberOff.isPlaying()){
                // Pause the sound and move the pointer to 100ms
                sound_lightSaberOff.pause();
                sound_lightSaberOff.seekTo(100);
            }
            sound_lightSaberOff.start();
        }
    }

    protected void lightSaberSwing(){
        // Compute the time difference from the previous play
        long difference = System.currentTimeMillis() - prevTimeSwing;

        // If the 0.5 seconds have passed, play the sound.
        if(SaberOn){
            if (difference > 1000) {
                prevTimeSwing = System.currentTimeMillis();
                if(sound_lightSaberOn.isPlaying()){
                    // Pause the sound and move the pointer to 100ms
                    sound_lightSaberOn.pause();
                    sound_lightSaberOn.seekTo(100);
                }
                sound_lightSaberOn.start();
            }
        }
    }

    public void manageData(float[] data){

        // If the force in the X or Z axes is grater than a threshold, play the Swing sound
        // (the lightSaberSwing() function will check whether the lightsaber is on)
        if(Math.abs(data[0]) > minAcc ){
            lightSaberSwing();
        }
        else if (Math.abs(data[1])>minAcc)
        {
            lightSaberSwing();
        }
        else if (Math.abs(data[2])>minAcc)
        {
            lightSaberSwing();

        }

    }
}
