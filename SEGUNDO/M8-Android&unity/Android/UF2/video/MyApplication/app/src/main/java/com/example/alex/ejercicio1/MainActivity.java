package com.example.alex.ejercicio1;

import android.media.MediaPlayer;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.MotionEvent;
import android.widget.MediaController;


public class MainActivity extends ActionBarActivity implements MediaController.MediaPlayerControl {

    // Atributs de l'activitat
    MediaPlayer so;
    MediaController controls;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        so = MediaPlayer.create(this, R.raw.blues);
        controls = new MediaController(this);
        controls.setMediaPlayer(this);
        controls.setAnchorView(findViewById(R.id.vista_controls_so));
    }

    // Mètodes de l'activitat
    @Override
    public boolean onTouchEvent(MotionEvent event) {
        controls.show();
        return false;
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        so.stop();
        so.release();
    }

    @Override
    public void start() {
        so.start();
    }

    @Override
    public void pause() {
        // Quan l'usuari toca el botó de pausa
        so.pause();
    }

    @Override
    public int getDuration() {
        // Torna la durada de la pista d'audio
        return so.getDuration();
    }

    @Override
    public int getCurrentPosition() {
        // Torna la posició actual a la pista d'audio
        return so.getCurrentPosition();
    }

    @Override
    public void seekTo(int pos) {
        // Per anar a una posició de la pista
        so.seekTo(pos);
    }

    @Override
    public boolean isPlaying() {
        // Torna cert quan s'està reproduint audio
        return so.isPlaying();
    }

    @Override
    public int getBufferPercentage() {
        return 0;
    }

    @Override
    public boolean canPause() {
        return true;
    }

    @Override
    public boolean canSeekBackward() {
        return false;
    }

    @Override
    public boolean canSeekForward() {
        return false;
    }

    @Override
    public int getAudioSessionId() {
        return 0;
    }

}
