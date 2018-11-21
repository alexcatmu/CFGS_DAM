package m8.instagramalex;

import android.graphics.Bitmap;
import android.graphics.Color;

/**
 * Created by Alex on 17/03/2017.
 */

public class FilterBlackWhite extends Filter {


    @Override
    protected int PerPixelOperation(int color) {
        int a = Color.alpha(color);
        int r = Color.red(color);
        int g = Color.green(color);
        int b = Color.blue(color);
        int avg = (r + g + b) / 3;
        if (avg >= 100) {
            avg = 255;
        } else {
            avg = 0;
        }
        return Color.argb(a, avg, avg, avg);
    }
}
