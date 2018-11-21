package m8.instagramalex;

import android.graphics.Bitmap;
import android.graphics.Color;

/**
 * Created by Alex on 17/03/2017.
 */

public class FilterSepia extends Filter {

    @Override
    protected int PerPixelOperation(int color) {
        int a = Color.alpha(color);
        int r = Color.red(color);
        int g = Color.green(color);
        int b = Color.blue(color);

        int red = (int) ((r * .393) + (g *.769) + (b * .189));
        int green = (int) ((r * .349) + (g *.686) + (b * .168));
        int blue = (int)((r * .272) + (g *.534) + (b * .131));
        if(red > 255) red = 255;
        if(green > 255) green = 255;
        if(blue > 255) blue = 255;

        if(red < 0) red = 0;
        if(green < 0) green = 0;
        if(blue < 0) blue = 0;

        return Color.argb(a, red, green, blue);
    }
}
