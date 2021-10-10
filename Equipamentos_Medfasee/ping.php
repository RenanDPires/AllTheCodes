<?php
$iplist = array
(
	array("UFPA","192.168.2.1","DFL-210"),
	array("UFPA","192.168.2.2","RPV311"),
	array("UFPA","192.168.2.3","RT430"),
	array("UBIFEI","192.168.3.1","DFL-210"),
	array("UNIFEI","192.168.3.2","RPV311"),
	array("UNIFEI","192.168.3.3","RT420"),
	array("UnB","192.168.4.1","DFL-210"),
	array("UnB","192.168.4.2","RPV311"),
	array("UnB","192.168.4.3","RT430"),
	array("COPPE","192.168.5.1","DFL-210"),
	array("COPPE","192.168.5.2","RPV311"),
	array("COPPE","192.168.5.3","RT430")

);
$i = count($iplist);
$results = [];

for ($j=0;$j<$i;$j++){
	$ip = $iplist[$j][1];
	$ping = exec("ping -n 1 $ip", $output, $status);
	$results[] = $status;
}
	
echo '<font face=Courier New>';
echo "<table border=3 style=border-collapse:collapse>
<th bgcolor='orange' colspan=4> Equipamentos MedFasee BT 60Hz </th>
<tr>
<td bgcolor='lightblue' width=100>PMU</td>
<td bgcolor='lightblue' width=110>IP</td>
<td bgcolor='lightblue' width=150>Equipamento</td>
<td bgcolor='lightblue' width=100>Status</td>
</tr>";

foreach($results as $item =>$k){
	echo '<tr>';
	echo '<td>'.$iplist[$item][0].'</td>';
	echo '<td>'.$iplist[$item][1].'</td>';
	echo'<td>'.$iplist[$item][2].'</td>';
	if($results[$item]==0){
		echo '<td style=color:green>Online</td>';
	}
	else{
		echo '<td style=color:red>Offline</td>';
	}
	echo '</tr>';
}

echo "</table>";
echo '</font>';


?>
<?php
$iplist = array
(
	array("UFC","192.168.6.1","DFL-260"),
	array("UFC","192.168.6.2","RPV311"),
	array("UFC","192.168.6.3","RT430"),
	array("USP-SC","192.168.7.1","DFL-210"),
	array("USP-SC","192.168.7.2","RPV311"),
	array("USP-SC","192.168.7.3","RT430"),
	array("UTFPR","192.168.8.1","DFL-210"),
	array("UTFPR","192.168.8.2","RPV311"),
	array("UTFPR","192.168.8.3","RT430")
	);
$i = count($iplist);
$results = [];

for ($j=0;$j<$i;$j++){
	$ip = $iplist[$j][1];
	$ping = exec("ping -n 1 $ip", $output, $status);
	$results[] = $status;
}
	
echo '<font face=Courier New>';
echo "<table border=3 style=border-collapse:collapse>
<th bgcolor='orange' colspan=4> Equipamentos MedFasee BT 60Hz </th>
<tr>
<td bgcolor='lightblue' width=100>PMU</td>
<td bgcolor='lightblue' width=110>IP</td>
<td bgcolor='lightblue' width=150>Equipamento</td>
<td bgcolor='lightblue' width=100>Status</td>
</tr>";

foreach($results as $item =>$k){
	echo '<tr>';
	echo '<td>'.$iplist[$item][0].'</td>';
	echo '<td>'.$iplist[$item][1].'</td>';
	echo'<td>'.$iplist[$item][2].'</td>';
	if($results[$item]==0){
		echo '<td style=color:green>Online</td>';
	}
	else{
		echo '<td style=color:red>Offline</td>';
	}
	echo '</tr>';
}

echo "</table>";
echo '</font>';

?>
