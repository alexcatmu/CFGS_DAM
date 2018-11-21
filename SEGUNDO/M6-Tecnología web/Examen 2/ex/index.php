<?php
    if(!isset($_GET['tireqty'])){
?>


        <!DOCTYPE html SYSTEM "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>


                <script type="text/JavaScript" src="jquery-1.7.2.min.js"></script>
                <script type="text/javascript">
                    
                    //Events en jQuery
                    $(document).ready(function(){

                                //En clicar en l'input de tipus button genera'
                                //Em cal l'event live donat que estic afegint codi html dinàmicament'
                                $('input[type=button]').live("click", function(){
                                    valida();
                                });

                    });


                    function valida(){

                            //Primer que res recullo el valor dels tres camps usant AJAX
                            var u=jQuery('input:eq(0)').attr('value');
                            var dos=jQuery('input:eq(1)').attr('value');
                            var tres=jQuery('input:eq(2)').attr('value');

                            //Si un dels tres no és un nombre el posare a '' i a més el poso groc
                            //En cas siguin nombres els deixo en blanc
                            if(!jQuery.isNumeric(u)){
                                jQuery('input:eq(0)').attr('value','');
                                jQuery('input:eq(0)').attr('class','groc');  
                            } else {
                                jQuery('input:eq(0)').attr('class','none'); 
                            } 
                            if(!jQuery.isNumeric(dos)){
                                jQuery('input:eq(1)').attr('value','');
                                jQuery('input:eq(1)').attr('class','groc'); 
                            } else {
                                jQuery('input:eq(1)').attr('class','none'); 
                            }
                            if(!jQuery.isNumeric(tres)){
                                jQuery('input:eq(2)').attr('value','');
                                jQuery('input:eq(2)').attr('class','groc'); 
                            } else {
                                jQuery('input:eq(2)').attr('class','none'); 
                            }
                            
                            //Crifo a procesa perque faci el procesament en cas que calgui
                            procesa();


                        }

                        function procesa(){
                            //Primer que res recullo el valor dels tres camps usant AJAX
                            var atr1 = jQuery('input:eq(0)').attr('value');
                            var atr2 = jQuery('input:eq(1)').attr('value');
                            var atr3 = jQuery('input:eq(2)').attr('value');
                            //I miro si algun dels tres és null ja que els incorrectes els haure posat a null
                            if ((atr1 == '') || (atr2 == '') ||(atr3 == '')){

                                        //Vaig a fer aquí la creació del paràgraf per jQuery primer recollint el contingut del paragraf
                                        alert('cas dolent');
                                        var cont = jQuery('form').html();

                                        //Perquè no em dupliqui la frase torna a introduir les dades
                                        //conto quants elements strong hi ha i si no n'hi ha cap en poso un'
                                        if(jQuery('strong').length == 0){
                                            jQuery('form').html(cont + '<p><strong class="imp">Torna a introduir les dades!</strong></p>');
                                        }else{
                                            jQuery('form').html(cont);
                                        }

                                        //poso el valor perque html no l'agafa'
                                        if ((atr1 != '')){jQuery('input:eq(0)').attr('value',atr1);}
                                        if ((atr2 != '')){jQuery('input:eq(1)').attr('value',atr2);}
                                        if ((atr3 != '')){jQuery('input:eq(2)').attr('value',atr3);}
                                        jQuery('input:eq(3)').attr('value','submitorder');
                                    }
                                    else {

                                        //Em cal encara el valor seleccionat de com ens va trobar
                                        var fnd = jQuery('select').val();

                                        //Ara he de construir a ma la direcció
                                        var direccio='http://localhost/ex/index.php?tireqty='+atr1+'&oilqty='+atr2+'&sparkqty='+atr3+'&find='+fnd;

                                        document.location.href=direccio;
                                    }

                        }

                </script>

                <style type="text/css">
                    body {
                        padding: 40px;
                    }

                    form {
                        border: 1px solid;
                        padding: 15px;
                        width: 320px;
                        background-color: #ccffcc;
                    }
                    /*La regla per a posar en bermell el tema de l'important'*/
                    .imp{
                        color: red;
                        text-decoration: underline;
                    }
                    .groc{
                        background-color: greenyellow;
                    }


                </style>

                <title>Primer PHP</title>



            </head>
            <body>

                <form>
                    <table border="0">
                        <tr bgcolor="red">
                            <td width="150">Item</td>
                            <td width="150">Quantity</td>
                        </tr>
                        <tr>
                            <td>Tires</td>
                            <td align="center"><input type="text" name="tireqty" size="3" maxlength="3"/></td>
                        </tr>
                        <tr>
                            <td>Oil</td>
                            <td align="center"><input type="text" name="oilqty" size="3" maxlength="3"/></td>
                        </tr>
                        <tr>
                            <td>Spark plugs</td>
                            <td align="center"><input type="text" name="sparkqty" size="3" maxlength="3"/></td>
                        </tr>
                        <tr>
                            <td>How did you find us?</td>
                            <td align="center">
                                <select name="find">
                                    <option value="a">I am a regular costumer</option>
                                    <option value="b">Phone directory</option>
                                    <option value="c">Tv advertising</option>
                                    <option value="d">Others</option>
                                </select>
                            </td>

                        </tr>
                        <tr>
                            <td colspan="2" align="left"><input type="button" value="submitorder"/></td>
                        </tr>
                    </table>
                    
                    
                </form>
            </body>
        </html>
        
<?php
    }
    else {
?>

        <!DOCTYPE html SYSTEM "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>

                <style type="text/css">
                    table{
                        border: 2px solid;
                        
                        border-collapse: collapse;
                    }
                    thead{
                        
                        border-bottom: 2px solid;
                        background-color: red;
                    }
                    th{
                        padding: 5px;
                        align: center;
                        border: 1px solid;
                    }
                    td{
                        padding: 5px;
                        align: center;
                        border: 1px solid;
                    }
                    caption{
                        background-color: oldlace;
                        border-top: 1px solid;
                        padding: 5px;
                    }


                </style>
                
                <script type="text/JavaScript" src="jquery-1.7.2.min.js"></script>
                <script type="text/javascript">
                    
                    //Events en jQuery
                    $(document).ready(function(){

                                carrOpcSel();

                    });
                
                    //Funcio que carregarà dinàmicament les diferents opcions del
                    //select option
                    function carrOpcSel(){
                        //Determino el nombre de comandes introduides
                        var nombreS = jQuery('tbody tr','table:eq(0)').length;
                        var html='<option value="0">Escull una comanda</option>';
                        for(var i=1;i<=nombreS;i++){
                            var html=html+'<option value="'+i+'">'+i+'</option>';
                        }
                        alert(html);
                        jQuery('select').html(html);
                    }

            </script>
                <title>Comanda processada</title>

            </head>
            <body>


            <h1>Bob's auto parts</h1>
            <h2>Comanda processada</h2>

            <?php 

            //Procedeixo a guardar en un arxiu
            //Obro l'arxiu per afegir
            $fp = fopen("order.txt",'a');
            if(!$fp){
                        echo '<p>No he pogut emmagatzemar el contingut de la comanda. Torna a introduir-la</p>'; 
                    }
            else {
                        //recullo
                        $tireqty=$_GET['tireqty'];
                        $oilqty=$_GET['oilqty'];
                        $sparkqty=$_GET['sparkqty'];

                        $find=$_GET['find'];
                        
                        $total=$tireqty*2+$oilqty*5+$sparkqty*3;


                        $comanda=$tireqty."\t".$oilqty."\t".$sparkqty."\t".$find."\t".$total."\r\n";

                        fwrite($fp, $comanda);

                        fclose($fp);
                 }

           ?>  

                 <!--Tema de la impressió de tot el contingut de l'arxiu order.txt-->
            <br/>
            <table>
                <?php
                echo '<caption>Resum de comandes fins: '.  date('H:i, jS F').'</caption>';
                ?>
                <thead>
                    <tr>
                        <th>Tires</th><th>Oil</th><th>Spark plugs</th><th>Tipus client</th><th>Preu final</th>
                    </tr>
                </thead>
                <tbody>
            <?php 
            $fp = fopen("C:\wamp\www\ex\order.txt",'r');
            
            if(!$fp){
                        echo '<p>No he pogut emmagatzemar el contingut de la comanda. Torna a introduir-la</p>'; 
                    }
            else {
                        //Obro i ho poso tot en un array
                        $array=fgetcsv($fp,999,"\t");
                        
                        //Vaig extraient-los de 7 en 7 i els vaig imprimint  
                        $tireqty=$array[0];
                        $oilqty=$array[1];
                        $sparkqty=$array[2];
                        $find=$array[3];
                        $total=$array[4];
                        //Per la data faig dos fgets ja que amb el primer el que aconsegueixo es arribar fins a final de línia

                        while(!feof($fp)){
                            echo '<tr>';
                            
                            echo '<td>';
                            echo $tireqty;
                            echo '</td>';
                            
                            echo '<td>';
                            echo $oilqty;
                            echo '</td>';
                            
                            echo '<td>' . $sparkqty . '</td>';
                            
                            //PHP strcmp() Function 0 - if the two strings are equal
                            //IF té el 1 com a true i el 0 com a false
                            //Per això em cap posar el negat
                            if (!strcmp('a',$find)){ echo '<td>Has indicat que ets un client habitual</td>';
                            }
                            if (!strcmp('b',$find)){ echo '<td>Has indicat que ens has trobat a la guia telefonica</td>';
                            }
                            if (!strcmp('c',$find)){ echo "<td>Has indicat que ens has trobat gracies a l'anunci de TV</td>";
                            }
                            if (!strcmp('d',$find)) {  echo '<td>Has indicat que ens has trobat per altres causes</td>';              
                            }

                            //Calculo en el swuitch el total amb descompte i aquí l'imprimeixo

                            echo '<td>'. $total . '</td>';

                            echo '</tr>';
                            
                            //Continuo extraient-los 

                            $array=fgetcsv($fp,999,"\t");
                        
 
                            $tireqty=$array[0];
                            $oilqty=$array[1];
                            $sparkqty=$array[2];
                            $find=$array[3];
                            $total=$array[4];
                            
                        }

;
                        fclose($fp);
                 }
            

            
            echo '</tr></tbody></table>';



            ?>
                        
            <table>

                <caption>Modifica</caption>

                <thead>
                    <tr>
                        <th>Tires</th><th>Oil</th><th>Spark plugs</th><th>Selecciona</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><input type="text" name="tires" value=""></td><td><input type="text" name="oil" value=""></td><td><input type="text" name="spark" value=""></td><td></td>
                    </tr> 
                    
                   <tr>
                        <td colspan="3"><select name="escull">
                                    <option value="0">Escull una comanda</option>
                                    <option></option>
                                </select>
                        </td>
                        <td><input type="button" value="Modifica seleccionat" name="modificaBoto"/></td>
                    </tr>                        

                </tbody>
            </body>
        </html>
<?php
    }
?>
