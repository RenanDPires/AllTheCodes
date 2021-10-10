<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="refresh" content="5" >
		<title>MedFasee BT</title>
	<head>
	
	<body>
		<style>
		#div1 {
		//background-color: lightpink;
		width: 50%;
		float: left;
		height: 720px;
		}		
		#div2 {
		//background-color: lightblue;
		width: 50%;
		float: right;
		height: 720px;
		}			
		</style>
		<div id="div1">
			<?php 
			include ("60Hz.php"); 
			?>
		</div>
		<div id="div2">
			<?php 
			include ("50Hz.php"); 
			?>
		</div>
	</body>
</html>