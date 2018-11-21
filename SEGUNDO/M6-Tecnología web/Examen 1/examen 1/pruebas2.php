<?php
       $list= $_POST['list'];
       $fp = fopen("order.txt",'a');
       $posicion=0;
       $aux = "";
       
       while(!feof($fp))
       { 
           $orderLinea ="";
           for ($i=0;$i<4;$i++)
           {
               $orderLinea= fgetcsv($fp,1024, "\t");
               
           }
           
           if (!in_array($posicion, $list))
           {
               $aux =($orderLinea[4]*2);
               fwrite($fp, $aux);
               //$aux.= $orderLinea;
           }
            
           $posicion = $posicion + 1;
       }
       
       
   //fclose($fp);
   //$fp = fopen("order.txt", 'w');
   //fwrite($fp, $aux);
   //fclose($fp);
?>


