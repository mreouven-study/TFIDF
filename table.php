<!DOCTYPE html>

<html lang="en">
<head>
	<title>TF-IDF</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
	<link rel="stylesheet" type="text/css" href="css/utiltable.css">
	<link rel="stylesheet" type="text/css" href="css/maintable.css">
</head>
<body>
	
	<?php
	if (file_exists('./result/result.json')){ 
	?>
	<div class="limiter">
		<div class="container-table100">
			<div class="wrap-table100">
					<div class="table">

						<div class="row header">
							<div class="cell">
								Name
							</div>
							<div class="cell">
								TF
							</div>
							<div class="cell">
								IDF
							</div>
							<div class="cell">
								TF-IDF
							</div>
						</div>
						<?php
						$jsons=file_get_contents("./result/result.json");
						$data =  json_decode($jsons);
						foreach($data as $json){
							echo '<div class="row">';
							echo '<div class="cell" data-title="Full Name">';
								echo '#'.$json->name;
							echo '</div>';
							echo '<div class="cell" data-title="TF">';
								echo $json->value->tf;
							echo '</div>';
							echo '<div class="cell" data-title="IDF">';
								echo $json->value->idf;
							echo '</div>';
							echo '<div class="cell" data-title="TF-IDF">';
								echo $json->value->tfidf;
							echo '</div>';
							echo '</div>';
						}
						?>
						
						

						

					</div>
			</div>
		</div>
	</div>


	<?php
	}
	else{
	?>
	<style>
		@import 'https://fonts.googleapis.com/css?family=Inconsolata';

html {
  min-height: 100%;
}

body {
  box-sizing: border-box;
  height: 100%;
  background-color: #000000;
  background-image: radial-gradient(#11581E, #041607);
  font-family: 'Inconsolata', Helvetica, sans-serif;
  font-size: 1.5rem;
  color: rgba(128, 255, 128, 0.8);
  text-shadow:
      0 0 1ex rgba(51, 255, 51, 1),
      0 0 2px rgba(255, 255, 255, 0.8);
}

.overlay {
  pointer-events: none;
  position: absolute;
  width: 100%;
  height: 100%;
  background:
      repeating-linear-gradient(
      180deg,
      rgba(0, 0, 0, 0) 0,
      rgba(0, 0, 0, 0.3) 50%,
      rgba(0, 0, 0, 0) 100%);
  background-size: auto 4px;
  z-index: 99;
}

.overlay::before {
  content: "";
  pointer-events: none;
  position: absolute;
  display: block;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  background-image: linear-gradient(
      0deg,
      transparent 0%,
      rgba(32, 128, 32, 0.2) 2%,
      rgba(32, 128, 32, 0.8) 3%,
      rgba(32, 128, 32, 0.2) 3%,
      transparent 100%);
  background-repeat: no-repeat;
  animation: scan 7.5s linear 0s infinite;
}

@keyframes scan {
  0%        { background-position: 0 -100vh; }
  35%, 100% { background-position: 0 100vh; }
}

.terminal {
  box-sizing: inherit;
  position: absolute;
  height: 100%;
  width: 1000px;
  max-width: 100%;
  padding: 4rem;
  text-transform: uppercase;
}

.output {
  color: rgba(128, 255, 128, 0.8);
  text-shadow:
      0 0 1px rgba(51, 255, 51, 0.4),
      0 0 2px rgba(255, 255, 255, 0.8);
}

.output::before {
  content: "> ";
}


a {
  color: #fff;
  text-decoration: none;
}

a::before {
  content: "[";
}

a::after {
  content: "]";
}

.errorcode {
  color: white;
}
	</style>
	<div class="overlay"></div>
	<div class="terminal">
  <h1>Error <span class="errorcode">230</span></h1>
  <p class="output">.json file is require</ü>
  <p class="output">Good luck</p>
	</div>

	<?php	
		
	}
	?>
	
<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<script src="vendor/bootstrap/js/popper.js"></script>
<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<script src="vendor/select2/select2.min.js"></script>
<script src="js/table.js"></script>

</body>
</html>