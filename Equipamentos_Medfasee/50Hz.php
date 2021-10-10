<?php
set_time_limit(500);
$iplist = array
(
	array("201","Argentina - UNT","192.168.48.1","192.168.48.2","192.168.48.3"),

);
$i = count($iplist);
$results4 = [];
$results5 = [];
$results6 = [];

for ($j=0;$j<$i;$j++){
	$ip = $iplist[$j][2];
	$ping = exec("ping -n 1 $ip", $output, $status);
	$results4[] = $status;
}
for ($j=0;$j<$i;$j++){
	$ip = $iplist[$j][3];
	$ping = exec("ping -n 1 $ip", $output, $status);
	$results5[] = $status;
}
for ($j=0;$j<$i;$j++){
	$ip = $iplist[$j][4];
	$ping = exec("ping -n 1 $ip", $output, $status);
	$results6[] = $status;
}
echo '<font face=Courier New>';
echo "<table border=3 style=border-collapse:collapse>
<th bgcolor='orange' colspan=5> Equipamentos MedFasee BT 50Hz </th>
<tr>
<td bgcolor='lightblue' width=50>ID</td>
<td bgcolor='lightblue' width=200>PMU</td>
<td bgcolor='lightblue' width=110>Firewall</td>
<td bgcolor='lightblue' width=150>RPV311/DR60</td>
<td bgcolor='lightblue' width=100>GPS</td>
</tr>";


foreach($results4 as $item =>$k){
	echo '<tr>';
	echo '<td>'.$iplist[$item][0].'</td>';
	echo '<td>'.$iplist[$item][1].'</td>';
	if($results4[$item]==0){
		echo '<td style=color:green>Online</td>';
	}
	else{
		echo '<td style=color:red>Offline</td>';
	}
	if($results5[$item]==0){
		echo '<td style=color:green>Online</td>';
	}
	else{
		echo '<td style=color:red>Offline</td>';
	}
	if($results6[$item]==0){
		echo '<td style=color:green>Online</td>';
	}
	else{
		echo '<td style=color:red>Offline</td>';
	}
	echo '</tr>';
}

echo "</table>";
echo '</font>';
echo '<font face=Courier New>';
echo 'Fim da consulta em: ';
echo date('d/m/y H:i:s');
echo ' UTC';

//echo '*** - Equipamentos sem acesso por não pertencerem ao projeto MedFasee';
?>