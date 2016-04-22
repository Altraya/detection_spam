function changeSelectX() 
{
	selectX = $("#xParameter").val();
	console.log(selectX);
	return selectX;
/*
	choiceX = selectX.selectedIndex;
	choiceY = selectY.selectedIndex;

	valeurX = selectX.options[choiceX].value;
	valeurY = selectY.options[choiceY].value;

	console.log(valeurX);
	console.log(valeurY);*/
}

function changeSelectY()
{
	selectY = $("#yParameter").val();
	console.log(selectY);
	return selectY;
}