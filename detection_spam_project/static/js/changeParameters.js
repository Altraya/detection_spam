/*
	Permet de recuperer l'id du select pour l'axe x
	@params : resultNormalize : le tableau avec toutes les valeurs normalisées
*/
function changeSelectX(resultNormalize) 
{
	selectX = $("#xParameter").val();
	indexX = $("#xParameter").index(); //always 0 i dont know why
	console.log(indexX);
	console.log(selectX);
	console.log(indexX);
	/*for (var i = resultNormalize.length - 1; i++) {
		resultNormalize[i]
	}
	return selectX;*/
}

function changeSelectY(resultNormalize)
{
	selectY = $("#yParameter").val();
	console.log(selectY);
	return selectY;
}