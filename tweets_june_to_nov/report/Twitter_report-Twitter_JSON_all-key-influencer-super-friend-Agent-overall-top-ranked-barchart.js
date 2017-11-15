Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['jmartNYT','BresPolitico','daveweigel','AaronMehta','ericgeller','BenjySarlin','jaketapper','CahnEmily',],
datasets : [
{
label: 'Agent (Twitter JSON all)',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
data : [75,50,50,25,25,25,25,25,]
},
]
}
var context = document.getElementById('Twitter_report-Twitter_JSON_all-key-influencer-super-friend-Agent-overall-top-ranked-barchart').getContext("2d");
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

