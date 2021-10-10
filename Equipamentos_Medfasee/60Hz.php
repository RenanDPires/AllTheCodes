<?php
set_time_limit(500);
$iplist = array
(
	array("2","UFPA","192.168.2.1","192.168.2.2","192.168.2.3"),
	array("3","UNIFEI","192.168.3.1","192.168.3.2","192.168.3.3"),
	array("4","UNB","192.168.4.1","192.168.4.2","192.168.4.3"),
	array("5","COPPE","192.168.5.1","192.168.5.2","192.168.5.3"),
	array("6","UFC","192.168.6.1","192.168.6.2","192.168.6.3"),
	array("7","USP-SC","192.168.7.1","192.168.7.2","192.168.7.3"),
	array("8","UTFPR","192.168.8.1","192.168.8.2","192.168.8.3"),
	array("9","UFSC","192.168.1.111","192.168.1.113","192.168.1.114"),
	array("10","UNIR","192.168.10.1","192.168.10.2","192.168.10.3"),
	array("11","UFMT","192.168.11.1","192.168.11.2","192.168.11.3"),
	array("12","UNIPAMPA","192.168.12.1","192.168.12.2","192.168.12.3"),
	array("13","UFMG","192.168.13.1","192.168.13.2","192.168.13.3"),
	array("14","UFMS","192.168.14.1","192.168.14.2","192.168.14.3"),
	array("15","UFPE","192.168.15.1","192.168.15.2","192.168.15.3"),
	array("16","UFT","192.168.16.1","192.168.16.2","192.168.16.3"),
	array("17","UFMA","192.168.17.1","192.168.17.2","192.168.17.3"),
	array("18","UFJF","192.168.18.1","192.168.18.2","192.168.18.3"),
	array("19","UFBA","192.168.19.1","192.168.19.2","192.168.19.3"),
	array("20","UFRGS","192.168.20.1","192.168.20.2","192.168.20.3"),
	array("21","UFAC","192.168.21.1","192.168.21.2","192.168.21.3"),
	array("22","UFAM","192.168.22.1","192.168.22.2","192.168.22.3"),
	array("23","UNIFAP","192.168.23.1","192.168.23.2","192.168.23.3"),
	array("24","UFRR","192.168.24.1","192.168.24.2","192.168.24.3"),
	array("26","COPPE","192.168.26.1","192.168.26.2","192.168.26.3"),
	array("27","UNICAMP","192.168.27.1","192.168.27.2","192.168.27.3"),
	//array("28","UFPR***","192.168.28.1","192.168.28.2","192.168.28.3"),
	array("29","UFPI","192.168.29.1","192.168.29.2","192.168.29.3")
);
$i = count($iplist);
$results = [];
$results2 = [];
$results3 = [];

for ($j=0;$j<$i;$j++){
	$ip = $iplist[$j][2];
	$ping = exec("ping -n 1 $ip", $output, $status);
	$results[] = $status;
}
for ($j=0;$j<$i;$j++){
	$ip = $iplist[$j][3];
	$ping = exec("ping -n 1 $ip", $output, $status);
	$results1[] = $status;
}
for ($j=0;$j<$i;$j++){
	$ip = $iplist[$j][4];
	$ping = exec("ping -n 1 $ip", $output, $status);
	$results2[] = $status;
}
	
echo '<font face=Courier New>';
echo "<table border=3 style=border-collapse:collapse>
<th bgcolor='orange' colspan=5> Equipamentos MedFasee BT 60Hz </th>
<tr>
<td bgcolor='lightblue' width=50>ID</td>
<td bgcolor='lightblue' width=100>PMU</td>
<td bgcolor='lightblue' width=110>Firewall</td>
<td bgcolor='lightblue' width=150>RPV311/DR60</td>
<td bgcolor='lightblue' width=100>GPS</td>
</tr>";


foreach($results as $item =>$k){
	echo '<tr>';
	if($results[$item]==0 and $results1[$item]==0 and $results2[$item]==0){
		echo '<td bgcolor="lightgreen" style=color:black>'.$iplist[$item][0].'</td>';
	}
	else{
		echo '<td bgcolor="red" style=color:white>'.$iplist[$item][0].'</td>';
	}
	if($results[$item]==0 and $results1[$item]==0 and $results2[$item]==0){
		echo '<td bgcolor="lightgreen" style=color:black>'.$iplist[$item][1].'</td>';
	}
	else{
		echo '<td bgcolor="red" style=color:white>'.$iplist[$item][1].'</td>';
	}
	if($results[$item]==0){
		echo '<td bgcolor="lightgreen" style=color:black>Online</td>';
	}
	else{
		echo '<td bgcolor="red" style=color:white>Offline</td>';
	}
	if($results1[$item]==0){
		echo '<td bgcolor="lightgreen" style=color:black>Online</td>';
	}
	else{
		echo '<td bgcolor="red" style=color:white>Offline</td>';
	}
	if($results2[$item]==0){
		echo '<td bgcolor="lightgreen" style=color:black>Online</td>';
	}
	else{
		echo '<td bgcolor="red" style=color:white>Offline</td>';
	}
	echo '</tr>';
}

echo "</table>";
echo '</font>';
echo '<font face=Courier New>';
date_default_timezone_set('UTC');
echo 'Fim da consulta em: ';
echo date('d/m/y H:i:s');
echo ' UTC';
echo $status;

//echo '*** - Equipamentos sem acesso por não pertencerem ao projeto MedFasee';
?>