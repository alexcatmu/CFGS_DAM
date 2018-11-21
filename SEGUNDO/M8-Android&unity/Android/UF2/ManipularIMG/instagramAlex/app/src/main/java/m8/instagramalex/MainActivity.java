package m8.instagramalex;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.Color;
import android.graphics.drawable.BitmapDrawable;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import java.io.ObjectInputStream;


public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    private static final int SELECT_PICTURE = 1;
    ImageView visorImatge;
    Bitmap bitmap;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        visorImatge = (ImageView)findViewById(R.id.imgToGuapa);

        Button btnLoadImage = (Button) findViewById(R.id.loadImage);
        btnLoadImage.setOnClickListener(this);

        Button btnBlackWhite = (Button) findViewById(R.id.blackWhite);
        btnBlackWhite.setOnClickListener(this);

        Button btnGrayScale = (Button) findViewById(R.id.grayScale);
        btnGrayScale.setOnClickListener(this);

        Button btnOriginal = (Button) findViewById(R.id.original);
        btnOriginal.setOnClickListener(this);

        Button btnSepiaTone = (Button) findViewById(R.id.sepiaTone);
        btnSepiaTone.setOnClickListener(this);

        bitmap = ((BitmapDrawable)visorImatge.getDrawable()).getBitmap();

    }

    @Override
    public void onClick(View v) {
        IfilterFactory filterfactory = new FilterFactory();
        Ifilter filtro = null;
        switch (v.getId()) {
            case R.id.loadImage:
                loadImageUser();
                break;

            case R.id.blackWhite:
                filtro = filterfactory.GetFilter("BlackWhite");
                break;

            case R.id.grayScale:
                filtro = filterfactory.GetFilter("GrayScale");
                break;

            case R.id.original:
                visorImatge.setImageBitmap(bitmap);
                break;

            case R.id.sepiaTone:
                filtro = filterfactory.GetFilter("SepiaScale");
                break;
        }
        if(filtro != null) {
            visorImatge.setImageBitmap(filtro.ApplyFilter(bitmap));
        }
    }

    private void loadImageUser() {
        Intent intent = new Intent();
        intent.setType("image/*");
        intent.setAction(Intent.ACTION_GET_CONTENT);
        startActivityForResult(Intent.createChooser(intent, "Select Picture"), SELECT_PICTURE);
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (resultCode == Activity.RESULT_OK) {
            if (requestCode == SELECT_PICTURE) {
                Uri selectedImageUri = data.getData();
                visorImatge.setImageURI(selectedImageUri);
                bitmap = ((BitmapDrawable)visorImatge.getDrawable()).getBitmap();

            }
        }
    }
}
