package com.example.insultador.ejercicio8;

import android.content.res.Resources;

import java.util.ResourceBundle;

/**
 * Created by alumneinf on 13/01/2017.
 */

public class ResourceIdRetriever {

    private Resources resources;
    private String tipo;
    private String packagename;

    public ResourceIdRetriever(Resources resources_c, String tipo_c, String packageName_c){
        this.resources = resources_c;
        this.tipo = tipo_c;
        this.packagename = packageName_c;
    }

    public int GetId(String resourceName){
        String name = RemoveWhiteSpaces(resourceName);
        return resources.getIdentifier(name, tipo, packagename);
    }

    private String RemoveWhiteSpaces(String resourceName){
        return resourceName.replace(" ", "");
    }
}
