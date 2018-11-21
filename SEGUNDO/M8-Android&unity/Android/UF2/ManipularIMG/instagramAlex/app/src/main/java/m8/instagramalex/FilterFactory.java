package m8.instagramalex;

/**
 * Created by Alex on 24/03/2017.
 */

public class FilterFactory implements IfilterFactory{
    public Ifilter GetFilter(String Filtertype){
        Ifilter filter = null;
        switch (Filtertype){
            case "BlackWhite":
                filter = new FilterBlackWhite();
                break;
            case "GrayScale":
                filter = new FilterGrayScale();
                break;
            case "SepiaScale":
                filter = new FilterSepia();
                break;
        }
        return filter;
    }
}
