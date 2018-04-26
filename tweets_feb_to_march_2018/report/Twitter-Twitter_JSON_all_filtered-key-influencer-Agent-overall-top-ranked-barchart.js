Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['jaketapper','mkraju','JakeSherman','HotlineJosh','CahnEmily','mitchellreports','SamLitzinger','peterbakernyt','markknoller','SunlenSerfaty','BretBaier','chucktodd','jdickerson','RMSilverman','Aiacone',],
datasets : [
{
label: 'Agent (Twitter JSON all_filtered)',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
data : [55.5556,44.4444,22.2222,22.2222,22.2222,22.2222,22.2222,11.1111,11.1111,11.1111,11.1111,11.1111,11.1111,11.1111,11.1111,]
},
]
}
var context = document.getElementById('Twitter-Twitter_JSON_all_filtered-key-influencer-Agent-overall-top-ranked-barchart').getContext("2d");
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

