<?php 

if(isset($_GET['second'])) {
	exec("del /f /q result\*.*");
	$requete='python ./python_script/tf_ifd.py ';
	$requete=$requete.$_GET['second'];
	if(isset($_GET['theme'])){
		$requete=$requete.' '.$_GET['theme'];
	}
	if(isset($_GET['json-file'])) {
		$requete=$requete.' json';
	}
	if(isset($_GET['xlsx-file'])) {
		$requete=$requete.' xlsx';
	}
	if(isset($_GET['sql-file'])) {
		$requete=$requete.' sql';
	}
	echo $requete;

	$outpout=shell_exec($requete);
	header('Location: table');
}
else{

?>


<!DOCTYPE html>
<html lang="en">
<head>
	<title>TF-IDF</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="fonts/Linearicons-Free-v1.0.0/icon-font.min.css">
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">	
	<link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
</head>
<body>
	
	<div class="limiter">
		<div class="container-login100">
			<div class="wrap-login100 p-l-50 p-r-50 p-t-77 p-b-30">
				<form class="login100-form validate-form">
					<span class="login100-form-title p-b-55">
						COMPUTE IDF - IF
					</span>

					<div class="wrap-input100 validate-input m-b-16" data-validate = "Nomber of seconde is required:">
						<input class="input100" type="text" name="second" placeholder="Nomber of second">
						<span class="focus-input100"></span>
						<span class="symbol-input100">
							<span class="lnr lnr-clock"></span>
						</span>
					</div>

					<div class="wrap-input100 validate-input m-b-16">
						<input class="input100" type="text" name="theme" placeholder="Theme do you want">
						<span class="focus-input100"></span>
						<span class="symbol-input100">
							<span class="lnr lnr-layers"></span>
						</span>
					</div>

					<div class="contact100-form-checkbox m-l-4">
						<input class="input-checkbox100" id="ckb1" type="checkbox" name="json-file">
						<label class="label-checkbox100" for="ckb1">
							Do save json file
						</label>
					</div>
					<div class="contact100-form-checkbox m-l-4">
						<input class="input-checkbox100" id="ckb2" type="checkbox" name="sql-file">
						<label class="label-checkbox100" for="ckb2">
							Do sql file
						</label>
					</div>
					<div class="contact100-form-checkbox m-l-4">
						<input class="input-checkbox100" id="ckb3" type="checkbox" name="xlsx-file">
						<label class="label-checkbox100" for="ckb3">
							Do Excel file
						</label>
					</div>
					
					<div class="container-login100-form-btn p-t-25">
						<button class="login100-form-btn">
							LUNCH
						</button>
					</div>


				
				</form>
			</div>
		</div>
	</div>
	

<script src="vendor/jquery/jquery-3.2.1.min.js">
</script><script src="vendor/bootstrap/js/popper.js"></script>
<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<script src="vendor/select2/select2.min.js"></script>
<script src="js/main.js"></script>

</body>
</html>

<?php
}
?>
