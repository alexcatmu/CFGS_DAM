<?php

       $tireqty=$_POST['tireqty'];
       $oilqty=$_POST['oilqty'];
       $sparkqty=$_POST['sparkqty'];
       
       $sor=0;
       
       if (is_numeric($tireqty) && is_numeric($oilqty) && is_numeric($sparkqty)){
           $sor=1;
           echo $sor;
       } else {
           echo $sor;
       }
       
?>
