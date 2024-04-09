Proceso NumAdiv
	Definir numeroadivinar, intentos, intentousuario, acertado, dificulty Como Entero;
	
	Escribir "ADIVINE EL NUMERO!";
	Esperar 1 Segundos;
	
	Escribir "Seleccione la  dificultad:";
	Esperar 1 Segundos;
	Escribir "1.- Facil";
	Escribir "2.- Normal";
	Escribir "3.- Dificil";
	Escribir "4.- Pitiao";
	
	Leer dificulty;
	si dificulty==1 Entonces
		numeroadivinar<-Aleatorio(1,10);
		intentos<-3;
		Escribir "Ingrese un numero del 1 al 10";
		Esperar 1 Segundos;
		Escribir "Tiene 3 intentos";
	SiNo
		si dificulty==2 Entonces
			numeroadivinar<-Aleatorio(1,15);
			intentos<-3;
			Escribir "Ingrese un numero del 1 al 15";
			Esperar 1 Segundos;
			Escribir "Tiene 3 intentos";
		SiNo
			si dificulty==3 Entonces
				numeroadivinar<-Aleatorio(1,20);
				intentos<-3;
				Escribir "Ingrese un numero del 1 al 20";
			    Esperar 1 Segundos;
				Escribir "Tiene 3 intentos";
			SiNo
				si dificulty==4 Entonces
					numeroadivinar<-Aleatorio(1,100);
					intentos<-1;
					Escribir "Ingrese un numero del 1 al 100";
					Esperar 1 Segundos;
					Escribir "Tiene solo un intento";
				FinSi
			FinSi
		FinSi
	FinSi
	
	Esperar 1 Segundos;
	Mientras intentos>0 Hacer
		Leer intentousuario;
		Si intentousuario==numeroadivinar Entonces
			Escribir "Felicidades!";
			intentos=0;
		SiNo
			intentos=intentos-1;
			si intentousuario>numeroadivinar Entonces
				Escribir "Es mayor al numero a adivinar";
			SiNo
				si intentos<numeroadivinar Entonces
					Escribir "Es menor al numero a adivinar";
				FinSi
			FinSi
		FinSi
	FinMientras
	
	Si intentousuario==numeroadivinar Entonces
		Escribir "Usted ha adivinado el numero";
	SiNo
		Escribir "Resultados:";
		Esperar 1 Segundos;
		Escribir "Usted no ha advinado el numero";
		Escribir "El numero era ", numeroadivinar;
	FinSi
FinProceso
