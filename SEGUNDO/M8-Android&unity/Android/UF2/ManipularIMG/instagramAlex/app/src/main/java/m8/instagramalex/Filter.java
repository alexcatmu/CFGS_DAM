package m8.instagramalex;

import android.graphics.Bitmap;
import android.graphics.Color;

/**
 * Created by Alex on 17/03/2017.
 */

public abstract class Filter implements Ifilter{

    public Bitmap ApplyFilter (Bitmap bitmap) {
        Bitmap mutableBitmap = bitmap.copy(Bitmap.Config.ARGB_8888, true);
        for (int i = 0; i < bitmap.getWidth(); i++) {

            for (int j = 0; j < bitmap.getHeight(); j++) {

                int color = bitmap.getPixel(i, j);

                int modifiedColor = PerPixelOperation(color);

                mutableBitmap.setPixel(i, j, modifiedColor);

            }
        }
        return mutableBitmap;
    }

    protected abstract int PerPixelOperation(int color);
}
