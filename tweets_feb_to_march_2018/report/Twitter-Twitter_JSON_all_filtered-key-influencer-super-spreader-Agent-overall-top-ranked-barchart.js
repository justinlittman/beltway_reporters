Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['mkraju','jaketapper','JakeSherman','HotlineJosh','Acosta','AllMattNYT','AlexNBCNews',],
datasets : [
{
label: 'Agent (Twitter JSON all_filtered)',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
data : [66.6667,66.6667,33.3333,33.3333,33.3333,33.3333,33.3333,]
},
]
}
var context = document.getElementById('Twitter-Twitter_JSON_all_filtered-key-influencer-super-spreader-Agent-overall-top-ranked-barchart').getContext("2d");
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

