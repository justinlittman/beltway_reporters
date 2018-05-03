Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['jaketapper','GlennThrush','ChadPergram','markknoller','CahnEmily','BretBaier','ZekeJMiller','JohnJHarwood','kasie','Phil_Mattingly','chucktodd','mitchellreports','jdickerson','Fahrenthold','JaredRizzi','HotlineJosh','JohnKingCNN','ryanbeckwith','Cory_Bennett','matmountain',],
datasets : [
{
label: 'Agent (Twitter JSON all)',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
data : [44.4444,22.2222,22.2222,22.2222,22.2222,11.1111,11.1111,11.1111,11.1111,11.1111,11.1111,11.1111,11.1111,11.1111,11.1111,11.1111,11.1111,11.1111,11.1111,11.1111,]
},
]
}
var context = document.getElementById('Twitter-Twitter_JSON_all-key-influencer-Agent-overall-top-ranked-barchart').getContext("2d");
var chart = new Chart(context, {
		type: 'bar',
		data: data,
		options: {
			autowidth:false,
			scales: {
			yAxes: [{
				ticks: {
					beginAtZero:true
				}
			}]
		}
	}
});

